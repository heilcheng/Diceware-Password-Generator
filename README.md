# Diceware Password Generator

This script generates a secure password using the Diceware method. 

## How It Works

The Diceware method involves rolling a six-sided dice five times to generate a five-digit number. Each number corresponds to a word in the Diceware word list. The script repeats this process for the number of words you want in your password.

The Diceware word list used in this script is sourced from `https://theworld.com/~reinhold/diceware.wordlist.asc`. This is a widely used word list for the Diceware method, created by Arnold G. Reinhold.

## Usage

1. Run the script with Python 3: `python3 Diceware.py`
2. When prompted, enter the number of words you want in your password. You can choose any number between 1 and 7776.

## Requirements

This script requires the `requests` module to download the Diceware word list. You can install it with `pip`: `pip install requests`

## Note

The passwords generated by this script are designed to be strong and memorable, but you should still keep them secure. Don't use the same password for multiple services, and consider using a password manager to keep track of your passwords.