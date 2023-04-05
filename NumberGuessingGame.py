import random

n = random.randrange(1, 101)
tries = 0
playerName = input("What is your name ")
print("Nice name " + playerName + ". Shall we begin")
guess = int(input("Enter any number"))
# try:
while tries < 5:
    if guess < n:
        print("Too low")
        tries += 1
        guess = int(input("Enter any number"))
    elif guess > n:
        print("Too high")
        tries += 1
        guess = int(input("Enter any number"))
    else:
        print("Wow you got it!")
        break
if guess == tries:
    print('You guessed the number in ' + str(tries) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(n))
