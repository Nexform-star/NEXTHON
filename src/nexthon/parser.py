from .lexer import Lexer
from .tokens import TokenType
from .errors import ParserError

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
        variable_value = self.current_token.value
        self.eat(TokenType.STRING)
        return variable_name, variable_value

lexer = Lexer('var username = "Nexform"')
parser = Parser(lexer)

result = parser.parse_variable_declaration()
print(result)