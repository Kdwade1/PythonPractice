import random

playAgain = 'y'


def play():
    while playAgain == 'y':
        user = input("Chose 'r' for rock,'p' for paper, 's' for scissor ")
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            print(computer)
            return "It's a tie"

        if is_win(user, computer):
            print(computer)
            return "you win"
        else:
            print(computer)
            return "you lost"


# playAgain = input("would you like to play again? y/n ")


def is_win(player, foe):
    if (player == 's' and foe == 'p') or (player == 'p' and foe == 'r') or (player == 'r' and foe == 's'):
        return True


def main():
    print(play())
    while input("Play Again? (Y/N) ").upper() == "Y":
        print(play())


if __name__ == "__main__":
    main()
