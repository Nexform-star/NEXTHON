from .lexer import Lexer
from .tokens import TokenType
from .errors import ParserError
from .ast import VariableDeclaration, PrintStatement, Program, PrintText, BinaryOperation, IfStatement, Block

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.token_type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise ParserError(
                f"Expected {token_type.name}, got {self.current_token.token_type.name} at line {self.current_token.line}"
            )

    def parse_variable_declaration(self):
        self.eat(TokenType.KEYWORD)
        variable_name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.OPERATOR)

        if self.current_token.token_type == TokenType.STRING:
            variable_value = self.current_token.value
            self.eat(TokenType.STRING)
        else:
            variable_value = self.parse_expression()

        return VariableDeclaration(variable_name, variable_value)

    def parse_print_statement(self):
        self.eat(TokenType.KEYWORD)
        self.eat(TokenType.PUNCTUATION)

        if self.current_token.token_type == TokenType.STRING:
            value = self.current_token.value
            self.eat(TokenType.STRING)
            statement = PrintText(value)
        else:
            value = self.parse_expression()
            statement = PrintStatement(value)

        self.eat(TokenType.PUNCTUATION)
        return statement

    def parse_program(self):
        statements = []
        while self.current_token.token_type != TokenType.EOF:
            if self.current_token.value == "var":
                statement = self.parse_variable_declaration()
            elif self.current_token.value == "print":
                statement = self.parse_print_statement()
            elif self.current_token.value == "if":
                statement = self.parse_if_statement()
            else:
                raise ParserError(
                    f"Unexpected token '{self.current_token.value}' at line {self.current_token.line}"
                )
            statements.append(statement)
        return Program(statements)

    def parse_factor(self):
        if self.current_token.value == "(":
            self.eat(TokenType.PUNCTUATION)
            value = self.parse_expression()
            self.eat(TokenType.PUNCTUATION)
            return value

        elif self.current_token.token_type == TokenType.NUMBER:
            value = self.current_token.value
            self.eat(TokenType.NUMBER)
            return float(value) if "." in value else int(value)

        elif self.current_token.token_type == TokenType.IDENTIFIER:
            value = self.current_token.value
            self.eat(TokenType.IDENTIFIER)
            return value

        raise ParserError("Expected a number, variable or expression")

    def parse_term(self):
        left = self.parse_factor()

        while self.current_token.value in ("*", "/"):
            operator = self.current_token.value
            self.eat(TokenType.OPERATOR)
            right = self.parse_factor()
            left = BinaryOperation(left, operator, right)

        return left

    def parse_arithmetic_expression(self):
        left = self.parse_term()

        while self.current_token.value in ("+", "-"):
            operator = self.current_token.value
            self.eat(TokenType.OPERATOR)
            right = self.parse_term()
            left = BinaryOperation(left, operator, right)

        return left

    def parse_expression(self):
        left = self.parse_arithmetic_expression()

        while self.current_token.value in ("==", "!=", "<", ">", "<=", ">="):
            operator = self.current_token.value
            self.eat(TokenType.OPERATOR)
            right = self.parse_arithmetic_expression()
            left = BinaryOperation(left, operator, right)

        return left

    def parse_block(self):
        self.eat(TokenType.PUNCTUATION)
        statements = []

        while self.current_token.value != "}":
            if self.current_token.value == "print":
                statements.append(self.parse_print_statement())
            elif self.current_token.value == "var":
                statements.append(self.parse_variable_declaration())
            else:
                raise ParserError(f"Unexpected token '{self.current_token.value}'")

        self.eat(TokenType.PUNCTUATION)
        return Block(statements)

    def parse_if_statement(self):
        self.eat(TokenType.KEYWORD)
        condition = self.parse_expression()
        body = self.parse_block()

        else_body = None
        if self.current_token.value == "else":
            self.eat(TokenType.KEYWORD)
            else_body = self.parse_block()

        return IfStatement(condition, body, else_body)