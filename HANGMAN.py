import random
import time


def secret_word():
    avail_words = ["apple",
                   "bana",
                   "water",
                   "pina",
                   "haze",
                   "wall",
                   ]
    return random.choice(avail_words)


sword = secret_word()
length = len(sword)

name = str(input("please enter your name:"))
print(f"Welcome To The Game Mr.{name}")
time.sleep(2)

print("LETS START")
count = 0
display = "*" * length


def hangman(count, display, sword):
    limit = 3
    guess = str(input(F"THIS IS THE CURRENT WORD:{display} ENTER YOUR GUESS:"))
    if guess in sword:
        pos = sword.find(guess)
        sword = sword[:pos] + "*" + sword[pos + 1:]
        display = display[:pos] + guess + display[pos + 1:]
    else:
        count += 1
        if count == 1:
            print(f"WRONG INPUT!! you have{limit - count} attempts left")
            print(''''
                    
                             
                          |          \n
                          |          \n
                          |          \n
                          |         \n
                          |         \n
                          |         \n
                          |         \n
                                            ''')



        elif count == 2:
            print(f"WRONG INPUT!! you have{limit - count} attempts left")
            print('''
                            __________  \n
                            |         | \n
                            |         | \n
                            |         | \n
                            |         | \n
                            |                  
                            |      
                            |      
                            |      
                            |       
                            |       
                                            ''')
        elif count == 3:
            print(f"WRONG INPUT!! you have{limit - count} attempts left")
            print('''' you have beeen hanged
                    __________  \n
                    |         | \n
                    |         | \n
                    |         | \n
                    |         | \n
                    |         O \n
                    |       / |\ \n
                    |      /  | \ \n
                    |         |     \n
                    |        / \    \n
                    |       /   \   \n

                                                ''')

    if sword == "*" * length:
        print("congratulations you've got the right word")
    elif limit != count:
        hangman(count, display, sword)


hangman(count, display, sword)
