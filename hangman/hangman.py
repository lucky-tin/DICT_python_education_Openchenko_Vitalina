#hangman
import random

#hangman word list

word_list= ["python", "java", "javascript", "php"]

def choose_word():
    return random.choice(word_list)

print('HANGMAN')