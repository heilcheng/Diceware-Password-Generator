
import random
import requests

def load_word_list(url):
    response = requests.get(url)
    lines = response.text.split('\n')
    word_list = {}
    for line in lines:
        parts = line.split()
        if len(parts) == 2 and parts[0].isdigit():
            word_list[parts[0]] = parts[1]
    return word_list

def roll_dice():
    return str(random.randint(1, 6))

def generate_password(num_words, word_list):
    password_words = []
    for _ in range(num_words):
        dice_rolls = "".join(roll_dice() for _ in range(5))
        password_words.append(word_list[dice_rolls])
    return ' '.join(password_words)

word_list = load_word_list('https://theworld.com/~reinhold/diceware.wordlist.asc')
num_words = int(input("Enter the number of words you want in your password (1 to 7776): "))
print(generate_password(num_words, word_list))