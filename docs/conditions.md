# Conditions

Conditional statements allow a NEXTHON program to make decisions based on specific conditions.

## 1. The `if` statement

The `if` statement executes a block of code when a condition is true.

```ne
var score = 75

if score >= 50 {
    print("You passed!")
}
```

Output:

```text
You passed!
```

## 2. The `else` statement

The `else` statement executes when the `if` condition is false.

```ne
var score = 30

if score >= 50 {
    print("You passed!")
} else {
    print("You failed!")
}
```

Output:

```text
You failed!
```

## 3. The `elif` statement

Use `elif` to check additional conditions when previous conditions are false.

```ne
var score = 75

if score >= 90 {
    print("Excellent!")
} elif score >= 50 {
    print("Good job!")
} else {
    print("Try again!")
}
```

Output:

```text
Good job!
```

## 4. Combining conditions

You can combine multiple conditions using logical operators.

```ne
var age = 20
var hasPermission = true

if age >= 18 and hasPermission {
    print("Access granted!")
} else {
    print("Access denied!")
}
```

## 5. Nested conditions

You can place an `if` statement inside another conditional block.

```ne
var age = 20
var hasID = true

if age >= 18 {
    if hasID {
        print("Welcome!")
    } else {
        print("Identification required.")
    }
} else {
    print("Access denied.")
}
```

## Next steps

- [Operators](operators.md)
- [Loops](loops.md)
- [Functions](functions.md)
- [Documentation Home](README.md)

---

[Back to NEXTHON](https://github.com/Nexform-star/NEXTHON)
