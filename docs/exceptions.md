# Exception Handling

Exception handling allows you to detect and manage errors without immediately stopping your program.

NEXTHON supports `try`, `except`, `finally` and `raise`.

## 1. The `try` statement

Use `try` to execute code that may produce an error.

```ne id="a2k9fz"
try {
    var result = 10 / 0
} except {
    print("An error occurred!")
}
```

## 2. The `except` statement

The `except` block executes when an error occurs inside the corresponding `try` block.

```ne id="p8z4jw"
try {
    var result = 10 / 0
} except {
    print("Something went wrong.")
}
```

## 3. The `finally` statement

The `finally` block executes after the `try` and `except` blocks, whether an error occurred or not.

```ne id="x7m3qa"
try {
    print("Executing program...")
} except {
    print("An error occurred.")
} finally {
    print("Execution completed.")
}
```

## 4. The `raise` statement

Use `raise` to manually trigger an error.

```ne id="n4v6yc"
raise "Something went wrong!"
```

You can also raise an error inside a function:

```ne id="k2w9fr"
fun checkAge(age) {
    if age < 18 {
        raise "Access denied."
    }

    print("Access granted!")
}

checkAge(20)
```

## 5. Combining exception handling

You can combine `try`, `except` and `finally` to handle errors and execute cleanup instructions.

```ne id="b5q1ht"
try {
    var result = 100 / 0
    print(result)
} except {
    print("Unable to calculate the result.")
} finally {
    print("Program finished.")
}
```

## Next steps

- [Functions](functions.md)
- [Modules](modules.md)
- [Built-in Functions](built-in-functions.md)
- [Documentation Home](README.md)

---

[Back to NEXTHON](https://github.com/Nexform-star/NEXTHON)
