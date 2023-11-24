#hangman
import random

#hangman word list

word_list= ["python", "java", "javascript", "php"]

def choose_word():
    return random.choice(word_list)

#game code

def play_hangman():
    while True:
        print('Hangman')
        choice = input('Type "play" to play the game, "exit" to quit: > ')

print('HANGMAN')