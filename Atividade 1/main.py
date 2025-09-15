from antlr4 import *
from ArithmeticLexer import ArithmeticLexer
from ArithmeticParser import ArithmeticParser

class ArithmeticVisitor:

    def __init__(self):
        self.variables = {}

    def visit(self, ctx):
        if isinstance(ctx, ArithmeticParser.ExprContext):
            return self.visitExpr(ctx)
        elif isinstance(ctx, ArithmeticParser.TermContext):
            return self.visitTerm(ctx)
        elif isinstance(ctx, ArithmeticParser.FactorContext):
            return self.visitFactor(ctx)
        elif isinstance(ctx, ArithmeticParser.ProgramContext):
            return self.visitProgram(ctx)
        elif isinstance(ctx, ArithmeticParser.StatementContext):
            return self.visitStatement(ctx)
        elif isinstance(ctx, ArithmeticParser.AssignmentContext):
            return self.visitAssignment(ctx)
        elif isinstance(ctx, ArithmeticParser.BaseContext):
            return self.visitBase(ctx)

    def visitExpr(self, ctx):
        result = self.visit(ctx.term(0))
        for i in range(1, len(ctx.term())):
            if ctx.getChild(i * 2 - 1).getText() == '+':
                result += self.visit(ctx.term(i))
            else:
                result -= self.visit(ctx.term(i))
        return result

    def visitTerm(self, ctx):
        result = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(i * 2 - 1).getText()
            if op == '*':
                result *= self.visit(ctx.factor(i))
            elif op == '/':
                result /= self.visit(ctx.factor(i))
            elif op == '%':
                result %= self.visit(ctx.factor(i))
        return result

    def visitFactor(self, ctx):
        left = self.visit(ctx.base())
        if ctx.POW():
            right = self.visit(ctx.factor())
            return left ** right
        return left

    def visitBase(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.VAR():
            var_name = ctx.VAR().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                raise Exception(f"Variável '{var_name}' não definida.")
        elif ctx.expr():
            return self.visit(ctx.expr())

    def visitProgram(self, ctx):
        results = []
        for statement in ctx.statement():
            results.append(self.visit(statement))
        return results

    def visitStatement(self, ctx):
        if ctx.assignment():
            return self.visit(ctx.assignment())
        else:
            return self.visit(ctx.expr())

    def visitAssignment(self, ctx):
        var_name = ctx.VAR().getText()
        value = self.visit(ctx.expr())
        self.variables[var_name] = value
        return f"{var_name} = {value}"

def main():
    visitor = ArithmeticVisitor()
    while True:
        try:
            expression = input("Digite uma expressão aritmética: ")
            lexer = ArithmeticLexer(InputStream(expression))
            stream = CommonTokenStream(lexer)
            parser = ArithmeticParser(stream)
            tree = parser.program()
            results = visitor.visit(tree)
            for r in results:
                if r is not None:
                    print("Resultado:", r)

        except Exception as e:
            print(f"Erro: {e}")

if __name__ == '__main__':
    main()