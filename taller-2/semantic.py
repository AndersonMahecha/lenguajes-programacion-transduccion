import sys

from antlr4 import *
from antlr4.InputStream import InputStream
from antlr4.tree.Tree import TerminalNodeImpl

from generatedcode.lenguajeLexer import lenguajeLexer
from generatedcode.lenguajeParser import lenguajeParser
from generatedcode.lenguajeVisitor import lenguajeVisitor


class Context:

    def __init__(self, parent=None, t=None):
        self.parent = parent
        self.t = t
        self.memory = {}

    def __str__(self):
        for key, value in self.memory.items():
            print(key, value, sep=": ", end="\n")
        self.parent.__str__()
        return ""

    def get(self, key):
        if key in self.memory:
            return self.memory[key]
        elif self.parent is not None:
            return self.parent.get(key)
        else:
            raise Exception(f"Variable no declarada: {key}")

    def get_value(self, key):
        if key in self.memory:
            if "value" not in self.memory[key]:
                if self.t != "function":
                    raise Exception(f"Variable no inicializada: {key}")
                else:
                    return self.memory[key]["type"]()
            return self.memory[key]["value"]
        elif self.parent is not None:
            return self.parent.get_value(key)
        else:
            raise Exception(f"Variable no declarada: {key}")

    def set(self, key, value, is_declaration=False):
        if is_declaration:
            try:
                existing_value = self.get(key)
                if existing_value is not None:
                    raise Exception(f"Variable ya declarada: {key}")
            except Exception:
                pass
            finally:
                self.memory[key] = value

        if key in self.memory:
            if self.memory[key]["type"] != value["type"]:
                if self.memory[key]["type"] == type(None):
                    self.memory[key]["type"] = value["type"]
                else:
                    raise Exception(
                        f"Tipo de dato incorrecto: {key}. Se esperaba {self.memory[key]['type']} y se recibio {value['type']}")
            self.memory[key] = value
        elif self.parent is not None:
            self.parent.set(key, value)
        else:
            raise Exception(f"Variable no declarada: {key}")


