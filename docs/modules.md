# Modules

Modules allow you to organize your NEXTHON code into separate files and reuse code across multiple programs.

## 1. Creating a module

Create a file named `math_utils.ne`:

```ne
fun add(a, b) {
    return a + b
}

fun multiply(a, b) {
    return a * b
}
```

This file contains two functions that can be reused in other NEXTHON programs.

## 2. Importing a module

Use the `import` keyword to import another NEXTHON file.

For example, create a file named `main.ne`:

```ne
import math_utils

var result = add(10, 5)

print(result)
```

If both files are in the same directory, NEXTHON can load the module.

Output:

```text
15
```

## 3. Reusing module functions

After importing a module, you can use its available functions.

For example:

```ne
import math_utils

print(add(10, 5))
print(multiply(4, 3))
```

Output:

```text
15
12
```

## 4. Module organization

A project can be organized into multiple files:

```text
my_project/
├── main.ne
├── math_utils.ne
└── string_utils.ne
```

This makes programs easier to organize and maintain.

## Next steps

- [Functions](functions.md)
- [Exceptions](exceptions.md)
- [File Handling](file-handling.md)
- [Documentation Home](README.md)

---

[Back to NEXTHON](https://github.com/Nexform-star/NEXTHON)
