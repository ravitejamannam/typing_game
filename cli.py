import time
import click
import random


# Difficulty level dictionary
difficulty_levels = {
    'easy': [
        "The quick brown fox",
        "Jumps over the lazy dog",
        "Hello world"
    ],
    'medium': [
        "Python is a powerful programming language",
        "I enjoy solving coding challenges",
        "The weather is nice today, isn't it?"
    ],
    'hard': [
        "Supercalifragilisticexpialidocious",
        "Pneumonoultramicroscopicsilicovolcanoconiosis",
        "Floccinaucinihilipilification"
    ]
}

# Function to calculate words per minute
def calculate_wpm(start_time, end_time, typed_text, original_text):
    time_taken = end_time - start_time
    word_count = len(typed_text.split())  # Count words
    wpm = (word_count / time_taken) * 60  # Words per minute
    return wpm

def get_sentence_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return random.choice(lines).strip()

#use the function to get a random sentence from typing_tests.txt
filename = 'random_sentence.py'
random_sentence = get_sentence_from_file(filename)
print(random_sentence)


# Function to get a random sentence based on difficulty
def get_sentence(difficulty):
    if difficulty not in difficulty_levels:
        raise ValueError("Invalid difficulty level. Choose from 'easy', 'medium', or 'hard'.")
    
    return random.choice(difficulty_levels[difficulty])

@click.command()
@click.option('--difficulty', default='easy', help="Choose the difficulty level: easy, medium, or hard")
def type_test(difficulty):
    """A typing test with different difficulty levels and WPM calculation."""
    print(f"Starting a {difficulty} typing test...\n")
    
    # Get the sentence for the chosen difficulty
    sentence = get_sentence(difficulty)
    print(f"Type this text:\n{sentence}\n")
    input("Press Enter to start...")

    start_time = time.time()  # Start the timer
    typed_text = input("Start typing: ")
    end_time = time.time()  # End the timer

    # Check if the typed text matches the sentence
    if typed_text == sentence:
        wpm = calculate_wpm(start_time, end_time, typed_text, sentence)
        print(f"Correct! You typed it in {end_time - start_time:.2f} seconds.")
        print(f"Your typing speed is {wpm:.2f} words per minute.")
    else:
        print("Incorrect text. Please try again!")

if __name__ == '__main__':
    type_test()
