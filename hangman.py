import os
import sys
import random
from words import gry,zwierzeta, imiona_menskie, imiona_zenskie, rodzina, sport, instrumenty, abc_list, z, r, im, iz, g, i, s
from hangman_display import display_hangmanl1, display_hangmanl2, display_hangmanl3

tries = 0
word = "cos"
used_letters = []
user_word = []
select = ""
again = ""
my_while = 0
dificulty = 0
easy = ""
normal = ""
hard = ""

def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
            
    
    return indexes
def show_state_of_game():
    print(" ".join(user_word))
    print("Other attempts:", tries)
    print("Letters used", ", ".join(used_letters))
    print()
def hi():
    print("welcome to hangman game")
    print()


############################################################################################################################################################################

haslo = ""
category_1 = [z, r, iz, im, s, i, g,]
selec1 = "1"
selec2 = "2"

dif = ""
dif1 = "1"
dif2 = "2"
dif3 = "3"


hi()
input("Press Enter to continue...")

while True:
    print("Select Dificulty: ")
    print("1. Easy")
    print("2. Normal")
    print("3. Hard")
    dif = (input("Enter 1, 2 or 3: "))
    
    if dif1 == dif:
        dificulty = easy
        tries = 9
    elif dif2 == dif:
        dificulty = normal
        tries = 6
    elif dif3 == dif:
        dificulty = hard
        tries = 3
    else:
        continue
    break

while True:
    while True:
        print("1. Enter your own password")
        print("2. Random password")
        selec = (input("Enter 1 Or 2: "))
        if selec1 == selec:
            word = input("Enter password: ")
            word = word.upper()
        elif selec2 == selec:
            print()
            print("category:")
            category = "".join(random.choice(category_1))
            print(category)
            if category == "zwierzeta":
                haslo = "".join(random.choice(zwierzeta))
                word=haslo
            elif category == "rodzina":
                haslo = "".join(random.choice(rodzina))
                word=haslo
            elif category == "imiona zenskie":
                haslo = "".join(random.choice(imiona_zenskie))
                word=haslo
            elif category == "imiona menskie":
                haslo = "".join(random.choice(imiona_menskie))
                word=haslo
            elif category == "sport":
                haslo = "".join(random.choice(sport))
                word=haslo
            elif category == "instrumenty":
                haslo = "".join(random.choice(instrumenty))
                word=haslo
            elif category == "gry":
                haslo = "".join(random.choice(gry))
                word=haslo
        else:
            print("Choose the correct options: ")
            continue
        break


############################################################################################################################################################################

    for letter in word:
        if letter in abc_list:
            user_word.append("_")
        elif not letter in abc_list:
            user_word.append(" ")
    while my_while != 1:
        print("Enter the letter: ")
        letter = (input())
        print()
        if not letter in used_letters:  
            if len(letter) == 1:    
                used_letters.append(letter)
                print()

                found_indexes = find_indexes(word, letter)

                if letter in abc_list:
                    if len(found_indexes) == 0:
                        print("There is no such letter")
                        if dificulty == easy:
                            print(display_hangmanl1(tries))
                        elif dificulty == normal:
                            print(display_hangmanl2(tries))
                        elif dificulty == hard:
                            print(display_hangmanl3(tries))
                        tries -= 1
                        if tries == 0:
                            print("End of the game :(")
                            print("word: "+word)
                            print("")
                            
                            again = input("Wanna play again: ")
                            if again.upper() == "YES":
                                my_while = 1
                                continue
                                
                            elif again.upper() == "NO":
                                sys.exit(0)
                    else:
                        for index in found_indexes:
                            user_word[index] = letter
                        if "".join(user_word) == word:
                            print("".join(user_word))
                            print("That's the word!")
                            print("")
                            
                            again = input("Wanna play again: ")
                            if again.upper() == "YES":
                                my_while = 1
                                continue
                            
                            elif again.upper() == "NO":
                                sys.exit(0)
                else:
                    print("Wrong sign")
                    print("Enter the letter")
            else:
                print("Enter ONE letter")
            show_state_of_game()
        else:
            print("You have already entered this letter")
            print("Enter the letter again")



#6. interface