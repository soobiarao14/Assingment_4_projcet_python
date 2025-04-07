
import random

def get_word():
    words = ["computer", "science", "keyboard", "monitor", "internet"]
    return random.choice(words).upper()

def display(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = get_word()
    guessed_letters = set()
    attempts = 6  # Maximum wrong guesses allowed

    print("Welcome to Hangman!")
    print("created by sobiarao")
    
    while attempts > 0:
        print("\nWord: ", display(word, guessed_letters))
        guess = input("Guess a letter: ").upper()
        
        if guess in guessed_letters:
            print("Warning: You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Correct guess! Keep going!")
            if set(word) <= guessed_letters:
                print(f"🎉 Congratulations! You guessed the word: {word}")
                return
        else:
            attempts -= 1
            print(f"❌ Wrong guess, try again! {attempts} attempts left.")
    
    print(f"💀 Game over! The word was: {word}")

# Run the game
hangman()
