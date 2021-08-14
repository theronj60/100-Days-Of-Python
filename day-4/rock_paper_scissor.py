import random

choices = ["rock", "paper", "scissors"]
user_choice = input("Rock, Paper or Scissors? ").lower()
computer_choice = random.choice(choices)


def user_win():
    print("User wins!")
    quit()

def computer_win():
    print("Computer wins!")
    quit()

while user_choice not in choices:
    print("Please type paper, rock, or scissors...")
    user_choice = input("Rock, Paper or Scissors? ").lower()
else:
    print(f"User: {user_choice}")
    print(f"Computer: {computer_choice}")
    if user_choice == "rock" and computer_choice == "paper":
        print("Paper covers rock")
        computer_win()
    elif user_choice == "paper" and computer_choice == "scissors":
        print("Scissor cuts paper")
        computer_win()
    elif user_choice == "scissors" and computer_choice == "rock":
        print("Rock smashes Scissors")
        computer_win()
    elif computer_choice == "rock" and user_choice == "paper":
        print("Paper covers rock")
        user_win()
    elif computer_choice == "paper" and user_choice == "scissors":
        print("Scissor cuts paper")
        user_win()
    elif computer_choice == "scissors" and user_choice == "rock":
        print("Rock smashes Scissors")
        user_win()
    else:
        print("Its a draw....nobody wins.")
