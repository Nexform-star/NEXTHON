# Operators

Operators are symbols and keywords used to perform operations on values and variables.

## 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Description | Example |
|---|---|---|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `%` | Modulo | `10 % 3` |
| `**` | Exponentiation | `2 ** 3` |

Example:

```ne id="a2wq8e"
var firstNumber = 10
var secondNumber = 5

print(firstNumber + secondNumber)
print(firstNumber - secondNumber)
print(firstNumber * secondNumber)
print(firstNumber / secondNumber)
```

## 2. Comparison Operators

Comparison operators compare two values and return a boolean.

| Operator | Description |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Example:

```ne id="n3p4lx"
var score = 100

print(score == 100)
print(score > 50)
print(score < 200)
```

## 3. Logical Operators

Logical operators combine or invert boolean expressions.

| Operator | Description |
|---|---|
| `and` | True if both conditions are true |
| `or` | True if at least one condition is true |
| `not` | Reverses a boolean value |

Example:

```ne id="g8w2zs"
var age = 18
var hasPermission = true

print(age >= 18 and hasPermission)
print(age < 18 or hasPermission)
print(not hasPermission)
```

## 4. Operator Precedence

NEXTHON evaluates expressions according to operator precedence.

For example, multiplication is evaluated before addition.

```ne id="x6r2kd"
var result = 10 + 5 * 2

print(result)
```

Output:

```text id="w1k5jm"
20
```

You can use parentheses to control the order of evaluation.

```ne id="p4t9va"
var result = (10 + 5) * 2

print(result)
```

Output:

```text id="v8c2ne"
30
```

## Next steps

- [Conditions](conditions.md)
- [Variables](variables.md)
- [Data Types](data-types.md)
- [Documentation Home](README.md)

---

[Back to NEXTHON](https://github.com/Nexform-star/NEXTHON)
