# hangman-
a python project on hangman
import random
import time


def secret_word():
    words = ["apple",
             "bananna",
             "strawberry",
             "pancakes",
             "water"]
    return random.choice(words)


def main():
    pos = 0
    count = 0
    name = input("enter you're name:")
    print(f"welcome {name} to HANGMAN")
    print("____________________________")
    time.sleep(2)
    sword = secret_word()
    print(sword)
    word = "*" * len(sword)
    print(word)
    while count < 4:
        letter = input("guess a letter")
        if letter in sword:
            pos = sword.index(letter)
            sword = sword[:pos] + "@" + sword[pos + 1:]
            word = word[:pos] + letter + word[pos + 1:]
            print(word)
            if sword == "@" * len(sword):
                print(f"congragultions {name} you've won the game")
                break

        else:
            count += 1
            if count == 1:
                print(f"you have only {4 - count} no. of steps, ALL THE BEST!!")
                print('''
                    ____________
    |          O
|         /|\
|        / | \
|          |
|         / \
|        /   \
|


                  ''')
            elif count == 2:
                print(f"you have only {4 - count} no. of steps, ALL THE BEST!!")
            elif count == 3:
                print(f"you have only {4 - count} no. of steps, ALL THE BEST!!")
            elif count == 4:
                print("you've lost the game")


main()
