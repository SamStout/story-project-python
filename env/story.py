from cmath import log
from secrets import choice
import time
import csv


answer_A =["A", "a"]
answer_B =["B", "b"]


class Player:
    def __init__(self, name, race):
        self.name = name 
        self.race = race



def first_choice():
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("    ")
    print(" Welcome to Middle Earth ")
    print("    ")
    print(" An old man comes to ur hole and tells you to return some jewelery" )
    print("to a volcano without a receipt")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    time.sleep(1)
    print("    ")
    print( " A. Will you accept his quest?"
            " B. Will u not?")
    print("    ")

    choice = input()
    log_message(choice)

    if choice in answer_A:
        option_do_it() 
    elif choice in answer_B: 
        option_dont_do_it()
    else: 
        print("Try again")
        intro()

def option_dont_do_it():
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("    ")
        (print("'Man thats tough' the old man saids."))
        print("    ")
        print("are you sure?")
        print("    ")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        time.sleep(1)
        print("    ")
        print( "A. take the quest "
        "B. Dont do it ")
        print("    ")
        choice = input(">>>>")
        log_message(choice)
        if choice in answer_A: 
            option_do_it()
        elif choice in answer_B:
            (print(" you died"))
        else: 
            print("Try again")
            option_dont_do_it()

def option_do_it():
        print("    ")
        (print("Fantastic, you have chosen to take this quest"))
        (print("Do you wanna take your bestie Sam?"))
        print("    ")
        time.sleep(1)
        print("A. Yes"
        " B. No")
        choice = input()
        log_message(choice)
        if choice in answer_A: 
            print("    ")
            (print("Cool, heres a map"))
            print("    ")
        elif choice in answer_B:
            print("    ")
            (print("'You cannot pass' the wizard says"))
            print("    ")
        else: 
            print("    ")
            print("Try again")
            option_do_it()

def option_do_it():
        print("    ")
        (print("Fantastic, you have chosen to take this quest"))
        (print("Do you wanna take your bestie Sam?"))
        print("    ")
        time.sleep(1)
        print("A. Yes"
        " B. No")
        choice = input()
        log_message(choice)
        if choice in answer_A: 
            print("    ")
            (print("Cool, heres a map"))
        elif choice in answer_B:
            print("    ")
            (print("'You cannot pass' the wizard says"))
        else: 
            print("    ")
            print("Try again")
            option_do_it()

# def intro():
#     print("")
#     print("whats your name")
#     inputName = input()
#     print("whats your race")
#     inputRace = input()
#     p1 = Player(inputName, inputRace)
#     first_choice()

def log_message(choice):
    with open('log.csv', 'a' , encoding = 'UTF8') as f: 
        csvwriter = csv.writer(f)
        csvwriter.writerow(choice)

first_choice()