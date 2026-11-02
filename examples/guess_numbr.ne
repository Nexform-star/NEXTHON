var secret = int(random() * 10) + 1
var guess = 0

print("Guess the number between 1 and 10!")

while guess != secret {
    guess = int(input("Your guess: "))

    if guess < secret {
        print("Too low!")
    } elif guess > secret {
        print("Too high!")
    } else {
        print("Correct! You win!")
    }
}
