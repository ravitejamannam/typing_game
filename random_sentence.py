import time
import random
from colorama import Fore, Back, Style, init
from termcolor import colored
from difflib import SequenceMatcher

# Initialize colorama
init(autoreset=True)

# Your sentences list here (use the same list from your original code)
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A comprehensive understanding of the natural world enables humans to make informed decisions regarding conservation efforts and biodiversity protection.",
    "The swirling winds carried the scent of freshly baked bread through the bustling streets of the quaint town nestled in the valley.",
    "After months of research and testing, the scientists finally unveiled their groundbreaking invention designed to revolutionize renewable energy sources worldwide.",
    "As the clock struck midnight, the city was bathed in the soft glow of streetlights, casting long shadows on the empty sidewalks where only the echoes of distant footsteps remained.",
    "She gazed at the night sky, captivated by the twinkling stars and the faint silhouette of the moon as it hung low over the horizon, a silent witness to the passage of time.",
    "The once quiet library now hummed with activity as students pored over their textbooks, furiously scribbling notes in a desperate attempt to finish their assignments before the looming deadline.",
    "With the arrival of spring, the fields bloomed with vibrant colors as flowers of every shade and hue stretched toward the sun, signaling the start of a new cycle of life.",
    "The novel was a masterful blend of mystery, adventure, and romance, weaving together multiple plotlines that kept the reader hooked until the final, unexpected twist.",
    "In a world where technology is constantly evolving, it becomes increasingly important to strike a balance between progress and maintaining our connection to the natural environment.",
    "The bustling city streets were filled with the sounds of honking cars, clattering coffee cups, and the distant chatter of pedestrians, all moving in sync with the rhythm of urban life.",
    "Despite the challenges they faced, the determined explorers pressed on through the dense jungle, driven by the hope of discovering an ancient civilization lost to time.",
    "At the heart of the forest, a serene pond reflected the surrounding trees like a giant mirror, its still surface broken only by the occasional ripple from a passing breeze.",
    "The old wooden cabin by the lake had stood the test of time, its weathered exterior telling the story of countless seasons and memories created by generations of families.",
    "As the sun dipped below the mountains, casting a golden hue across the valley, the campers gathered around the campfire, sharing stories of their adventures under the starlit sky.",
    "The fast-paced world of finance is filled with volatility, uncertainty, and risk, demanding constant vigilance and the ability to make quick, calculated decisions that could lead to great rewards or catastrophic losses.",
    "Her heart raced as she navigated the maze of narrow alleyways, the sound of footsteps behind her growing louder as the figure in the shadows closed the distance.",
    "The artist stood in front of the blank canvas, brush in hand, contemplating the swirling colors and shapes that would soon take form in a masterpiece that would captivate audiences for generations to come.",
    "With each passing day, the city grew taller and more crowded, its skyline a testament to the relentless pursuit of progress, as towering skyscrapers emerged to replace the quaint buildings of the past.",
    "The historian spent years painstakingly piecing together fragments of ancient manuscripts, uncovering lost knowledge that had been buried beneath centuries of dust and neglect."
]


# Function to calculate accuracy
def calculate_accuracy(original_text, typed_text):
    return SequenceMatcher(None, original_text, typed_text).ratio() * 100

# Function to calculate words per minute (WPM)
def calculate_wpm(start_time, end_time, typed_text):
    time_taken = end_time - start_time
    word_count = len(typed_text.split())
    wpm = (word_count / time_taken) * 60
    return wpm

# Function to get a random sentence
def get_sentence():
    return random.choice(sentences)

# Function to display progress bar
def progress_bar(progress, total):
    bar_length = 30
    filled_length = int(bar_length * progress // total)
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    return f'|{bar}| {progress}/{total}'

# Improved typing test function
def typing_test():
    total_tests = 60
    test_count = 0
    total_wpm = 0
    total_accuracy = 0

    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.YELLOW}*** Welcome to the Advanced Typing Speed Test! ***")
    print(f"{Fore.YELLOW}>>> Let's improve your typing skills! <<<")
    print(f"{Fore.CYAN}{'='*60}\n")

    while test_count < total_tests:
        sentence = get_sentence()
        
        # Clear some space
        print("\n" * 2)
        
        # Show progress
        print(f"{Fore.BLUE}{progress_bar(test_count, total_tests)}")
        print(f"\n{Fore.MAGENTA}Test {test_count + 1}/{total_tests}")
        print(f"\n{Fore.WHITE}Type this sentence:")
        print(f"{Fore.YELLOW}{sentence}\n")

        input(f"{Fore.GREEN}Press Enter when ready to start typing...{Style.RESET_ALL}")
        
        start_time = time.time()
        typed_text = input(f"{Fore.CYAN}> ")
        end_time = time.time()

        # Calculate metrics
        wpm = calculate_wpm(start_time, end_time, typed_text)
        accuracy = calculate_accuracy(sentence, typed_text)
        time_taken = end_time - start_time

        # Update totals
        total_wpm += wpm
        total_accuracy += accuracy

        # Display results with colorful feedback
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.WHITE}Results for Test {test_count + 1}:")
        print(f"{Fore.GREEN}Speed: {wpm:.2f} WPM")
        print(f"{Fore.YELLOW}Accuracy: {accuracy:.2f}%")
        print(f"{Fore.MAGENTA}Time: {time_taken:.2f} seconds")
        
        # Performance feedback
        if accuracy >= 95:
            print(f"{Fore.GREEN}Excellent accuracy!")
        elif accuracy >= 85:
            print(f"{Fore.YELLOW}Good accuracy, keep practicing!")
        else:
            print(f"{Fore.RED}Focus on accuracy over speed")

        if wpm >= 60:
            print(f"{Fore.GREEN}Great speed!")
        elif wpm >= 40:
            print(f"{Fore.YELLOW}Good speed, keep it up!")
        else:
            print(f"{Fore.RED}Focus on maintaining a steady pace")
            
        print(f"{Fore.CYAN}{'='*60}")

        test_count += 1
        time.sleep(1)  # Brief pause between tests

    # Final results
    avg_wpm = total_wpm / total_tests
    avg_accuracy = total_accuracy / total_tests
    
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.YELLOW}*** Congratulations! You've completed all tests! ***")
    print(f"\n{Fore.WHITE}Final Statistics:")
    print(f"{Fore.GREEN}Average Speed: {avg_wpm:.2f} WPM")
    print(f"{Fore.YELLOW}Average Accuracy: {avg_accuracy:.2f}%")
    print(f"{Fore.CYAN}{'='*60}\n")

if __name__ == '__main__':
    typing_test()
