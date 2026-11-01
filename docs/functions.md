# Functions

Functions allow you to organize code into reusable blocks.

They help reduce repetition and make programs easier to maintain.

## 1. Declaring a function

Use the `fun` keyword to declare a function.

```ne id="n1w3pk"
fun greet() {
    print("Hello, World!")
}
```

## 2. Calling a function

To execute a function, call it by its name followed by parentheses.

```ne id="j3c8qa"
fun greet() {
    print("Hello, World!")
}

greet()
```

Output:

```text id="u4t2vw"
Hello, World!
```

## 3. Function parameters

Functions can receive parameters.

```ne id="a5m9rx"
fun greet(name) {
    print("Hello,")
    print(name)
}

greet("Nexform")
```

## 4. Returning values

Use the `return` keyword to send a value back from a function.

```ne id="k7p2yd"
fun add(a, b) {
    return a + b
}

var result = add(10, 5)

print(result)
```

Output:

```text id="v6n3qb"
15
```

## 5. Multiple parameters

Functions can accept multiple parameters.

```ne id="c9x4lm"
fun calculateTotal(price, quantity) {
    return price * quantity
}

var total = calculateTotal(20, 3)

print(total)
```

Output:

```text id="f2w8za"
60
```

## 6. Recursive functions

A recursive function is a function that calls itself.

```ne id="d4j6hs"
fun countdown(number) {
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

```text id="p8r5vn"
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
