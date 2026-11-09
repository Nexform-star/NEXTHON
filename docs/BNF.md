# NEXTHON — Formal Grammar (BNF)

It provides a formal reference for the language grammar, including declarations, statements, expressions, operators and data structures.

The grammar uses an EBNF-style notation.

## 1. Notation

| Notation | Meaning                  |
| -------- | ------------------------ |
| `::=`    | Is defined as            |
| `\|`     | Alternative              |
| `[ ]`    | Optional element         |
| `{ }`    | Zero or more repetitions |
| `" "`    | Literal token            |
| `EOF`    | End of file              |

## 2. Program structure

```ebnf
<program> ::= { ";" } { <statement> { ";" } } EOF

<block> ::= "{"
            { ";" }
            { <statement> { ";" } }
            "}"
```

Statements are not required to end with a semicolon. Newlines are ignored by the lexer.

## 3. Statements

```ebnf
<statement> ::= <variable_declaration>
              | <print_statement>
              | <assignment>
              | <if_statement>
              | <while_statement>
              | <for_statement>
              | <function_declaration>
              | <return_statement>
              | <break_statement>
              | <continue_statement>
              | <import_statement>
              | <try_statement>
              | <raise_statement>
              | <expression_statement>
```

### 3.1 Variable declarations

```ebnf
<variable_declaration> ::= "var" <identifier> "=" <expression>
                         | "const" <identifier> "=" <expression>
```

Examples:

```ne
var name = "NEXTHON"
var version = 0.1
const PI = 3.14159
```

### 3.2 Print statement

```ebnf
<print_statement> ::= "print" "(" <expression> ")"
```

Example:

```ne
print("Hello, NEXTHON!")
```

### 3.3 Assignments

```ebnf
<assignment> ::= <assignment_target> <assignment_operator> <expression>

<assignment_target> ::= <identifier>
                      | <indexed_identifier>

<indexed_identifier> ::= <identifier> { "[" <expression> "]" }

<assignment_operator> ::= "="
                        | "+="
                        | "-="
                        | "*="
                        | "/="
                        | "%="
                        | "**="
                        | "//="
```

Examples:

```ne
var count = 10
count = 20
count += 5
count -= 2

var numbers = [1, 2, 3]
numbers[0] = 10
```

### 3.4 Conditional statements

```ebnf
<if_statement> ::= "if" <expression> <block> [ <else_clause> ]

<else_clause> ::= "elif" <expression> <block> [ <else_clause> ]
                | "else" <block>
```

Examples:

```ne
if age >= 18 {
    print("Adult")
} elif age >= 13 {
    print("Teenager")
} else {
    print("Child")
}
```

### 3.5 While loops

```ebnf
<while_statement> ::= "while" <expression> <block>
```

Example:

```ne
while count < 10 {
    count += 1
}
```

### 3.6 For loops

```ebnf
<for_statement> ::= "for" <identifier> "in" <expression> <block>
```

Example:

```ne
for item in numbers {
    print(item)
}
```

### 3.7 Function declarations

```ebnf
<function_declaration> ::= "function" <identifier>
                           "(" [ <parameter_list> ] ")"
                           <block>

<parameter_list> ::= <identifier> { "," <identifier> }
```

Example:

```ne
function greet(name) {
    print("Hello " + name)
}
```

### 3.8 Return statement

```ebnf
<return_statement> ::= "return" [ <expression> ]
```

Example:

```ne
function add(a, b) {
    return a + b
}
```

### 3.9 Loop control

```ebnf
<break_statement> ::= "break"

<continue_statement> ::= "continue"
```

### 3.10 Imports

```ebnf
<import_statement> ::= "import" <module_name> [ "as" <identifier> ]

<module_name> ::= <identifier>
                | <string>
```

Examples:

```ne
import math
import math as m
import "my_module.ne"
```

### 3.11 Exception handling

```ebnf
<try_statement> ::= "try" <block>
                    "except" [ <identifier> ]
                    <block>
                    [ "finally" <block> ]
```

Example:

```ne
try {
    print(10 / 0)
} except error {
    print(error)
} finally {
    print("Finished")
}
```

### 3.12 Raise statement

```ebnf
<raise_statement> ::= "raise" <expression>
```

Example:

```ne
raise "Something went wrong"
```

## 4. Expressions

Expressions follow a precedence hierarchy.

```ebnf
<expression> ::= <or_expression>

<or_expression> ::= <and_expression> { "or" <and_expression> }

<and_expression> ::= <comparison> { "and" <comparison> }

<comparison> ::= <arithmetic_expression>
                 { <comparison_operator> <arithmetic_expression> }

<comparison_operator> ::= "=="
                        | "!="
                        | "<"
                        | ">"
                        | "<="
                        | ">="
                        | "in"

<arithmetic_expression> ::= <term> { ( "+" | "-" ) <term> }

<term> ::= <power> { ( "*" | "/" | "//" | "%" ) <power> }

<power> ::= <factor> [ "**" <power> ]

<factor> ::= <unary_operator> <factor>
           | <primary>

<unary_operator> ::= "-"
                   | "+"
                   | "not"
```

