import random

# A list of words used in guessing game
wordList = [
    "New World",
    "Hearts of Iron",
    "Guild Wars 2",
    "World of Warcraft",
    "Diablo IV"
]

def main():
    # A little introduction to game
    name = input("What's your name?: ")
    print(f"Welcome {name}.\nLet's Play a word guessing game!\nYou need to type singular characters of the word in correct order.\nWords are case insensitive.\n\nGood Luck!")
    
    # Picking a random word from wordlist
    word = wordList[random.randint(0, len(wordList) - 1)].lower()
    guessedChars = []
    for char in word:
            if char != " ":
                guessedChars.append("-")
            else:
                guessedChars.append(" ")

    missedChars = 0
    whichChar = 0
    while True:
        # Print the word layout
        for v in guessedChars:
            print(v)

        # If the character is space - skip
        if word[whichChar] == " ":
            whichChar += 1
            continue
        
        # Waits for player character guess
        inChar = input("insert character: ").lower()

        # If player guess is correct, guessedChars list updates, and the word index (whichChar) increases by 1
        if inChar == word[whichChar]:
             guessedChars[whichChar] = inChar
             whichChar += 1
        # If it's incorrect it updates mistakes count
        else:
             missedChars += 1

        # If word index is same as length of word, player won
        if whichChar == len(word):
            for v in guessedChars:
                print(v)
            break
             
    # Game finishes after successful attempt of guessing the whole word
    print(f"The word was {word}. You won! You made {missedChars} mistakes")

main()