import sys

from antlr4 import *
from antlr4.InputStream import InputStream

from generatedcode.lenguajeLexer import lenguajeLexer
from generatedcode.lenguajeParser import lenguajeParser
from generatedcode.lenguajeVisitor import lenguajeVisitor
from antlr4.tree.Tree import TerminalNodeImpl


class Context:

    def __init__(self, parent=None):
        self.parent = parent
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
            if self.memory[key]["typo"] != value["typo"]:
                raise Exception(
                    f"Tipo de dato incorrecto: {key}. Se esperaba {self.memory[key]['typo']} y se recibio {value['typo']}")
            self.memory[key] = value
        elif self.parent is not None:
            self.parent.set(key, value)
        else:
            raise Exception(f"Variable no declarada: {key}")


class MyVisitor(lenguajeVisitor):
    def __init__(self):

        self.current_context = Context()

    def visitBloque(self, ctx: lenguajeParser.BloqueContext):
        self.current_context = Context(self.current_context)
        self.visitChildren(ctx)
        self.current_context = self.current_context.parent

    def visitDeclaracionVariable(self, ctx: lenguajeParser.DeclaracionVariableContext):
        global identificador, valor, tipo
        for children in ctx.getChildren():
            if isinstance(children, lenguajeParser.IdentificadorContext):
                identificador = self.visitIdentificador(children)
            elif isinstance(children, lenguajeParser.TipoContext):
                tipo = self.visitTipo(children)
            elif isinstance(children, lenguajeParser.ExpresionContext):
                valor = self.visitChildren(children)
        if tipo == type(None):
            tipo = type(valor)
        self.current_context.set(identificador, {"typo": tipo, "valor": valor}, True)
        return self.visitChildren(ctx)

    def visitDeclaracionFuncion(self, ctx: lenguajeParser.DeclaracionFuncionContext):
        global identificador, parametros
        for children in ctx.getChildren():
            if isinstance(children, lenguajeParser.IdentificadorContext):
                identificador = self.visitIdentificador(children)
            elif isinstance(children, lenguajeParser.ListaParametrosContext):
                parametros = self.visitListaParametros(children)
        self.current_context.set(identificador, {"typo": "func"}, True)
        self.current_context = Context(self.current_context)

        for key in parametros:
            self.current_context.set(key, parametros[key], True)
        self.visitChildren(ctx)
        self.current_context = self.current_context.parent

    def visitListaParametros(self, ctx: lenguajeParser.ListaParametrosContext):
        parametros = {}
        for children in ctx.getChildren():
            if isinstance(children, lenguajeParser.ParametroContext):
                parametros[children.identificador().getText()] = {"typo": self.visitTipo(children.tipo())}
        return parametros

    def visitAsignacion(self, ctx: lenguajeParser.AsignacionContext):
        global identificador, valor
        for children in ctx.getChildren():
            if isinstance(children, lenguajeParser.IdentificadorContext):
                identificador = self.visitIdentificador(children)
            elif isinstance(children, lenguajeParser.ExpresionContext):
                valor = self.visitChildren(children)
        self.current_context.set(identificador, {"typo": type(valor), "valor": valor})
        return self.visitChildren(ctx)

    def visitExpresion(self, ctx: lenguajeParser.ExpresionContext):
        for children in ctx.getChildren():
            if isinstance(children, lenguajeParser.TerminoContext):
                return self.visitChildren(children)

    def visitTermino(self, ctx: lenguajeParser.TerminoContext):
        for children in ctx.getChildren():
            if isinstance(children, lenguajeParser.IdentificadorContext) and len(ctx.children) >= 1:
                print(children)
            elif isinstance(children, TerminalNodeImpl) and len(ctx.children) == 1:
                return children.getText()
            else:
                return self.visitChildren(ctx)

    def visitIdentificador(self, ctx: lenguajeParser.IdentificadorContext):
        return ctx.getText()

    def visitTipo(self, ctx: lenguajeParser.TipoContext):
        type_string = ctx.getText()
        if type_string == "int":
            return type(int())
        elif type_string == "float":
            return type(float())
        elif type_string == "string":
            return type(str())
        elif type_string == "bool":
            return type(bool())
        else:
            return type(None)

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
