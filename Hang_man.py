import random
# Hangman figure parts
hangman_parts = [
    " O ",  # Head
    "/|\\",  # Body
    " | ",  # Torso
    "/ \\"  # Legs
]
def display_hangman(attempts):
    for i in range(attempts, 4):  # Show remaining body parts
        print(hangman_parts[i])

def play_hangman():
    words = ["APPLE", "PYTHON", "TABLE", "LAPTOP"]  # Word choices
    word = random.choice(words)  # Player 1 (Agent) chooses a word
    guessed_word = ["_"] * len(word)
    attempts = 4  # Max body parts

    print("Welcome to Hangman!")
    
    while attempts > 0 and "_" in guessed_word:
        print("\nWord:", " ".join(guessed_word))
        display_hangman(attempts)
        
        guess = input("Player 2, guess a letter: ").upper()
        
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            if attempts < 4:  # Remove a body part for a correct guess
                attempts += 1  
        else:
            attempts -= 1  # Wrong guess → Add body part
        
        if "_" not in guessed_word:
            print("\nCongratulations! You guessed the word:", word)
            return
        
    print("\nGame Over! The word was:", word)
    display_hangman(attempts)

play_hangman()
