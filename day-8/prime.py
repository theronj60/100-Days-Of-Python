def prime_checker(number):
    if number % 2 != 0 and number % number == 0:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

game = True

while game:
    n = int(input("Check this number: "))
    prime_checker(number=n)
    keep_playing = input("Would you like to play again? Y or N ").lower()
    if keep_playing == "n":
        game = False
    if game == False:
        print("Thanks for playing!")
        break
