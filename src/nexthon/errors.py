class NexthonError(Exception):
    def __init__(self, message, line=None, column=None):
        self.message = message
        self.line = line
        self.column = column

        location = ""

        if line is not None:
            location = f" at line {line}"

            if column is not None:
                location += f", column {column}"

        super().__init__(f"{message}{location}")


class LexicalError(NexthonError):
    pass


class ParserError(NexthonError):
    pass


class RuntimeError(NexthonError):
    pass


class ImportError(NexthonError):
    pass


class TypeError(NexthonError):
    pass


class NameError(NexthonError):
    pass


class IndexError(NexthonError):
    pass


class ValueError(NexthonError):
    pass