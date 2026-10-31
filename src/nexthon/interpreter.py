from .errors import RuntimeError
from .ast import VariableDeclaration, PrintStatement, PrintText, BinaryOperation, IfStatement

class Interpreter:
    def __init__(self):
        self.variables = {}

    def evaluate(self, expression):
        if isinstance(expression, BinaryOperation):
            left = self.evaluate(expression.left)
            right = self.evaluate(expression.right)

            if expression.operator == "+":
                return left + right
            elif expression.operator == "-":
                return left - right
            elif expression.operator == "*":
                return left * right
            elif expression.operator == "/":
                return left / right
            elif expression.operator == "==":
                return left == right
            elif expression.operator == "!=":
                return left != right
            elif expression.operator == "<":
                return left < right
            elif expression.operator == ">":
                return left > right
            elif expression.operator == "<=":
                return left <= right
            elif expression.operator == ">=":
                return left >= right

        elif isinstance(expression, str):
            if expression not in self.variables:
                raise RuntimeError(f"Undefined variable '{expression}'")
            return self.variables[expression]

        return expression

    def interpret(self, program):
        for statement in program.statements:
            if isinstance(statement, VariableDeclaration):
                value = self.evaluate(statement.value)
                self.variables[statement.name] = value

            elif isinstance(statement, PrintText):
                print(statement.value)

            elif isinstance(statement, PrintStatement):
                print(self.evaluate(statement.value))
            elif isinstance(statement, IfStatement):
                if self.evaluate(statement.condition):
                    self.interpret(statement.body)
                elif statement.else_body is not None:
                    self.interpret(statement.else_body)


