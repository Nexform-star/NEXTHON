# Loops

Loops allow you to execute a block of code multiple times.

NEXTHON supports `while` and `for` loops.

## 1. The `while` loop

A `while` loop repeats a block of code as long as its condition is true.

```ne
var count = 0

while count < 5 {
    print(count)
    count = count + 1
}
```

Output:

```text
0
1
2
3
4
```

## 2. The `for` loop

A `for` loop allows you to iterate over a sequence of values.

```ne
for number in range(5) {
    print(number)
}
```

Output:

```text
0
1
2
3
4
```

## 3. The `break` statement

The `break` statement immediately exits the current loop.

```ne
var count = 0

while count < 10 {
    if count == 5 {
        break
    }

    print(count)
    count = count + 1
}
```

Output:

```text
0
1
2
3
4
```

## 4. The `continue` statement

The `continue` statement skips the current iteration and moves to the next one.

```ne
for number in range(5) {
    if number == 2 {
        continue
    }

    print(number)
}
```

Output:

```text
0
1
3
4
```

## 5. Nested loops

You can place one loop inside another loop.

```ne
for row in range(3) {
    for column in range(2) {
        print(row)
        print(column)
    }
}
```

## Next steps

- [Conditions](conditions.md)
- [Functions](functions.md)
- [Collections](collections.md)
- [Documentation Home](README.md)

---

[Back to NEXTHON](https://github.com/Nexform-star/NEXTHON)
