import random

from Words import wordlist


def get_word():
    word = random.choice(wordlist)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letter = []
    guessed_word = []
    tries = 6

    print("It's time to play hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letter:
                print("Hey, smart one, you've already guessed that!", guess)
            elif guess not in word:
                print(guess, "not in word")
                tries -= 1
                guessed_letter.append(guess)
            else:
                print("GoodJob ", guess, " is the word")
                guessed_letter.append(guess)
                words_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    words_as_list[index] = guess
                    word_completion = "".join(words_as_list)
                    if "_" not in word_completion:
                        guess = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_word:
                print("you've already guessed the word smart one!", guess)
            elif guess != word:
                print(guess, "not in the word")
                tries -= 1
                guessed_word.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("not a valid guess")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("congrats you guessed the word. You Win")
    else:
        print("HAHAHA! Loser. The word was ", word)


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