class MyVisitor(lenguajeVisitor):
    def __init__(self):

        self.current_context = Context()

    def visitPrint(self, ctx: lenguajeParser.PrintContext):
        value = self.visitExpresion(ctx.expresion())
        print(f'print from built-in function:\n\t"{value}"')

    def visitLinearRegression(self, ctx: lenguajeParser.LinearRegressionContext):
        value = self.visitExpresion(ctx.expresion())
        print(value)

    def visitBloque(self, ctx: lenguajeParser.BloqueContext):
        if isinstance(ctx.parentCtx, lenguajeParser.DeclaracionFuncionContext):
            return self.visitChildren(ctx)
        self.current_context = Context(self.current_context)
        self.visitChildren(ctx)
        self.current_context = self.current_context.parent

    def visitDeclaracionVariable(self, ctx: lenguajeParser.DeclaracionVariableContext):
        identificador, valor, tipo = None, None, {}
        for children in ctx.getChildren():
            if isinstance(children, lenguajeParser.IdentificadorContext):
                identificador = self.visitIdentificador(children)
            elif isinstance(children, lenguajeParser.TipoContext):
                tipo = self.visitTipo(children)
            elif isinstance(children, lenguajeParser.ExpresionContext):
                tipo["value"] = self.visitExpresion(children)
            elif isinstance(children, lenguajeParser.ExpresionArrayContext):
                tipo["value"] = self.visitExpresionArray(children)
        if "type" not in tipo or tipo["type"] == type(None):
            tipo["type"] = type(valor)
        self.current_context.set(identificador, tipo, True)
        return self.visitChildren(ctx)

    def visitDeclaracionFuncion(self, ctx: lenguajeParser.DeclaracionFuncionContext):
        identificador, parametros = None, {}
        for children in ctx.getChildren():
            if isinstance(children, lenguajeParser.IdentificadorContext):
                identificador = self.visitIdentificador(children)
            elif isinstance(children, lenguajeParser.ListaParametrosContext):
                parametros = self.visitListaParametros(children)
        self.current_context.set(identificador, {"type": "func"}, True)
        self.current_context = Context(self.current_context, t="function")

        for key in parametros:
            self.current_context.set(key, parametros[key], True)
        self.visitChildren(ctx)
        self.current_context = self.current_context.parent

    def visitListaParametros(self, ctx: lenguajeParser.ListaParametrosContext):
        parametros = {}
        for children in ctx.getChildren():
            if isinstance(children, lenguajeParser.ParametroContext):
                parametros[children.identificador().getText()] = self.visitTipo(children.tipo())
        return parametros

    def visitAsignacion(self, ctx: lenguajeParser.AsignacionContext):
        identificador, valor = None, None
        for children in ctx.getChildren():
            if isinstance(children, lenguajeParser.IdentificadorContext):
                identificador = self.visitIdentificador(children)
            elif isinstance(children, lenguajeParser.ExpresionContext):
                valor = self.visitExpresion(children)
        self.current_context.set(identificador, {"type": type(valor), "value": valor})
        ##return self.visitChildren(ctx)

    def visitExpresion(self, ctx: lenguajeParser.ExpresionContext):
        if len(ctx.children) == 1:
            return self.visitChildren(ctx)
        operation = ""
        for children in ctx.getChildren():
            if isinstance(children, lenguajeParser.TerminoContext):
                value = self.visit(children)
                operation += str(value)
            elif isinstance(children, lenguajeParser.OperadorAritmeticoContext):
                operation += self.visitOperadorAritmetico(children)
            elif isinstance(children, lenguajeParser.ExpresionContext):
                operation += self.visitExpresion(children)
        return eval(operation)

    def visitOperadorAritmetico(self, ctx: lenguajeParser.OperadorAritmeticoContext):
        return ctx.getText()

    def visitTermino(self, ctx: lenguajeParser.TerminoContext):
        for children in ctx.getChildren():
            if isinstance(children, lenguajeParser.IdentificadorContext):
                key = children.getText()
                return self.current_context.get_value(key)
            elif isinstance(children, TerminalNodeImpl):
                return children.getText()
            else:
                return self.visitChildren(ctx)

    def visitIdentificador(self, ctx: lenguajeParser.IdentificadorContext):
        return ctx.getText()

    def visitBooleanos(self, ctx: lenguajeParser.BooleanosContext):
        return ctx.getText() == "true"

    def visitTipo(self, ctx: lenguajeParser.TipoContext):

        for arrays in ctx.getChildren(lambda x: isinstance(x, lenguajeParser.ArrayContext)):
            return {"type": "array", "subtype": self.visitArray(arrays)}
        type_string = ctx.getText()
        if type_string == "int":
            return {"type": type(int())}
        elif type_string == "float":
            return {"type": type(float())}
        elif type_string == "string":
            return {"type": type(str())}
        elif type_string == "bool":
            return {"type": type(bool())}
        else:
            return {"type": type(None)}

    def visitArray(self, ctx: lenguajeParser.ArrayContext):
        dim = []
        for children in ctx.getChildren():
            if isinstance(children, lenguajeParser.TipoContext):
                typo = self.visitTipo(children)
                if "type" in typo:
                    if "size" in typo:
                        for x in typo["size"]:
                            dim.append(x)
                        typo["size"] = dim
                    else:
                        typo["size"] = dim
                    return typo

            elif isinstance(children, lenguajeParser.ExpresionContext):
                dim.append(self.visitExpresion(children))

    def visitExpresionArray(self, ctx: lenguajeParser.ExpresionArrayContext):
        expression = ""
        for children in ctx.getChildren():
            if isinstance(children, lenguajeParser.ExpresionContext):
                expression += str(self.visitExpresion(children))
            elif isinstance(children, TerminalNodeImpl):
                expression += children.getText()
        return eval(expression.replace("{", "[").replace("}", "]"))

    def visitEntero(self, ctx: lenguajeParser.EnteroContext):
        return int(ctx.getText())

    def visitDecimal(self, ctx: lenguajeParser.DecimalContext):
        return float(ctx.getText())


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = lenguajeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = lenguajeParser(token_stream)
    tree = parser.programa()
    visitor = MyVisitor()
    visitor.visit(tree)
