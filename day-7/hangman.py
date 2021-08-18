import random
from os import system, name
from time import sleep

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

word_list = ["ardvark", "baboon", "camel"]

display = []

chosen_word = random.choice(word_list)

for _ in chosen_word:
    display += "_"


end_of_game = False
lives = 6

while not end_of_game:
    print(f"{' '.join(display)}")
    print(stages[lives])
    if lives != 0:
        guess = input("Guess a letter: ").lower()
        if guess in display:
            print("Already chose that letter. Try again.")
            sleep(2)
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        if guess not in chosen_word:
            lives -= 1
            print(lives)
        if "_" not in display:
            end_of_game = True
            print(f"{' '.join(display)}")
            print("Congrats, you won!")
        clear()
    else:
        print("You lose!")
        print(f"The correct word is {chosen_word}")
        break
        
