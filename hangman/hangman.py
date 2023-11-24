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

        if choice =="play":
            secret_word = choose_word()
            guessed_word = ["_"] * len(secret_word)
            attempts = 8 #number of attempts
            guessed_letters = [] #list of letters already guessed

            print('Welcome to the game!')

            while attempts > 0:
                print("".join(guessed_word))
                guess = input("Input a letter : > ").lower()