## 5. Primary expressions

```ebnf
<primary> ::= <number>
            | <string>
            | "true"
            | "false"
            | "null"
            | <identifier_expression>
            | <list_literal>
            | <tuple_literal>
            | <dict_literal>
```

### 5.1 Identifiers and function calls

```ebnf
<identifier_expression> ::= <identifier>
                            [ "(" [ <argument_list> ] ")" ]
                            { <postfix_operation> }

<argument_list> ::= <expression> { "," <expression> }

<postfix_operation> ::= "[" <expression> "]"
                       | "." <identifier>
                         [ "(" [ <argument_list> ] ")" ]
```

Examples:

```ne
print("Hello")

calculate(10, 20)

user.name

user.get_name()

numbers[0]

user.address.city
```

### 5.2 Lists

```ebnf
<list_literal> ::= "[" [ <expression_list> [ "," ] ] "]"

<expression_list> ::= <expression> { "," <expression> }
```

Example:

```ne
var numbers = [1, 2, 3, 4]
var empty = []
```

### 5.3 Tuples

```ebnf
<tuple_literal> ::= "(" ")"
                  | "(" <expression> "," [ <expression_list> [ "," ] ] ")"
                  | "(" <expression> ")"
```

Examples:

```ne
var empty = ()
var point = (10, 20)
var single = (10,)
```

### 5.4 Dictionaries

```ebnf
<dict_literal> ::= "{" [ <dictionary_entries> [ "," ] ] "}"

<dictionary_entries> ::= <dictionary_entry>
                         { "," <dictionary_entry> }

<dictionary_entry> ::= <expression> ":" <expression>
```

Example:

```ne
var user = {
    "name": "Alex",
    "age": 20
}
```

## 6. Lexical structure

The lexer recognizes the following token categories.

### 6.1 Keywords

```text
var const print
if elif else
while for in
function return
break continue
true false null
and or not
import as
try except finally raise
```

### 6.2 Operators

```text
=  +  -  *  /  %
** // ->

== != < > <= >=

+= -= *= /= %= **= //=
```

### 6.3 Punctuation

```text
( ) { } [ ]
, ; . :
```

### 6.4 Identifiers

```ebnf
<identifier> ::= <letter> { <letter> | <digit> | "_" }
```

Identifiers cannot begin with a digit.

Examples:

```ne
name
user_name
variable123
_private
```

### 6.5 Numbers

```ebnf
<number> ::= <integer> [ "." <digit_sequence> ]

<integer> ::= <digit_sequence>

<digit_sequence> ::= <digit> { <digit> }

<digit> ::= "0" | "1" | "2" | "3" | "4"
          | "5" | "6" | "7" | "8" | "9"
```

Examples:

```ne
42
3.14
1000
0.5
```

### 6.6 Strings

Strings can use single or double quotes.

```ebnf
<string> ::= '"' { <string_character> } '"'
           | "'" { <string_character> } "'"
```

Supported escape sequences:

| Sequence | Meaning         |
| -------- | --------------- |
| `\n`     | Newline         |
| `\t`     | Tab             |
| `\r`     | Carriage return |
| `\"`     | Double quote    |
| `\'`     | Single quote    |
| `\\`     | Backslash       |
| `\0`     | Null character  |

### 6.7 Comments

Comments begin with `#` or `!` and continue until the end of the line.

```ne
# This is a comment

! This is also a comment

print("Hello") # Inline comment
```

The sequence `!=` is recognized as an inequality operator rather than a comment.

## 7. Operator precedence

From lowest to highest precedence:

| Priority | Operators                              | Associativity |
| -------- | -------------------------------------- | ------------- |
| 1        | `or`                                   | Left          |
| 2        | `and`                                  | Left          |
| 3        | `==`, `!=`, `<`, `>`, `<=`, `>=`, `in` | Left          |
| 4        | `+`, `-`                               | Left          |
| 5        | `*`, `/`, `//`, `%`                    | Left          |
| 6        | `**`                                   | Right         |
| 7        | `+`, `-`, `not` (unary)                | Right         |

## 8. Parser implementation notes

The grammar above documents the syntax recognized by the current parser.

Some additional restrictions apply:

- Function parameters must be identifiers.
- Function calls do not accept trailing commas in their argument lists.
- Lists, tuples and dictionaries support trailing commas.
- A `try` statement must contain an `except` block.
- A `finally` block is optional.
- Assignment is supported for variables and indexed expressions, but not attribute assignments.
- Standalone expression statements are restricted to function and method calls or assignments.
- Parenthesized expressions are supported; parentheses without a comma do not create a tuple.
- Newlines are not statement separators because they are discarded by the lexer.

This document describes the current NEXTHON parser implementation and should be updated whenever the language grammar changes.
