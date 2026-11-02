# Data Types

NEXTHON supports several data types that allow you to store and work with different kinds of values.

## 1. Integers

Integers are whole numbers without decimal places.

```ne
var age = 16
var score = 100
var temperature = -5

print(age)
print(score)
print(temperature)
```

## 2. Floats

Floats are numbers that contain decimal places.

```ne
var price = 19.99
var average = 15.5

print(price)
print(average)
```

## 3. Strings

Strings are sequences of characters enclosed in quotation marks.

```ne
var username = "Nexform"
var message = "Welcome to NEXTHON!"

print(username)
print(message)
```

## 4. Booleans

Booleans represent one of two values: `True` or `False`.

```ne
var is_active = True
var is_admin = False

print(is_active)
print(is_admin)
```

## 5. Lists

Lists store multiple values in an ordered collection.

```ne
var numbers = [10, 20, 30]
var names = ["Alice", "Bob", "Charlie"]

print(numbers)
print(names)
```

## 6. Tuples

Tuples are ordered collections of values.

```ne
var coordinates = (10, 20)

print(coordinates)
```

## 7. Dictionaries

Dictionaries store values using key-value pairs.

```ne
var player = {
    "name": "Nexform",
    "score": 150
}

print(player)
```

## 8. Sets

Sets store unique values.

Create a set using the `set()` built-in function.

```ne
var numbers = set([1, 2, 3])

print(numbers)
```

## 9. None

`None` represents the absence of a value.

```ne
var result = None

print(result)
```

## 10. Checking data types

Use the `type()` built-in function to identify a value's type.

```ne
var name = "Nexform"
var age = 16
var active = True

print(type(name))
print(type(age))
print(type(active))
```

Output:

```text
str
int
bool
```

## Next steps

- [Variables](variables.md)
- [Operators](operators.md)
- [Collections](collections.md)
- [Documentation Home](README.md)

---

[Back to NEXTHON](https://github.com/Nexform-star/NEXTHON)
