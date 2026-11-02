# Collections

NEXTHON supports several collection types for storing multiple values.

## 1. Lists

Lists store multiple values in an ordered collection.

```ne
var numbers = [10, 20, 30, 40]

print(numbers)
```

### Accessing elements

Use an index to access an element. Indexes start at `0`.

```ne
var numbers = [10, 20, 30]

print(numbers[0])
print(numbers[1])
```

Output:

```text
10
20
```

### List methods

Lists support methods such as `append()` and `remove()`.

```ne
var numbers = [10, 20, 30]

numbers.append(40)
print(numbers)

numbers.remove(20)
print(numbers)
```

## 2. Tuples

Tuples store multiple values in an ordered collection.

```ne
var coordinates = (10, 20)

print(coordinates)
print(coordinates[0])
```

Output:

```text
(10, 20)
10
```

## 3. Dictionaries

Dictionaries store values using key-value pairs.

```ne
var player = {
    "name": "Nexform",
    "score": 150
}

print(player["name"])
print(player["score"])
```

### Updating dictionary values

You can update a value using its key.

```ne
var player = {
    "name": "Nexform",
    "score": 150
}

player["score"] = 200

print(player["score"])
```

Output:

```text
200
```

## 4. Sets

Sets store unique values.

Create a set using the `set()` built-in function.

```ne
var numbers = set([1, 2, 3])

print(numbers)
```

## 5. Collection length

Use the `len()` built-in function to get the number of elements in a collection.

```ne
var numbers = [10, 20, 30]

print(len(numbers))
```

Output:

```text
3
```

## Next steps

- [Data Types](data-types.md)
- [Built-in Functions](built-in-functions.md)
- [Functions](functions.md)
- [Documentation Home](README.md)

---

[Back to NEXTHON](https://github.com/Nexform-star/NEXTHON)
