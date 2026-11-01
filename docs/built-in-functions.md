# Built-in Functions

NEXTHON provides built-in functions that can be used directly in your programs.

These functions cover common operations such as displaying output, converting values, working with collections and handling files.

## 1. Input and Output

| Function | Description |
|---|---|
| `print()` | Displays a value |
| `input()` | Reads user input |

Example:

```ne
print("Hello, World!")

var username = input("Enter your name: ")
print(username)
```

## 2. Type Conversion

| Function | Description |
|---|---|
| `str()` | Converts a value to a string |
| `int()` | Converts a value to an integer |
| `float()` | Converts a value to a floating-point number |
| `bool()` | Converts a value to a boolean |

Example:

```ne
var number = "42"

print(int(number))
print(float(number))
print(str(100))
print(bool(1))
```

## 3. Type Information

| Function | Description |
|---|---|
| `type()` | Returns the type of a value |

Example:

```ne
var username = "Nexform"

print(type(username))
```

## 4. Mathematical Functions

| Function | Description |
|---|---|
| `abs()` | Returns the absolute value |
| `round()` | Rounds a number |
| `min()` | Returns the smallest value |
| `max()` | Returns the largest value |
| `sum()` | Calculates the sum of values |
| `sqrt()` | Calculates the square root |

Example:

```ne
print(abs(-10))
print(round(3.14159, 2))
print(min(10, 20, 30))
print(max(10, 20, 30))
print(sum([10, 20, 30]))
print(sqrt(25))
```

## 5. Collection Functions

| Function | Description |
|---|---|
| `len()` | Returns the number of elements |
| `list()` | Creates a list |
| `tuple()` | Creates a tuple |
| `dict()` | Creates a dictionary |
| `set()` | Creates a set |
| `sorted()` | Returns sorted values |
| `reversed()` | Returns values in reverse order |
| `enumerate()` | Returns indexed values |
| `range()` | Generates a sequence of numbers |

Example:

```ne
var numbers = [3, 1, 2]

print(len(numbers))
print(sorted(numbers))
print(list(reversed(numbers)))
```

## 6. Random and Time Functions

| Function | Description |
|---|---|
| `random()` | Generates a random value |
| `time()` | Returns the current time value |

Example:

```ne
print(random())
print(time())
```

## 7. Program Control

| Function | Description |
|---|---|
| `exit()` | Stops program execution |

Example:

```ne
print("Program started")

exit()

print("This message should not appear")
```

## 8. JSON Functions

NEXTHON provides functions for encoding and decoding JSON data.

| Function | Description |
|---|---|
| `json_encode()` | Converts a value into JSON |
| `json_decode()` | Converts JSON into a NEXTHON value |

Example:

```ne
var data = {
    "name": "Nexform",
    "score": 100
}

var json = json_encode(data)

print(json)
print(json_decode(json))
```

## 9. File Functions

NEXTHON provides built-in functions for basic file operations.

| Function | Description |
|---|---|
| `read_file()` | Reads a file |
| `write_file()` | Writes content to a file |
| `append_file()` | Appends content to a file |
| `file_exists()` | Checks whether a file exists |

Example:

```ne
write_file("example.txt", "Hello from NEXTHON!")

var content = read_file("example.txt")

print(content)
print(file_exists("example.txt"))
```

## Next steps

- [File Handling](file-handling.md)
- [Collections](collections.md)
- [Exceptions](exceptions.md)
- [Documentation Home](README.md)

---

[Back to NEXTHON](https://github.com/Nexform-star/NEXTHON)
