class Program:
    def __init__(self, statements):
        self.statements = statements


class Block:
    def __init__(self, statements):
        self.statements = statements


class VariableDeclaration:
    def __init__(self, name, value, line):
        self.name = name
        self.value = value
        self.line = line


class Assignment:
    def __init__(self, name, value, line):
        self.name = name
        self.value = value
        self.line = line


class PrintStatement:
    def __init__(self, value, line):
        self.value = value
        self.line = line


class PrintText:
    def __init__(self, value):
        self.value = value


class StringLiteral:
    def __init__(self, value):
        self.value = value


class ListLiteral:
    def __init__(self, elements):
        self.elements = elements


class TupleLiteral:
    def __init__(self, elements):
        self.elements = elements


class DictLiteral:
    def __init__(self, entries):
        self.entries = entries


class IndexAccess:
    def __init__(self, collection, index):
        self.collection = collection
        self.index = index


class IndexAssignment:
    def __init__(self, collection, index, value, line):
        self.collection = collection
        self.name = collection if isinstance(collection, str) else None
        self.index = index
        self.value = value
        self.line = line


class AttributeAccess:
    def __init__(self, object, name):
        self.object = object
        self.name = name


class MethodCall:
    def __init__(self, object, name, arguments):
        self.object = object
        self.name = name
        self.arguments = arguments


class FunctionCall:
    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments


class BinaryOperation:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


class UnaryOperation:
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand


class IfStatement:
    def __init__(self, condition, body, else_body=None):
        self.condition = condition
        self.body = body
        self.else_body = else_body


class WhileStatement:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class ForStatement:
    def __init__(self, variable, iterable, body, line):
        self.variable = variable
        self.iterable = iterable
        self.body = body
        self.line = line


class BreakStatement:
    def __init__(self, line):
        self.line = line


class ContinueStatement:
    def __init__(self, line):
        self.line = line


class FunctionDeclaration:
    def __init__(self, name, parameters, body):
        self.name = name
        self.parameters = parameters
        self.body = body


class ReturnStatement:
    def __init__(self, value, line):
        self.value = value
        self.line = line


class ImportStatement:
    def __init__(self, module, alias, line):
        self.module = module
        self.alias = alias
        self.line = line


class TryStatement:
    def __init__(self, body, exception_name, except_body, finally_body=None):
        self.body = body
        self.exception_name = exception_name
        self.except_body = except_body
        self.finally_body = finally_body


class RaiseStatement:
    def __init__(self, value, line):
        self.value = value
        self.line = line