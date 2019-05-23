from time import *
from random import *

def askName():
    print("What is your name?")
    name = input(">>> ")
    return name
    
def greetings():
    print("")
    name = askName()
    print("Hello there", name, "!")
    print("How are you?")
    reply = input(">>> ").lower()
    print("nice to know.")
    return reply
   

def command():
    command = input("\n>>> ").lower()
    return command




















