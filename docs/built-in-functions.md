# Built-in Functions

NEXTHON provides several built-in functions to simplify common programming tasks.

## 1. Output

### `print()`

Displays a value in the console.

```ne
print("Hello, World!")
print(42)
```

## 2. User Input

### `input()`

Reads input from the user.

```ne
var name = input("Enter your name: ")
print(name)
```

## 3. Type Conversion

NEXTHON provides functions to convert values between types.

| Function | Description |
|---|---|
| `str()` | Converts a value to a string |
| `int()` | Converts a value to an integer |
| `float()` | Converts a value to a float |
| `bool()` | Converts a value to a boolean |

Example:

```ne
var number = int("42")
var price = float("19.99")
var message = str(100)

print(number)
print(price)
print(message)
```

## 4. Type Information

### `type()`

Returns the type of a value.

```ne
var name = "Nexform"

print(type(name))
```

## 5. Mathematical Functions

| Function | Description |
|---|---|
| `abs()` | Returns the absolute value |
| `round()` | Rounds a number |
| `min()` | Returns the smallest value |
| `max()` | Returns the largest value |
| `sum()` | Returns the sum of values |
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

## 6. Collection Functions

| Function | Description |
|---|---|
| `len()` | Returns the number of elements |
| `list()` | Creates a list |
| `tuple()` | Creates a tuple |
| `dict()` | Creates a dictionary |
| `set()` | Creates a set |
| `sorted()` | Returns a sorted collection |
| `reversed()` | Returns a reversed collection |
| `enumerate()` | Returns indexed elements |
| `range()` | Generates a sequence of numbers |

Example:

```ne
var numbers = [3, 1, 2]

print(len(numbers))
print(sorted(numbers))
print(list(reversed(numbers)))
```

## 7. Random and Time Functions

| Function | Description |
|---|---|
| `random()` | Generates a random number |
| `time()` | Returns the current timestamp |

Example:

```ne
print(random())
print(time())
```

## 8. JSON Functions

| Function | Description |
|---|---|
| `json_encode()` | Converts a value to JSON |
| `json_decode()` | Parses JSON data |

Example:

```ne
var player = {"name": "Nexform", "score": 150}

var data = json_encode(player)

print(data)
print(json_decode(data))
```

## 9. File Functions

| Function | Description |
|---|---|
| `read_file()` | Reads a file |
| `write_file()` | Writes content to a file |
| `append_file()` | Adds content to a file |
| `exists()` | Checks whether a file exists |

Example:

```ne
write_file("example.txt", "Hello from NEXTHON")

print(read_file("example.txt"))
print(exists("example.txt"))
```

## 10. Program Control

### `exit()`

Stops program execution.

```ne
exit()
```

## Next steps

- [File Handling](file-handling.md)
- [Collections](collections.md)
- [Functions](functions.md)
- [Documentation Home](README.md)

---

[Back to NEXTHON](https://github.com/Nexform-star/NEXTHON)
