from enum import Enum, auto


class TokenType(Enum):
    KEYWORD = auto()
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING = auto()
    OPERATOR = auto()
    PUNCTUATION = auto()
    EOF = auto()


class Token:
    def __init__(self, token_type, value, line, column=None):
        self.token_type = token_type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return (
            f"Token({self.token_type.name}, "
            f"{self.value!r}, line={self.line})"
        )