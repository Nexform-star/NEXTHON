import os

import sys

import math

import json

import random

import time

from pathlib import Path

from .errors import RuntimeError

from .ast import (

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

    BinaryOperation,

    UnaryOperation,

    IfStatement,

    WhileStatement,

    ForStatement,

    BreakStatement,

    ContinueStatement,

    FunctionDeclaration,

    FunctionCall,

    ReturnStatement,

    ImportStatement,

    TryStatement,

    RaiseStatement,

)

from .lexer import Lexer

from .parser import Parser

class ReturnSignal(Exception):

    def __init__(self, value):

        self.value = value

class BreakSignal(Exception):

    pass

class ContinueSignal(Exception):

    pass

class NexthonException(Exception):

    pass

class Interpreter:

    def __init__(self):

        self.variables = {}

        self.constants = set()

        self.scopes = [self.variables]

        self.functions = {}

        self.call_depth = 0

        self.loop_depth = 0

        self.module_cache = {}

        self.current_directory = Path.cwd()

        self.native_functions = {

            "input": self.native_input,

            "type": self.native_type,

            "str": self.native_str,

            "int": self.native_int,

            "float": self.native_float,

            "bool": self.native_bool,

            "len": self.native_len,

            "abs": self.native_abs,

            "round": self.native_round,

            "min": self.native_min,

            "max": self.native_max,

            "sum": self.native_sum,

            "range": self.native_range,

            "enumerate": self.native_enumerate,

            "sorted": self.native_sorted,

            "reversed": self.native_reversed,

            "list": self.native_list,

            "tuple": self.native_tuple,

            "dict": self.native_dict,

            "set": self.native_set,

            "print": self.native_print,

            "sqrt": self.native_sqrt,

            "random": self.native_random,

            "time": self.native_time,

            "exit": self.native_exit,

            "json_encode": self.native_json_encode,

            "json_decode": self.native_json_decode,

            "read_file": self.native_read_file,

            "write_file": self.native_write_file,

            "append_file": self.native_append_file,

            "exists": self.native_exists,

        }

    def get_variable(self, name):

        for scope in reversed(self.scopes):

            if name in scope:

                return scope[name]

        raise RuntimeError(f"Undefined variable '{name}'")

    def set_variable(self, name, value):

        for scope in reversed(self.scopes):

            if name in scope:

                if name in self.constants:

                    raise RuntimeError(

                        f"Cannot modify constant '{name}'"

                    )

                scope[name] = value

                return

        raise RuntimeError(f"Undefined variable '{name}'")

    def get_index(self, collection, index):

        try:

            if isinstance(collection, (list, tuple, str)):

                if not isinstance(index, int) or isinstance(index, bool):

                    raise RuntimeError("Index must be an integer")

                return collection[index]

            if isinstance(collection, dict):

                if index not in collection:

                    raise RuntimeError(

                        f"Key not found: {index}"

                    )

                return collection[index]

            raise RuntimeError(

                f"Cannot index value of type '{self.get_type(collection)}'"

            )

        except IndexError:

            raise RuntimeError(f"Index out of range: {index}")

        except TypeError as error:

            raise RuntimeError(str(error))

    def set_index(self, collection, index, value):

        try:

            if isinstance(collection, list):

                if not isinstance(index, int) or isinstance(index, bool):

                    raise RuntimeError("List index must be an integer")

                collection[index] = value

                return

            if isinstance(collection, dict):

                collection[index] = value

                return

            raise RuntimeError(

                "Index assignment requires a list or dictionary"

            )

        except IndexError:

            raise RuntimeError(f"Index out of range: {index}")

        except TypeError as error:

            raise RuntimeError(str(error))

    def get_type(self, value):

        if value is None:

            return "null"

        if isinstance(value, bool):

            return "bool"

        if isinstance(value, int):

            return "int"

        if isinstance(value, float):

            return "float"

        if isinstance(value, str):

            return "str"

        if isinstance(value, list):

            return "list"

        if isinstance(value, tuple):

            return "tuple"

        if isinstance(value, dict):

            return "dict"

        if isinstance(value, set):

            return "set"

        if callable(value):

            return "function"

        return "unknown"

    def call_method(self, statement):

        collection = self.evaluate(statement.object)

        arguments = [

            self.evaluate(argument)

            for argument in statement.arguments

        ]

        name = statement.name

        if isinstance(collection, dict) and name in collection and callable(collection[name]):

            try:

                return collection[name](*arguments)

            except RuntimeError:

                raise

            except Exception as error:

                raise RuntimeError(f"{name}(): {error}")

        if isinstance(collection, list):

            if name == "append":

                self.check_argument_count(name, arguments, 1)

                collection.append(arguments[0])

                return None

            if name == "extend":

                self.check_argument_count(name, arguments, 1)

                collection.extend(arguments[0])

                return None

            if name == "insert":

                self.check_argument_count(name, arguments, 2)

                collection.insert(*arguments)

                return None

            if name == "pop":

                if len(arguments) > 1:

                    raise RuntimeError("pop() accepts zero or one argument")

                if not collection:

                    raise RuntimeError("Cannot pop from an empty list")

                return collection.pop(*arguments)

            if name == "remove":

                self.check_argument_count(name, arguments, 1)

                collection.remove(arguments[0])

                return None

            if name == "clear":

                self.check_argument_count(name, arguments, 0)

                collection.clear()

                return None

            if name == "copy":

                self.check_argument_count(name, arguments, 0)

                return collection.copy()

            if name == "index":

                self.check_argument_count(name, arguments, 1)

                return collection.index(arguments[0])

            if name == "count":

                self.check_argument_count(name, arguments, 1)

                return collection.count(arguments[0])

            if name == "sort":

                self.check_argument_count(name, arguments, 0)

                collection.sort()

                return None

            if name == "reverse":

                self.check_argument_count(name, arguments, 0)

                collection.reverse()

                return None

        if isinstance(collection, dict):

            if name == "keys":

                self.check_argument_count(name, arguments, 0)

                return list(collection.keys())

            if name == "values":

                self.check_argument_count(name, arguments, 0)

                return list(collection.values())

            if name == "items":

                self.check_argument_count(name, arguments, 0)

                return [

                    [key, value]

                    for key, value in collection.items()

                ]

            if name == "get":

                if len(arguments) not in (1, 2):

                    raise RuntimeError(

                        "get() expects one or two arguments"

                    )

                return collection.get(*arguments)

            if name == "update":

                self.check_argument_count(name, arguments, 1)

                collection.update(arguments[0])

                return None

            if name == "pop":

                if len(arguments) not in (1, 2):

                    raise RuntimeError(

                        "pop() expects one or two arguments"

                    )

                return collection.pop(*arguments)

            if name == "clear":

                self.check_argument_count(name, arguments, 0)

                collection.clear()

                return None

            if name == "copy":

                self.check_argument_count(name, arguments, 0)

                return collection.copy()

        if isinstance(collection, str):

            if name == "upper":

                self.check_argument_count(name, arguments, 0)

                return collection.upper()

            if name == "lower":

                self.check_argument_count(name, arguments, 0)

                return collection.lower()

            if name == "strip":

                self.check_argument_count(name, arguments, 0)

                return collection.strip()

            if name == "split":

                if len(arguments) > 1:

                    raise RuntimeError(

                        "split() accepts zero or one argument"

                    )

                return collection.split(*arguments)

            if name == "replace":

                self.check_argument_count(name, arguments, 2)

                return collection.replace(*arguments)

            if name == "startswith":

                self.check_argument_count(name, arguments, 1)

                return collection.startswith(arguments[0])

            if name == "endswith":

                self.check_argument_count(name, arguments, 1)

                return collection.endswith(arguments[0])

            if name == "find":

                self.check_argument_count(name, arguments, 1)

                return collection.find(arguments[0])

            if name == "count":

                self.check_argument_count(name, arguments, 1)

                return collection.count(arguments[0])

            if name == "capitalize":

                self.check_argument_count(name, arguments, 0)

                return collection.capitalize()

            if name == "title":

                self.check_argument_count(name, arguments, 0)

                return collection.title()

            if name == "join":

                self.check_argument_count(name, arguments, 1)

                return collection.join(arguments[0])

        raise RuntimeError(

            f"Unknown method '{name}' for type '{self.get_type(collection)}'"

        )

    def check_argument_count(self, name, arguments, expected):

        if len(arguments) != expected:

            raise RuntimeError(

                f"{name}() expects {expected} argument(s), "

                f"got {len(arguments)}"

            )

    def evaluate(self, expression):

        if isinstance(expression, StringLiteral):

            return expression.value

        if isinstance(expression, ListLiteral):

            return [

                self.evaluate(element)

                for element in expression.elements

            ]

        if isinstance(expression, TupleLiteral):

            return tuple(

                self.evaluate(element)

                for element in expression.elements

            )

        if isinstance(expression, DictLiteral):

            result = {}

            for key, value in expression.entries:

                evaluated_key = self.evaluate(key)

                evaluated_value = self.evaluate(value)

                result[evaluated_key] = evaluated_value

            return result

        if isinstance(expression, IndexAccess):

            collection = self.evaluate(expression.collection)

            index = self.evaluate(expression.index)

            return self.get_index(collection, index)

        if isinstance(expression, AttributeAccess):

            obj = self.evaluate(expression.object)

            if isinstance(obj, dict) and expression.name in obj:

                return obj[expression.name]

            raise RuntimeError(

                f"Unknown attribute '{expression.name}'"

            )

        if isinstance(expression, MethodCall):

            return self.call_method(expression)

        if isinstance(expression, FunctionCall):

            return self.call_function(expression)

        if isinstance(expression, UnaryOperation):

            value = self.evaluate(expression.operand)

            if expression.operator == "-":

                return -value

            if expression.operator == "+":

                return +value

            if expression.operator == "not":

                return not value

        if isinstance(expression, BinaryOperation):

            left = self.evaluate(expression.left)

            if expression.operator == "and":

                return bool(left) and bool(

                    self.evaluate(expression.right)

                )

            if expression.operator == "or":

                return bool(left) or bool(

                    self.evaluate(expression.right)

                )

            right = self.evaluate(expression.right)

            operator = expression.operator

            try:

                operations = {

                    "+": lambda: left + right,

                    "-": lambda: left - right,

                    "*": lambda: left * right,

                    "/": lambda: left / right,

                    "//": lambda: left // right,

                    "%": lambda: left % right,

                    "**": lambda: left ** right,

                    "==": lambda: left == right,

                    "!=": lambda: left != right,

                    "<": lambda: left < right,

                    ">": lambda: left > right,

                    "<=": lambda: left <= right,

                    ">=": lambda: left >= right,

                    "in": lambda: left in right,

                }

                if operator not in operations:

                    raise RuntimeError(

                        f"Unknown operator '{operator}'"

                    )

                return operations[operator]()

            except (TypeError, ValueError, ZeroDivisionError, OverflowError) as error:

                raise RuntimeError(str(error))

        if isinstance(expression, str):

            return self.get_variable(expression)

        return expression

    def call_function(self, statement):

        arguments = [

            self.evaluate(argument)

            for argument in statement.arguments

        ]

        if statement.name in self.native_functions:

            try:

                return self.native_functions[statement.name](*arguments)

            except RuntimeError:

                raise

            except Exception as error:

                raise RuntimeError(

                    f"{statement.name}(): {error}"

                )

        return self.call_named_function(statement.name, arguments)

    def call_named_function(self, name, arguments):

        if name not in self.functions:

            raise RuntimeError(

                f"Undefined function '{name}'"

            )

        function = self.functions[name]

        if len(arguments) != len(function.parameters):

            raise RuntimeError(

                f"Function '{name}' expects "

                f"{len(function.parameters)} arguments, "

                f"got {len(arguments)}"

            )

        local_scope = dict(zip(function.parameters, arguments))

        self.scopes.append(local_scope)

        self.call_depth += 1

        previous_loop_depth = self.loop_depth

        self.loop_depth = 0

        try:

            try:

                self.interpret(function.body)

            except ReturnSignal as signal:

                return signal.value

            return None

        finally:

            self.loop_depth = previous_loop_depth

            self.call_depth -= 1

            self.scopes.pop()

    def native_input(self, prompt=""):

        return input(str(prompt))

    def native_type(self, value):

        return self.get_type(value)

    def native_str(self, value):

        return str(value)

    def native_int(self, value):

        return int(value)

    def native_float(self, value):

        return float(value)

    def native_bool(self, value):

        return bool(value)

    def native_len(self, value):

        return len(value)

    def native_abs(self, value):

        return abs(value)

    def native_round(self, value, digits=0):

        return round(value, int(digits))

    def native_min(self, *values):

        if len(values) == 1:

            return min(values[0])

        return min(values)

    def native_max(self, *values):

        if len(values) == 1:

            return max(values[0])

        return max(values)

    def native_sum(self, values):

        return sum(values)

    def native_range(self, *arguments):

        return list(range(*arguments))

    def native_enumerate(self, iterable):

        return [

            [index, value]

            for index, value in enumerate(iterable)

        ]

    def native_sorted(self, iterable):

        return sorted(iterable)

    def native_reversed(self, iterable):

        return list(reversed(iterable))

    def native_list(self, value=None):

        return [] if value is None else list(value)

    def native_tuple(self, value=None):

        return () if value is None else tuple(value)

    def native_dict(self, value=None):

        return {} if value is None else dict(value)

    def native_set(self, value=None):

        return set() if value is None else set(value)

    def native_print(self, *values):

        print(*values)

        return None

    def native_sqrt(self, value):

        return math.sqrt(value)

    def native_random(self):

        return random.random()

    def native_time(self):

        return time.time()

    def native_exit(self, code=0):

        raise SystemExit(code)

    def native_json_encode(self, value):

        return json.dumps(value, ensure_ascii=False)

    def native_json_decode(self, value):

        return json.loads(value)

    def native_read_file(self, filename):

        path = self.resolve_path(filename)

        with open(path, "r", encoding="utf-8") as file:

            return file.read()

    def native_write_file(self, filename, content):

        path = self.resolve_path(filename)

        with open(path, "w", encoding="utf-8") as file:

            file.write(str(content))

        return None

    def native_append_file(self, filename, content):

        path = self.resolve_path(filename)

        with open(path, "a", encoding="utf-8") as file:

            file.write(str(content))

        return None

    def native_exists(self, filename):

        return self.resolve_path(filename).exists()

    def resolve_path(self, filename):

        path = Path(str(filename))

        if not path.is_absolute():

            path = self.current_directory / path

        return path.resolve()

    def execute_import(self, statement):

        module_name = str(statement.module)

        if module_name in self.module_cache:

            module = self.module_cache[module_name]

        else:

            filename = module_name

            if not filename.endswith(".ne"):

                filename += ".ne"

            path = self.resolve_path(filename)

            if not path.is_file():

                raise RuntimeError(

                    f"Module not found: '{module_name}'"

                )

            source = path.read_text(encoding="utf-8")

            lexer = Lexer(source)

            parser = Parser(lexer)

            program = parser.parse_program()

            module = Interpreter()

            module.current_directory = path.parent

            module.interpret(program)

            self.module_cache[module_name] = module

        namespace = dict(module.variables)

        for function_name in module.functions:

            def imported_function(*arguments, _module=module, _name=function_name):

                return _module.call_named_function(_name, list(arguments))

            namespace[function_name] = imported_function

        alias = statement.alias or Path(module_name).stem

        self.scopes[-1][alias] = namespace

    def interpret_statement(self, statement):

        if isinstance(statement, VariableDeclaration):

            value = self.evaluate(statement.value)

            if statement.name in self.scopes[-1]:

                raise RuntimeError(

                    f"Variable '{statement.name}' already declared"

                )

            self.scopes[-1][statement.name] = value

            if getattr(statement, "constant", False):

                self.constants.add(statement.name)

        elif isinstance(statement, Assignment):

            value = self.evaluate(statement.value)

            self.set_variable(statement.name, value)

        elif isinstance(statement, IndexAssignment):

            collection = self.evaluate(statement.collection)

            index = self.evaluate(statement.index)

            value = self.evaluate(statement.value)

            self.set_index(collection, index, value)

        elif isinstance(statement, PrintStatement):

            print(self.evaluate(statement.value))

        elif isinstance(statement, IfStatement):

            if self.evaluate(statement.condition):

                self.interpret(statement.body)

            elif statement.else_body is not None:

                self.interpret(statement.else_body)

        elif isinstance(statement, WhileStatement):

            self.loop_depth += 1

            try:

                while self.evaluate(statement.condition):

                    try:

                        self.interpret(statement.body)

                    except ContinueSignal:

                        continue

                    except BreakSignal:

                        break

            finally:

                self.loop_depth -= 1

        elif isinstance(statement, ForStatement):

            iterable = self.evaluate(statement.iterable)

            self.loop_depth += 1

            try:

                for value in iterable:

                    self.scopes[-1][statement.variable] = value

                    try:

                        self.interpret(statement.body)

                    except ContinueSignal:

                        continue

                    except BreakSignal:

                        break

            finally:

                self.loop_depth -= 1

            self.scopes[-1].pop(statement.variable, None)

        elif isinstance(statement, FunctionDeclaration):

            self.functions[statement.name] = statement

        elif isinstance(statement, (FunctionCall, MethodCall)):

            self.evaluate(statement)

        elif isinstance(statement, ReturnStatement):

            if self.call_depth == 0:

                raise RuntimeError(

                    f"Line {statement.line}: Return outside function"

                )

            value = (

                self.evaluate(statement.value)

                if statement.value is not None

                else None

            )

            raise ReturnSignal(value)

        elif isinstance(statement, BreakStatement):

            if self.loop_depth == 0:

                raise RuntimeError(

                    f"Line {statement.line}: Break outside loop"

                )

            raise BreakSignal()

        elif isinstance(statement, ContinueStatement):

            if self.loop_depth == 0:

                raise RuntimeError(

                    f"Line {statement.line}: Continue outside loop"

                )

            raise ContinueSignal()

        elif isinstance(statement, ImportStatement):

            self.execute_import(statement)

        elif isinstance(statement, TryStatement):

            try:

                self.interpret(statement.body)

            except (RuntimeError, NexthonException) as error:

                if statement.exception_name:

                    self.scopes[-1][statement.exception_name] = str(error)

                self.interpret(statement.except_body)

            finally:

                if statement.finally_body is not None:

                    self.interpret(statement.finally_body)

        elif isinstance(statement, RaiseStatement):

            value = self.evaluate(statement.value)

            raise NexthonException(str(value))

    def interpret(self, program):

        for statement in program.statements:

            try:

                self.interpret_statement(statement)

            except (

                ReturnSignal,

                BreakSignal,

                ContinueSignal,

                SystemExit,

            ):

                raise

            except RuntimeError as error:

                line = getattr(statement, "line", None)

                if line is not None:

                    raise RuntimeError(

                        f"Line {line}: {error}"

                    )

                raise

