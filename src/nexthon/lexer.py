from .tokens import Token, TokenType
from .errors import LexicalError


KEYWORDS = {
    "var",
    "const",
    "print",
    "if",
    "elif",
    "else",
    "while",
    "for",
    "in",
    "function",
    "return",
    "break",
    "continue",
    "true",
    "false",
    "null",
    "and",
    "or",
    "not",
    "import",
    "as",
    "try",
    "except",
    "finally",
    "raise",
}

OPERATORS = [
    "**=",
    "//=",
    "==",
    "!=",
    "<=",
    ">=",
    "+=",
    "-=",
    "*=",
    "/=",
    "%=",
    "**",
    "//",
    "->",
    "=",
    "+",
    "-",
    "*",
    "/",
    "%",
    "<",
    ">",
]

PUNCTUATION = {
    "(",
    ")",
    "{",
    "}",
    "[",
    "]",
    ",",
    ";",
    ".",
    ":",
}


class Lexer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.line = 1
        self.column = 1

    def current_char(self):
        if self.position < len(self.source):
            return self.source[self.position]

        return None

    def peek_char(self, offset=1):
        position = self.position + offset

        if position < len(self.source):
            return self.source[position]

        return None

    def advance(self):
        character = self.current_char()

        if character is None:
            return None

        self.position += 1

        if character == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1

        return self.current_char()

    def skip_whitespace(self):
        while (
            self.current_char() is not None
            and self.current_char().isspace()
        ):
            self.advance()

    def skip_comment(self):
        while (
            self.current_char() is not None
            and self.current_char() != "\n"
        ):
            self.advance()

    def read_number(self):
        start_line = self.line
        number = ""
        dot_count = 0

        while self.current_char() is not None:
            character = self.current_char()

            if character.isdigit():
                number += character
                self.advance()

            elif character == ".":
                if dot_count > 0 or not self.peek_char().isdigit():
                    break

                dot_count += 1
                number += character
                self.advance()

            else:
                break

        return Token(TokenType.NUMBER, number, start_line)

    def read_identifier(self):
        start_line = self.line
        name = ""

        while self.current_char() is not None:
            character = self.current_char()

            if character.isalnum() or character == "_":
                name += character
                self.advance()
            else:
                break

        token_type = (
            TokenType.KEYWORD
            if name in KEYWORDS
            else TokenType.IDENTIFIER
        )

        return Token(token_type, name, start_line)

    def read_string(self):
        start_line = self.line
        quote = self.current_char()
        self.advance()

        string = ""

        escapes = {
            "n": "\n",
            "t": "\t",
            "r": "\r",
            '"': '"',
            "'": "'",
            "\\": "\\",
            "0": "\0",
        }

        while self.current_char() is not None:
            character = self.current_char()

            if character == quote:
                self.advance()
                return Token(TokenType.STRING, string, start_line)

            if character == "\n":
                raise LexicalError(
                    f"Unterminated string at line {start_line}"
                )

            if character == "\\":
                self.advance()

                escaped = self.current_char()

                if escaped is None:
                    break

                string += escapes.get(escaped, escaped)
                self.advance()
                continue

            string += character
            self.advance()

        raise LexicalError(
            f"Unterminated string at line {start_line}"
        )

    def read_operator(self):
        start_line = self.line

        for operator in OPERATORS:
            if self.source.startswith(operator, self.position):
                for _ in operator:
                    self.advance()

                return Token(
                    TokenType.OPERATOR,
                    operator,
                    start_line
                )

        return None

    def get_next_token(self):
        self.skip_whitespace()

        character = self.current_char()

        if character is None:
            return Token(TokenType.EOF, "", self.line)

        if character == "!":
            if self.peek_char() == "=":
                self.advance()
                self.advance()

                return Token(
                    TokenType.OPERATOR,
                    "!=",
                    self.line
                )

            self.skip_comment()
            return self.get_next_token()

        if character == "#":
            self.skip_comment()
            return self.get_next_token()

        if character.isdigit():
            return self.read_number()

        if character.isalpha() or character == "_":
            return self.read_identifier()

        if character in ('"', "'"):
            return self.read_string()

        operator = self.read_operator()

        if operator is not None:
            return operator

        if character in PUNCTUATION:
            start_line = self.line
            self.advance()

            return Token(
                TokenType.PUNCTUATION,
                character,
                start_line
            )

        raise LexicalError(
            f"Unknown character '{character}' "
            f"at line {self.line}, column {self.column}"
        )

    def tokenize(self):
        tokens = []

        while True:
            token = self.get_next_token()
            tokens.append(token)

            if token.token_type == TokenType.EOF:
                break

        return tokens