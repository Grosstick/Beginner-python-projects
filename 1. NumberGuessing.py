import random

### Guessing game

# Main function
def main():

    # user sets up a range
    while True:
        try:
            firstNum = input("Enter first number in a range: ")
        except ValueError:
            print("Invalid input! Try again.")
            continue
        else:
            try:
                firstNum = int(firstNum)
            except ValueError:
                print("Your input is not an integer! Try again.")
                continue
        break

    while True:
        try:
            secondNum = input("Enter second number in a range: ")
        except ValueError:
            print("Invalid input! Try again.")
            continue
        else:
            try:
                secondNum = int(secondNum)
            except ValueError:
                print("Your input is not an integer! Try again.")
                continue
        break

    # program presents a set range
    print(f"You range is: {firstNum}-{secondNum}")

    # program chooses a random number in range
    randomNum = random.randint(firstNum, secondNum)

    # program notifies that random number was chosen
    print("Random number was chosen")

    # guessing process, program loops until correct answer is found
    guessTries = 0
    while True:
        guessTries += 1
        # check for valid input
        while True:
            try:
                guessNumber = input("Enter your guess: ")
            except ValueError:
                print("Invalid input! Try again.")
                continue
            else:
                try:
                    guessNumber = int(guessNumber)
                except ValueError:
                    print("Your input is not an integer! Try again.")
                    continue
            break
        # if correct break loop
        if guessNumber == randomNum: break
        # notify if user needs to guess higher or lower
        elif guessNumber > randomNum:
            print("It's not the correct number :( You need to guess lower numbers!")
        else:
            print("It's not the correct number :( You need to guess higher numbers!")

    # user is notified about successful answer
    print(f"Congratulations! You guessed the right number! It took you {guessTries} tries to succeed. number was {randomNum}")

main()