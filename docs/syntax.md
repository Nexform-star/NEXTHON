# NEXTHON Syntax

This page introduces the basic syntax rules of the NEXTHON programming language.

## 1. Statements

A statement is an instruction executed by the interpreter.

NEXTHON programs are written using one instruction per line.

```ne
var name = "Nexform"
var score = 100

print(name)
print(score)
```

## 2. Variables

Use the `var` keyword to declare a variable.

```ne
var username = "Nexform"
var level = 5
```

Variables can be reassigned after declaration:

```ne
var score = 100

score = 150
```

## 3. Constants

Use the `const` keyword to declare a constant.

```ne
const MAX_SCORE = 100
```

A constant cannot be reassigned after declaration.

## 4. Comments

Comments allow you to write notes inside your code.

NEXTHON supports two comment styles:

```ne
! This is a comment

# This is also a comment

print("Hello, World!")
```

Comments are ignored by the interpreter.

## 5. Expressions

Expressions produce values.

```ne
var result = 10 + 5

print(result)
```

NEXTHON supports arithmetic and comparison expressions.

```ne
print(10 + 5)
print(10 > 5)
print(10 == 10)
```

## 6. Blocks

Some instructions use braces `{}` to group multiple statements.

For example, conditional statements:

```ne
var score = 75

if score >= 50 {
    print("You passed!")
} else {
    print("You failed!")
}
```

## 7. Naming conventions

For readability, use descriptive names for variables and functions.

Examples:

```ne
var playerName = "Nexform"
var totalScore = 250
var isActive = true
```

## Next steps

- [Variables](variables.md)
- [Data Types](data-types.md)
- [Operators](operators.md)
- [Conditions](conditions.md)
- [Documentation Home](README.md)

---

[Back to NEXTHON](https://github.com/Nexform-star/NEXTHON)
