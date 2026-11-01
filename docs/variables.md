# Variables

Variables are used to store and manage data in a NEXTHON program.

## 1. Declaring variables

Use the `var` keyword followed by a name and a value.

```ne
var username = "Nexform"
var score = 100
var isActive = true
```

## 2. Accessing variables

Use the variable name to access its stored value.

```ne
var username = "Nexform"

print(username)
```

Output:

```text
Nexform
```

## 3. Reassigning variables

Variables declared with `var` can be reassigned.

```ne
var score = 100

score = 150

print(score)
```

Output:

```text
150
```

You can also use the current value to calculate a new one:

```ne
var score = 100

score = score + 50
score = score + 25

print(score)
```

Output:

```text
175
```

## 4. Constants

Constants store values that cannot be reassigned.

Use the `const` keyword:

```ne
const MAX_SCORE = 100

print(MAX_SCORE)
```

Attempting to reassign a constant causes an error.

## 5. Variable naming

Choose descriptive names to make your code easier to understand.

Examples:

```ne
var playerName = "Nexform"
var totalScore = 250
var accountBalance = 500
```

Prefer meaningful names over short or unclear ones.

## 6. Variables in calculations

Variables can be used in expressions.

```ne
var price = 20
var quantity = 3

var total = price * quantity

print(total)
```

Output:

```text
60
```

## Next steps

- [Data Types](data-types.md)
- [Operators](operators.md)
- [Conditions](conditions.md)
- [Documentation Home](README.md)

---

[Back to NEXTHON](https://github.com/Nexform-star/NEXTHON)
