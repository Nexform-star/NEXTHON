# NEXTHON

**A general-purpose programming language built from scratch in Python.**

NEXTHON is an experimental programming language designed to provide a simple and readable syntax while exploring the fundamentals of language design, interpreters, lexers and parsers.

## Features

- Variables and constants
- Arithmetic and logical expressions
- Conditional statements (`if`, `elif`, `else`)
- Loops (`while`, `for`)
- Functions, parameters and return values
- Recursion
- Lists, tuples and dictionaries
- Built-in functions and string methods
- Module imports
- Exception handling (`try`, `except`, `finally`)
- File operations
- Interactive REPL

## Project Structure

```text
NEXTHON/
├── .vscode/
│   ├── settings.json
│   └── tasks.json
├── examples/
│   ├── hello.ne
│   ├── math.ne
│   └── test_import.ne
├── src/
│   └── nexthon/
│       ├── __init__.py
│       ├── ast.py
│       ├── errors.py
│       ├── interpreter.py
│       ├── lexer.py
│       ├── parser.py
│       └── tokens.py
├── LICENSE
├── README.md
└── nexthon.bat
```

## Getting Started

### Requirements

- Python 3
- Windows (for the provided `.bat` launcher)

### Clone the repository

```bash
git clone https://github.com/Nexform-star/NEXTHON.git
cd NEXTHON
```

### Run a NEXTHON program

On Windows, use the included launcher:

```powershell
.\nexthon.bat .\examples\hello.ne
```

Alternatively, set the Python module path and run the interpreter directly:

```powershell
$env:PYTHONPATH = "src"
py -m nexthon.interpreter .\examples\hello.ne
```

## Example

```ne
function greet(name) {
    print("Hello " + name)
}

var score = 100

if score >= 50 {
    print("Level completed!")
} else {
    print("Try again!")
}

greet("Nexform")
```

Output:

```text
Level completed!
Hello Nexform
```

## VS Code Support

NEXTHON source files use the `.ne` extension.

The repository includes VS Code workspace settings and a task for running the currently active NEXTHON file with `Ctrl + Shift + B`.

Syntax highlighting is available through the separate NEXTHON Language extension.

## Development

NEXTHON is an ongoing learning and development project.

The language is still experimental, and its syntax and features may evolve over time.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

**Created by [Nexform-star](https://github.com/Nexform-star)**

