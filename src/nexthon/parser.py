from .tokens import TokenType
from .errors import ParserError
from .ast import (
    Program,
    Block,
    VariableDeclaration,
    Assignment,
    PrintStatement,
    StringLiteral,
    ListLiteral,
    TupleLiteral,
    DictLiteral,
    IndexAccess,
    IndexAssignment,
    AttributeAccess,
    MethodCall,
    FunctionCall,
    BinaryOperation,
    UnaryOperation,
    IfStatement,
    WhileStatement,
    ForStatement,
    BreakStatement,
    ContinueStatement,
    FunctionDeclaration,
    ReturnStatement,
    ImportStatement,
    TryStatement,
    RaiseStatement,
)


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens = lexer.tokenize()
        self.position = 0
        self.current_token = self.tokens[0]

    def peek(self, offset=1):
        index = self.position + offset

        if index >= len(self.tokens):
            return self.tokens[-1]

        return self.tokens[index]

    def advance(self):
        if self.current_token.token_type != TokenType.EOF:
            self.position += 1
            self.current_token = self.tokens[self.position]

    def eat(self, token_type, value=None):
        token = self.current_token

        if token.token_type != token_type:
            raise ParserError(
                f"Expected {token_type.name}, got "
                f"{token.token_type.name} at line {token.line}"
            )

        if value is not None and token.value != value:
            raise ParserError(
                f"Expected '{value}', got '{token.value}' "
                f"at line {token.line}"
            )

        self.advance()
        return token

    def match(self, value):
        return self.current_token.value == value

    def eat_value(self, value):
        if not self.match(value):
            raise ParserError(
                f"Expected '{value}', got "
                f"'{self.current_token.value}' "
                f"at line {self.current_token.line}"
            )

        self.advance()

    def skip_semicolons(self):
        while self.match(";"):
            self.advance()

    def parse_program(self):
        statements = []

        while self.current_token.token_type != TokenType.EOF:
            self.skip_semicolons()

            if self.current_token.token_type == TokenType.EOF:
                break

            statements.append(self.parse_statement())

        return Program(statements)

    def parse_statement(self):
        value = self.current_token.value

        if value == "var":
            return self.parse_variable_declaration()

        if value == "const":
            return self.parse_variable_declaration(constant=True)

        if value == "print":
            return self.parse_print_statement()

        if value == "if":
            return self.parse_if_statement()

        if value == "while":
            return self.parse_while_statement()

        if value == "for":
            return self.parse_for_statement()

        if value == "function":
            return self.parse_function_declaration()

        if value == "return":
            return self.parse_return_statement()

        if value == "break":
            line = self.current_token.line
            self.advance()
            return BreakStatement(line)

        if value == "continue":
            line = self.current_token.line
            self.advance()
            return ContinueStatement(line)

        if value == "import":
            return self.parse_import_statement()

        if value == "try":
            return self.parse_try_statement()

        if value == "raise":
            return self.parse_raise_statement()

        if self.current_token.token_type == TokenType.IDENTIFIER:
            return self.parse_expression_statement()

        raise ParserError(
            f"Unexpected token '{value}' "
            f"at line {self.current_token.line}"
        )

    def parse_variable_declaration(self, constant=False):
        line = self.current_token.line
        self.advance()

        name = self.eat(TokenType.IDENTIFIER).value
        self.eat(TokenType.OPERATOR, "=")

        value = self.parse_expression()

        statement = VariableDeclaration(name, value, line)
        statement.constant = constant

        return statement

    def parse_print_statement(self):
        line = self.current_token.line
        self.advance()

        self.eat_value("(")
        value = self.parse_expression()
        self.eat_value(")")

        return PrintStatement(value, line)

    def parse_assignment_operator(self, target, line):
        operator = self.current_token.value
        self.advance()

        value = self.parse_expression()

        if operator != "=":
            binary_operator = operator[:-1]
            value = BinaryOperation(
                target,
                binary_operator,
                value
            )

        if isinstance(target, str):
            return Assignment(target, value, line)

        if isinstance(target, IndexAccess):
            return IndexAssignment(
                target.collection,
                target.index,
                value,
                line
            )

        raise ParserError(
            f"Invalid assignment target at line {line}"
        )

    def parse_expression_statement(self):
        line = self.current_token.line
        expression = self.parse_identifier()
        expression = self.parse_postfix(expression)

        if self.current_token.token_type == TokenType.OPERATOR:
            if self.current_token.value in (
                "=",
                "+=",
                "-=",
                "*=",
                "/=",
                "%=",
                "**=",
                "//=",
            ):
                return self.parse_assignment_operator(
                    expression,
                    line
                )

        if isinstance(expression, (FunctionCall, MethodCall)):
            return expression

        raise ParserError(
            f"Invalid expression statement at line {line}"
        )

    def parse_function_declaration(self):
        self.advance()

        name = self.eat(TokenType.IDENTIFIER).value

        self.eat_value("(")

        parameters = []

        while not self.match(")"):
            if self.current_token.token_type != TokenType.IDENTIFIER:
                raise ParserError(
                    f"Expected parameter name at line "
                    f"{self.current_token.line}"
                )

            parameters.append(self.current_token.value)
            self.advance()

            if self.match(","):
                self.advance()
            elif not self.match(")"):
                raise ParserError(
                    f"Expected ',' or ')' at line "
                    f"{self.current_token.line}"
                )

        self.eat_value(")")

        body = self.parse_block()

        return FunctionDeclaration(name, parameters, body)

    def parse_return_statement(self):
        line = self.current_token.line
        self.advance()

        if self.match("}") or self.match(";"):
            return ReturnStatement(None, line)

        if self.current_token.token_type == TokenType.EOF:
            return ReturnStatement(None, line)

        value = self.parse_expression()

        return ReturnStatement(value, line)

    def parse_block(self):
        self.eat_value("{")

        statements = []

        while (
            not self.match("}")
            and self.current_token.token_type != TokenType.EOF
        ):
            self.skip_semicolons()

            if self.match("}"):
                break

            statements.append(self.parse_statement())

        if not self.match("}"):
            raise ParserError(
                f"Expected '}}' at line {self.current_token.line}"
            )

        self.advance()

        return Block(statements)

    def parse_if_statement(self):
        self.advance()

        condition = self.parse_expression()
        body = self.parse_block()

        else_body = None

        if self.match("elif"):
            else_body = Block([self.parse_elif_statement()])

        elif self.match("else"):
            self.advance()
            else_body = self.parse_block()

        return IfStatement(condition, body, else_body)

    def parse_elif_statement(self):
        self.eat_value("elif")

        condition = self.parse_expression()
        body = self.parse_block()

        else_body = None

        if self.match("elif"):
            else_body = Block([self.parse_elif_statement()])

        elif self.match("else"):
            self.advance()
            else_body = self.parse_block()

        return IfStatement(condition, body, else_body)

    def parse_while_statement(self):
        self.advance()

        condition = self.parse_expression()
        body = self.parse_block()

        return WhileStatement(condition, body)

    def parse_for_statement(self):
        line = self.current_token.line
        self.advance()

        variable = self.eat(TokenType.IDENTIFIER).value
        self.eat_value("in")

        iterable = self.parse_expression()
        body = self.parse_block()

        return ForStatement(variable, iterable, body, line)

    def parse_import_statement(self):
        line = self.current_token.line
        self.advance()

        module = self.current_token.value

        if self.current_token.token_type not in (
            TokenType.IDENTIFIER,
            TokenType.STRING,
        ):
            raise ParserError(
                f"Expected module name at line {line}"
            )

        self.advance()

        alias = None

        if self.match("as"):
            self.advance()
            alias = self.eat(TokenType.IDENTIFIER).value

        return ImportStatement(module, alias, line)

    def parse_try_statement(self):
        self.advance()

        body = self.parse_block()

        if not self.match("except"):
            raise ParserError(
                f"Expected 'except' at line "
                f"{self.current_token.line}"
            )

        self.advance()

        exception_name = None

        if self.current_token.token_type == TokenType.IDENTIFIER:
            exception_name = self.current_token.value
            self.advance()

        except_body = self.parse_block()

        finally_body = None

        if self.match("finally"):
            self.advance()
            finally_body = self.parse_block()

        return TryStatement(
            body,
            exception_name,
            except_body,
            finally_body
        )

    def parse_raise_statement(self):
        line = self.current_token.line
        self.advance()

        value = self.parse_expression()

        return RaiseStatement(value, line)

    def parse_identifier(self):
        name = self.eat(TokenType.IDENTIFIER).value

        if self.match("("):
            return self.parse_function_call(name)

        return name

    def parse_function_call(self, name):
        self.eat_value("(")
        arguments = self.parse_arguments()
        self.eat_value(")")

        return FunctionCall(name, arguments)

    def parse_arguments(self):
        arguments = []

        if self.match(")"):
            return arguments

        while True:
            arguments.append(self.parse_expression())

            if not self.match(","):
                break

            self.advance()

        return arguments

    def parse_postfix(self, expression):
        while True:
            if self.match("["):
                self.advance()

                index = self.parse_expression()

                self.eat_value("]")

                expression = IndexAccess(expression, index)

            elif self.match("."):
                self.advance()

                name = self.eat(TokenType.IDENTIFIER).value

                if self.match("("):
                    self.advance()
                    arguments = self.parse_arguments()
                    self.eat_value(")")

                    expression = MethodCall(
                        expression,
                        name,
                        arguments
                    )
                else:
                    expression = AttributeAccess(
                        expression,
                        name
                    )

            else:
                break

        return expression

    def parse_list_literal(self):
        self.eat_value("[")

        elements = []

        if self.match("]"):
            self.advance()
            return ListLiteral(elements)

        while True:
            elements.append(self.parse_expression())

            if not self.match(","):
                break

            self.advance()

            if self.match("]"):
                break

        self.eat_value("]")

        return ListLiteral(elements)

    def parse_tuple_literal(self):
        self.eat_value("(")

        elements = []

        if self.match(")"):
            self.advance()
            return TupleLiteral(elements)

        first = self.parse_expression()

        if not self.match(","):
            self.eat_value(")")
            return first

        elements.append(first)

        while self.match(","):
            self.advance()

            if self.match(")"):
                break

            elements.append(self.parse_expression())

        self.eat_value(")")

        return TupleLiteral(elements)

    def parse_dict_literal(self):
        self.eat_value("{")

        entries = []

        if self.match("}"):
            self.advance()
            return DictLiteral(entries)

        while True:
            key = self.parse_expression()
            self.eat_value(":")
            value = self.parse_expression()

            entries.append((key, value))

            if not self.match(","):
                break

            self.advance()

            if self.match("}"):
                break

        self.eat_value("}")

        return DictLiteral(entries)

    def parse_factor(self):
        token = self.current_token
        value = token.value
        if self.current_token.token_type == TokenType.STRING:
            self.advance()
            return StringLiteral(value)

        if value in ("-", "+", "not"):
            self.advance()
            operand = self.parse_factor()
            return UnaryOperation(value, operand)

        if self.current_token.token_type == TokenType.NUMBER:
            self.advance()

            if "." in value:
                return float(value)

            return int(value)

        if value == "true":
            self.advance()
            return True

        if value == "false":
            self.advance()
            return False

        if value == "null":
            self.advance()
            return None

        if value == "(":
            return self.parse_tuple_literal()

        if value == "[":
            return self.parse_list_literal()

        if value == "{":
            return self.parse_dict_literal()

        if self.current_token.token_type == TokenType.IDENTIFIER:
            expression = self.parse_identifier()
            return self.parse_postfix(expression)

        raise ParserError(
            f"Expected expression at line {token.line}"
        )

    def parse_power(self):
        left = self.parse_factor()

        if self.match("**"):
            operator = self.current_token.value
            self.advance()

            right = self.parse_power()

            return BinaryOperation(left, operator, right)

        return left

    def parse_term(self):
        left = self.parse_power()

        while self.current_token.value in (
            "*",
            "/",
            "%",
            "//",
        ):
            operator = self.current_token.value
            self.advance()

            right = self.parse_power()

            left = BinaryOperation(left, operator, right)

        return left

    def parse_arithmetic_expression(self):
        left = self.parse_term()

        while self.current_token.value in ("+", "-"):
            operator = self.current_token.value
            self.advance()

            right = self.parse_term()

            left = BinaryOperation(left, operator, right)

        return left

    def parse_comparison(self):
        left = self.parse_arithmetic_expression()

        while self.current_token.value in (
            "==",
            "!=",
            "<",
            ">",
            "<=",
            ">=",
            "in",
        ):
            operator = self.current_token.value
            self.advance()

            right = self.parse_arithmetic_expression()

            left = BinaryOperation(left, operator, right)

        return left

    def parse_and(self):
        left = self.parse_comparison()

        while self.match("and"):
            operator = self.current_token.value
            self.advance()

            right = self.parse_comparison()

            left = BinaryOperation(left, operator, right)

        return left

    def parse_expression(self):
        left = self.parse_and()

        while self.match("or"):
            operator = self.current_token.value
            self.advance()

            right = self.parse_and()

            left = BinaryOperation(left, operator, right)

        return left
