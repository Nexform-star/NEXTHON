# Functions

Functions allow you to organize code into reusable blocks.

They help reduce repetition and make programs easier to maintain.

## 1. Declaring a function

Use the `function` keyword to declare a function.

```ne
function greet() {
    print("Hello, World!")
}
```

## 2. Calling a function

To execute a function, call it by its name followed by parentheses.

```ne
function greet() {
    print("Hello, World!")
}

greet()
```

Output:

```text
Hello, World!
```

## 3. Function parameters

Functions can receive parameters.

```ne
function greet(name) {
    print("Hello,")
    print(name)
}

greet("Nexform")
```

Output:

```text
Hello,
Nexform
```

## 4. Returning values

Use the `return` keyword to send a value back from a function.

```ne
function add(a, b) {
    return a + b
}

var result = add(10, 5)

print(result)
```

Output:

```text
15
```

## 5. Multiple parameters

Functions can accept multiple parameters.

```ne
function calculateTotal(price, quantity) {
    return price * quantity
}

var total = calculateTotal(20, 3)

print(total)
```

Output:

```text
60
```

## 6. Recursive functions

A recursive function is a function that calls itself.

```ne
function countdown(number) {
    if number <= 0 {
        print("Done!")
        return
    }

    print(number)
    countdown(number - 1)
}

countdown(3)
```

Output:

```text
3
2
1
Done!
```

## Next steps

- [Loops](loops.md)
- [Collections](collections.md)
- [Modules](modules.md)
- [Documentation Home](README.md)

---

[Back to NEXTHON](https://github.com/Nexform-star/NEXTHON)
