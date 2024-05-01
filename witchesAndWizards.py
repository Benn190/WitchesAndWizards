#!/usr/bin/env python

def intro():
    print("Sylvan: Welcome! If you want to become a witch or wizard, you are in the right place.")
    print("Sylvan: What is your name?")
    name = input()


    print("Sylvan: Hello " + name + "! Are you a witch or a wizard? (1 for witch, 2 for wizard)")
    witWiz = input()

    while not(witWiz is "1" or witWiz is "2"):
        print("Are you a witch or a wizard? (1 for witch, 2 for wizard)")
        witWiz = input()
        print(witWiz)


    witch = False
    wizard = False
    ww = ""
    if witWiz == "1":
        witch = True
        ww = "witch"
    else:
        wizard = True
        ww = "wizard"
        
    print("Sylvan: Amazing! To the " + ww + " academy! You will soon be a strong " + ww + "!")

if __name__ == "__main__":
    intro()