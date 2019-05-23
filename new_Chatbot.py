from time import *
import random
from random import *
import random
whySoGood = ["Amazing! But why was it so good?","Thats sick! But why was it so good?"]

amazedExpressions = ["Sick!","Wow!","Mad!","Awesome!","Madness!","Jheez!","Great!"]

hopeGetsBetter = ["I Hope it gets better...",
                  "If your day hasn't been the greatest, I can try and make you laugh? Type 'joke' for me to giver you a joke",
                  "Ah that's not good is it! Just try and look at the bright side of things :)"
                  ]

hello = [
        "Sat Sri Akaal","Assalamualaikum",
         "Namaste","Bonjour","¡Hola","Konnichiwa",
         "Guten Tag","Nǐn hǎo","Privet","Ahoj",
         "Dzień Dobry","yeh wot fam",
         "swag1famalam",
         "swag el swafwaan tayyib",
         "safwaan"
         ]

failure = [
           "Sorry. I don't know.",
           "Sorry. I do not understand that command.",
           "Sorry, I am not advanced enough to read your mind.",
           "I don't think that's possible.",
           "I can't do that. Maybe the creator hasn't implemented it yet.",
           "That command is false.",
           "I cannot recognize the command."
           ]
            

#define a function to ask for a name
print(random.choice(hello)+"!"+" I'm JustManjjjBot!")
sleep(0.35)

def AskName():
    name = input("What's your name?\n>>> ")
    return name

#define function to greet you
def Greetings():
    name = AskName()
    print("Hello there {}!".format(name))

Greetings()
print("\nType 'help' for a list of commands for ManjBot to follow.")
#LOOOOP like a POoooooop
while True:
    sleep(0.7)

    #ask for a command and put it inside of a variable
    command = input("\nWhat would you like me to do?\n>>> ").lower()

    if command in ("set alarm","alarm","alarm set","turn on an alarm","make an alarm","create an alarm"):
        alarmDate = input("\nWhat date would you like to set your alarm for?(dd/mm/yy)\n>>> ")
        alarmTime = input("What time would you like to set your alarm for?(hh:mm)\n>>> ".format(alarmDate))
        print("Your alarm has been successfully set on {}, at {}.".format(alarmDate,alarmTime))

    if command in ("hello","hi","hey","hola","sat sri akaal"):
        print(random.choice(hello)+"!"+" How are you?")
        response_hello = input(">>> ")
        if 'bad' or 'not good' or 'not great' or 'terrible' or 'rubbish' or 'crappy' or 'crap' or 'dead' in response_hello:
            response_responseHello = input((random.choice(whySoGood))+"\n>>> ".format(response_hello))
            print(random.choice(hopeGetsBetter))
           
        elif 'good' or 'great' or 'amazing' or 'very good' in response_hello:
            WhatDidYouDo = input("That's amazing! What exicting things did you do today?\n>>> ")
            print(random.choice(amazedExpressions))

    else:
        print(random.choice(failure))
