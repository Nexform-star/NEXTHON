from .tokens import Token, TokenType
from .errors import LexicalError

KEYWORDS = ["var", "print", "if", "else", "while"]
OPERATORS = ["=", "+", "-", "*", "/", "<", ">", "==", "!=", "<=", ">="]
PUNCTUATION = ["(", ")", "{", "}", ",", ";"]

class Lexer:
    def __init__(self, source):
        self.position = 0
        self.source = source
        self.line = 1

    def current_char(self):
        if self.position < len(self.source):
            return self.source[self.position]
        else:
            return None
        
    def advance(self):
        self.position += 1
        return self.current_char()

    def skip_whitespace(self):
        character = self.current_char()
        while character is not None and character.isspace():
            if character == "\n":
                self.line += 1    
            self.position += 1
            character = self.current_char()
        else :
            return self.current_char()
            
    def read_number(self):
        number = ""
        dot_count = 0
        character = self.current_char()
        while character is not None and (character.isdigit() or character == "."):
            if character == ".":
                dot_count += 1
                if dot_count > 1:
                    raise LexicalError(f"Invalid number at line {self.line}")
            number = number + self.current_char()
            self.advance()
            character = self.current_char()
        return Token(TokenType.NUMBER, number, self.line)



    def read_identifier(self):
        character = self.current_char()
        name = ""
        while character is not None and (character.isalnum() or character == "_"):
            name = name + character
            self.advance()
            character = self.current_char()
        if name in KEYWORDS:
            token_type = TokenType.KEYWORD
        else:
            token_type = TokenType.IDENTIFIER
        return Token(token_type, name, self.line)

    def get_next_token(self):
        self.skip_whitespace()
        character = self.current_char()
        if character is None:
            return Token(TokenType.EOF, "", self.line)
        if character.isdigit():
            return self.read_number()
        if character.isalnum() or character == "_":
            return self.read_identifier()
        if self.source[self.position:self.position + 2] in ("==", "!=", "<=", ">="):
            operator = self.source[self.position:self.position + 2]
            self.advance()
            self.advance()
            return Token(TokenType.OPERATOR, operator, self.line)
        if character == "!":
            self.skip_comment()
            return self.get_next_token()
        if character in OPERATORS:
            self.advance()
            return Token(TokenType.OPERATOR, character, self.line)
        if character in PUNCTUATION:
            self.advance()
            return Token(TokenType.PUNCTUATION, character, self.line)
        if character == '"':
            return self.read_string()
        else:
            raise LexicalError(f"Unknown character '{character}' at line {self.line}")

    def read_string(self):
        string = ""
        self.advance()  
        character = self.current_char()
        while character is not None and character != '"':
            string = string + character
            self.advance()
            character = self.current_char()
        if character is None:
            raise LexicalError(f"Unterminated string at line {self.line}")
        self.advance() 
        return Token(TokenType.STRING, string, self.line)

    def skip_comment(self):
        character = self.current_char()
        while character is not None and character != "\n":
            self.advance()
            character = self.current_char()

