from enum import Enum, auto

class TokenType(Enum):
    KEYWORD = auto()
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING = auto()
    OPERATOR = auto()
    EOF = auto()
    PUNCTUATION = auto()

    
class Token():
    def __init__(self, token_type, value, line):
        self.token_type = token_type
        self.value = value
        self.line = line
token = Token(TokenType.KEYWORD, "var", 1)
Token(TokenType.KEYWORD, "var", 1)   
