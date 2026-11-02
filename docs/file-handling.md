# File Handling

NEXTHON provides built-in functions to read, write, append to, and check files.

## 1. Writing to a File

Use `write_file()` to create a file or replace its existing content.

```ne
write_file("example.txt", "Hello from NEXTHON")

print("File written")
```

## 2. Reading a File

Use `read_file()` to retrieve the content of a file.

```ne
var content = read_file("example.txt")

print(content)
```

Output:

```text
Hello from NEXTHON
```

## 3. Appending to a File

Use `append_file()` to add content to the end of an existing file.

```ne
append_file("example.txt", "\nSecond line")

print(read_file("example.txt"))
```

Output:

```text
Hello from NEXTHON
Second line
```

## 4. Checking if a File Exists

Use `exists()` to check whether a file exists.

```ne
var file_found = exists("example.txt")

print(file_found)
```

Output:

```text
True
```

## 5. Complete Example

The following example demonstrates basic file operations.

```ne
var filename = "notes.txt"

write_file(filename, "My first NEXTHON note")

append_file(filename, "\nLearning file handling")

var content = read_file(filename)

print(content)
print(exists(filename))
```

## Next steps

- [Built-in Functions](built-in-functions.md)
- [Variables](variables.md)
- [Documentation Home](README.md)

---

[Back to NEXTHON](https://github.com/Nexform-star/NEXTHON)
