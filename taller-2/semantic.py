import sys

from antlr4 import *
from antlr4.InputStream import InputStream

from generatedcode.lenguajeLexer import lenguajeLexer
from generatedcode.lenguajeParser import lenguajeParser
from generatedcode.lenguajeVisitor import lenguajeVisitor


class MyVisitor(lenguajeVisitor):
    def __init__(self):
        self.memory = {}

    def visitDeclaracionVariable(self, ctx: lenguajeParser.DeclaracionVariableContext):
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

    def visitExpresion(self, ctx:lenguajeParser.ExpresionContext):
        return self.visitChildren(ctx)

    def visitTermino(self, ctx:lenguajeParser.TerminoContext):
        return self.visitChildren(ctx)

    def visitFactor(self, ctx:lenguajeParser.FactorContext):

        return self.visitChildren(ctx)


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