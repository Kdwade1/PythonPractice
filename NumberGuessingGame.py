import random

n = random.randrange(1, 101)
tries = 5
playerName = input("What is your name ")
print("Eh I guess it was kinda pointless to learn your name. Alright " + playerName + "! Shall we begin.")
guess = int(input("Enter any number between 1-100 "))
# try:
while tries > 0:
    if guess > 100:
        print("You can't read can you.")
    if guess < n:
        print("Too low")
        tries -= 1
        print("You have " + str(tries) + " tries left")
        guess = int(input("Enter any number "))

    elif guess > n:
        print("Too high")
        tries -= 1
        print("You have " + str(tries) + " tries left")

        guess = int(input("Enter any number"))

    else:
        print('You guessed the number in ' + str(tries) + ' tries!')
        break

if tries == 0:
    print('You did not guess the number, The number was ' + str(n))




