# Collections

Collections allow you to store multiple values in a single variable.

NEXTHON supports lists, tuples, dictionaries and sets.

## 1. Lists

Lists are ordered collections of values.

```ne
var languages = ["NEXTHON", "Python", "JavaScript"]

print(languages)
```

### Accessing elements

List indexes start at `0`.

```ne
var languages = ["NEXTHON", "Python", "JavaScript"]

print(languages[0])
print(languages[1])
```

### Modifying lists

Lists support methods for modifying their contents.

```ne
var numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

### Removing elements

```ne
var numbers = [10, 20, 30]

numbers.remove(20)

print(numbers)
```

## 2. Tuples

Tuples are ordered collections of values.

```ne
var coordinates = (10, 20)

print(coordinates)
print(coordinates[0])
```

## 3. Dictionaries

Dictionaries store values using key-value pairs.

```ne
var player = {
    "name": "Nexform",
    "score": 100
}

print(player["name"])
print(player["score"])
```

### Modifying dictionaries

```ne
var player = {
    "name": "Nexform",
    "score": 100
}

player["score"] = 150

print(player["score"])
```

## 4. Sets

Sets store unique values.

```ne
var numbers = {1, 2, 3}

print(numbers)
```

## 5. Collection length

Use `len()` to get the number of elements in a collection.

```ne
var languages = ["NEXTHON", "Python", "JavaScript"]

print(len(languages))
```

Output:

```text
3
```

## Next steps

- [Data Types](data-types.md)
- [Modules](modules.md)
- [Built-in Functions](built-in-functions.md)
- [Documentation Home](README.md)

---

[Back to NEXTHON](https://github.com/Nexform-star/NEXTHON)
