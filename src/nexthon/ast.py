class VariableDeclaration:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class PrintStatement:
    def __init__(self, value):
        self.value = value

class Program:
    def __init__(self, statements):
        self.statements = statements

class PrintText:
    def __init__(self, value):
        self.value = value

class BinaryOperation:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class IfStatement:
    def __init__(self, condition, body, else_body):
        self.condition = condition
        self.body = body
        self.else_body = else_body


class Block:
    def __init__(self, statements):
        self.statements = statements