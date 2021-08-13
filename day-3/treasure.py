print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You wake in a hall way, there's 2 ways out.")

def game_over():
    print("Game Over")
    exit()

first_choice = input("Which way do you go? Left or Right? ").lower()

if first_choice == "right":
    print("Theres a hole in the floor.....")
    print("...with spikes")
    game_over()
else:
    print("Your enter into a room, theres a pool of water and a door on the other side.")

print("You're hesitant, the door is open but you would have to swim across.")

second_choice = input("Swim across? or Look around? (swim or look) ")

if second_choice == "swim":
    print("You jump in the water...")
    print("Tentacles fly out and wrap themselves around you and the last thing you see are the bubbles floating to the surface....")
    game_over()
else:
    print("Your hesitance proves useful...")
    print("A bridge drops down and you quickly run across")

print("When you get to the other side you see 2 other doors...")
print("Each door is a different color...red, yellow, and blue")
last_choice = input("Which door do you choose? Red? Blue? or Yellow? ").lower()
if last_choice == "yellow":
    print("You go through the door...")
    print("You're outside now, you made it out.")
    print("Congratulations")
    exit()
else:
    print("WRONG DOOR!")
    print("....")
    game_over()