def run_source(source, filename="<memory>"):

    lexer = Lexer(source)

    parser = Parser(lexer)

    program = parser.parse_program()

    interpreter = Interpreter()

    if filename != "<memory>":

        interpreter.current_directory = Path(filename).resolve().parent

    interpreter.interpret(program)

    return interpreter

def run_file(filename):

    path = Path(filename).resolve()

    if not path.is_file():

        raise RuntimeError(f"File not found: {path}")

    source = path.read_text(encoding="utf-8")

    return run_source(source, str(path))

def count_open_blocks(source):

    depth = 0

    in_string = None

    escaped = False

    for character in source:

        if in_string:

            if escaped:

                escaped = False

            elif character == "\\":

                escaped = True

            elif character == in_string:

                in_string = None

            continue

        if character in ('"', "'"):

            in_string = character

        elif character == "!":

            break

        elif character == "{":

            depth += 1

        elif character == "}":

            depth -= 1

    return depth

if __name__ == "__main__":

    if len(sys.argv) > 1:

        try:

            run_file(sys.argv[1])

        except Exception as error:

            print(f"NEXTHON ERROR: {error}")

            sys.exit(1)

    else:

        print("NEXTHON V1")

        print("Type 'exit()' to quit.")

        interpreter = Interpreter()

        buffer = []

        while True:

            try:

                prompt = "... " if buffer else ">>> "

                source = input(prompt)

                if not buffer and source.strip() == "":

                    continue

                if not buffer and source.strip() == "exit()":

                    break

                buffer.append(source)

                complete_source = "\n".join(buffer)

                if count_open_blocks(complete_source) > 0:

                    continue

                try:

                    lexer = Lexer(complete_source)

                    parser = Parser(lexer)

                    program = parser.parse_program()

                    interpreter.interpret(program)

                except Exception as error:

                    print(f"NEXTHON ERROR: {error}")

                buffer.clear()

            except (KeyboardInterrupt, EOFError):

                print()

                buffer.clear()

                break
