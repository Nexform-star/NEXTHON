# File Handling

File handling allows NEXTHON programs to read and write data stored in files.

NEXTHON provides built-in functions for basic file operations.

## 1. Writing to a file

Use `write_file()` to create a file or replace its existing content.

```ne id="q7m3kf"
write_file("example.txt", "Hello from NEXTHON!")
```

## 2. Reading a file

Use `read_file()` to retrieve the content of a file.

```ne id="w4n8jx"
var content = read_file("example.txt")

print(content)
```

Output:

```text id="p2z6vb"
Hello from NEXTHON!
```

## 3. Appending to a file

Use `append_file()` to add content to the end of an existing file.

```ne id="m9r5yc"
append_file("example.txt", "\nWelcome to NEXTHON!")
```

Reading the file again:

```ne id="t6k2qa"
var content = read_file("example.txt")

print(content)
```

## 4. Checking whether a file exists

Use `file_exists()` to check whether a file is available.

```ne id="x3j8wd"
if file_exists("example.txt") {
    print("File found!")
} else {
    print("File not found.")
}
```

## 5. Complete example

The following program demonstrates basic file operations.

```ne id="h5v1zn"
var filename = "player.txt"

write_file(filename, "Nexform")

append_file(filename, "\nScore: 150")

if file_exists(filename) {
    var content = read_file(filename)
    print(content)
}
```

Expected output:

```text id="u8p4lm"
Nexform
Score: 150
```

## Important notes

- `write_file()` replaces existing file content.
- `append_file()` adds content to the end of a file.
- `read_file()` returns the file content.
- `file_exists()` checks whether a file exists.

## Next steps

- [Built-in Functions](built-in-functions.md)
- [Modules](modules.md)
- [Documentation Home](README.md)

---

[Back to NEXTHON](https://github.com/Nexform-star/NEXTHON)
