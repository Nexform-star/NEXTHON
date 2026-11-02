var first = float(input("First number: "))
var operation = int(input("Operation (1=+, 2=-, 3=*, 4=/): "))
var second = float(input("Second number: "))

if operation == 1 {
    print(first + second)
} elif operation == 2 {
    print(first - second)
} elif operation == 3 {
    print(first * second)
} elif operation == 4 {
    if second == 0 {
        print("Cannot divide by zero.")
    } else {
        print(first / second)
    }
} else {
    print("Unknown operation.")
}
