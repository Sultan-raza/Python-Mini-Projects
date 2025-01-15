import random

# List of words for the game
words = ["python", "hangman", "challenge", "programming", "quiz"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to display the word with guessed letters
def display_word(word, guessed_letters):
    return "Word: " + " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Function to implement the Hangman game
def hangman():
    word = choose_word()
    attempts = 15
    guessed_letters = set()
    correct_letters = set(word)
    
    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))
    
    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()
        
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input, please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You have already guessed the letter '{guess}'. Try again.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in correct_letters:
            print(f"Great job! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Incorrect! '{guess}' is not in the word. Attempts left: {attempts}.")
        
        current_display = display_word(word, guessed_letters)
        print(current_display)
        
        if "_" not in current_display:
            print("Congratulations! You guessed the word!")
            break
    else:
        print(f"Game Over! The word was '{word}'.")

if __name__ == "__main__":
    hangman()
