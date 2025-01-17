import random
import nltk
from nltk.corpus import words

# Download the words corpus if not already downloaded
nltk.download("words")

# Create a sequence of English words
english_words = words.words()

# Define difficulty ranges
difficulty_ranges = {
    "easy": (4, 6),
    "medium": (7, 8),
    "hard": (9, 10)
}

def filter_words(min_len, max_len):
    """Filter words based on length."""
    return [word.lower() for word in english_words if min_len <= len(word) <= max_len]

def provide_hint(word):
    """Provide a hint for words longer than 7 characters."""
    return f"The word starts with '{word[0]}' and ends with '{word[-1]}'."


def play_round(total_score):
    """Play a single round of Word Jumble."""
    # Choose difficulty
    while True:
        difficulty = input("Choose a difficulty (easy, medium, hard): ").lower()
        if difficulty in difficulty_ranges:
            break
        print("Invalid difficulty. Please choose 'easy', 'medium', or 'hard'.")

    min_len, max_len = difficulty_ranges[difficulty]
    WORDS = filter_words(min_len, max_len)

    # Pick a random word
    word = random.choice(WORDS)
    correct = word

    # Create a jumbled version of the word
    jumble = ""
    temp_word = word
    while temp_word:
        position = random.randrange(len(temp_word))
        jumble += temp_word[position]
        temp_word = temp_word[:position] + temp_word[(position + 1):]

    print(f"\nThe jumble is: {jumble}")

    # Provide a hint for longer words
    if len(word) > 7:
        print(f"Hint: {provide_hint(word)}")

    # Start guessing
    attempts = 6
    while attempts > 0:
        print(f"Remaining attempts: {attempts}")
        guess = input("Your guess: ").lower()
        if guess == correct:
            print(f"That's it! You guessed it!\n")
            total_score += attempts  # Add remaining attempts to total score
            print(f"Your total score is now: {total_score}")
            break
        else:
            print("Sorry, that's not it.")
            attempts -= 1

    if attempts == 0:
        print(f"You've run out of tries. The correct word was: {correct}\n")

    return total_score


def main():
    """Main game loop."""
    total_score = 0

    while True:
        print("\nStarting a new round!")
        total_score = play_round(total_score)

        # Ask if the player wants to play again
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing! Your final total score is:", total_score)
            break


if __name__ == "__main__":
    main()
