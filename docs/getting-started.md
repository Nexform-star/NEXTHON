# Getting Started

Welcome to NEXTHON!

This guide will help you write and run your first NEXTHON program.

## 1. Create your first program

Create a new file named:

```text
hello.ne
```

Add the following instructions:

```ne
print("Hello, World!")
```

Save the file.

## 2. Run your program

Open PowerShell or Command Prompt in the directory containing your file.

Run:

```powershell
nexthon hello.ne
```

Expected output:

```text
Hello, World!
```

Congratulations! You have executed your first NEXTHON program.

## 3. Create variables

Variables allow you to store information.

Use the `var` keyword to declare a variable:

```ne
var name = "Nexform"
var age = 16

print(name)
print(age)
```

Output:

```text
Nexform
16
```

## 4. Perform calculations

NEXTHON supports arithmetic operations.

```ne
var firstNumber = 20
var secondNumber = 10

print(firstNumber + secondNumber)
print(firstNumber - secondNumber)
print(firstNumber * secondNumber)
print(firstNumber / secondNumber)
```

Output:

```text
30
10
200
2
```

## 5. Modify variables

You can change the value of a variable after declaring it.

```ne
var score = 100

score = score + 50

print(score)
```

Output:

```text
150
```

## 6. Your first challenge

Now it's your turn!

Create a program that:

1. Declares a variable named `player` containing your username.
2. Declares a variable named `score` containing `100`.
3. Declares a variable named `bonus` containing `50`.
4. Adds the bonus to the score.
5. Prints the player's name and final score.

Expected final score:

```text
150
```

## Next steps

Continue learning NEXTHON:

- [Variables](variables.md)
- [Data Types](data-types.md)
- [Operators](operators.md)
- [Language Syntax](syntax.md)
- [Documentation Home](README.md)

---

[Back to NEXTHON](https://github.com/Nexform-star/NEXTHON)
