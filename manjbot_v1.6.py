from time import *
import random
from random import *
import random
import urllib
import webbrowser
import sys
import winsound

amazedExpressions = ["Sick!","Amazing!","Wow!", "Awesome!","Mad!"]

hopeGetsBetter = [
                  "I Hope it gets better...",
                  "If your day hasn't been the greatest, I can try and make you laugh? Type 'joke' for me to giver you a joke",
                  "Ah that's not good is it! Just try and look at the bright side of things :)"
                  ]

hello = ["Sat Sri Akaal","Assalamualaikum",
         "Namaste","Bonjour","¡Hola","Konnichiwa",
         "Guten Tag","Nǐn hǎo","Privet","Ahoj",
         "Dzień Dobry","yeh wot fam","Hey","Hello"
         ]

failure = ["Sorry. I don't know.",
           "Sorry. I do not understand that command.",
           "Sorry, I am not advanced enough to read your mind.",
           "I don't think that's possible.",
           "I can't do that. Maybe the creator hasn't implemented it yet.",
           "That command is false.",
           "I cannot recognize the command."]
            

#define a function to ask for a name
print(random.choice(hello)+"!"+" I'm ManjBot!\n~~~~~~~~~~~~~~~~~~~~~~~~~")
sleep(0.35)

def help():
    print("""\nYou can enter these commands to get an answer. \n""")

def help_list():
    print("""
• Alarm - This command will help you to set an alarm for whenever you want, even if it is not a real date.\n
• Nothing - Literally insults you and switches itself off. \n
• Turn Off - It will switch ManjBot off.\n
• Open Website - You can open any website with the URL. MAnjBot will ask for the URL and will open that website.\n
• JustManjjj - Opens my Youtube channel.\n
• Set Alarm - This is a tool that can help setup alarms.\n
• Simon Says - This will copy whatever you say.\n
• ManjBot - Information about ManjBot.

-------------------

COmmands like 'hello' can start conversations with ManjBot. These conversations may not be accurate because I have to make an if statement for every outcome.
""")

def AskName():
    name = input("What's your name?\n>>> ")
    return name

#define function to greet you
def Greetings():
    name = AskName()
    print("Hello there {}!".format(name))

Greetings()
sleep(0.4)
print("\nType 'help' for a list of commands for ManjBot to follow.")



################################################ ACTUAL PROGRAM ###################################################



#while loop
while True:



    sleep(0.7)

    #Ask for a command and put it inside of a variable
    command = input("\nWhat would you like me to do?\n>>> ").lower()




    #This command will show all of the possible commands.
    if command in ("help"):
        help() 
        sleep(0.75)
        help_list()
        sleep(0.3)




    
    #This will give you info on what Manjbot actually is.
    elif command in ("manjbot","manj bot"):
        print("""ManjBot is an AI based in Python that allows you to interact with him.

        ManjBot [Version 0.1.6]
       (py) 2019 Manjeev Takhar. All rights reserved.\n""")





    #This is when you don't need ManjBot's help. It gets very upset.
    elif command == 'nothing':
        print("i dont need you either you idiot")
        break




    #This will shut down ManjBot and break the while True loop
    elif command in("turn off","shutdown","exit","leave"):
        break





    #This will open a website by asking for the user for a URL and then opening that URL.
    elif command in ("open website","open url","url open"):
        url = input("\nEnter the URL of the website that you would like to open\n>>> ")
        webbrowser.open_new(url)

    



    #This will open my YouTube channel, JustManjjj
    elif command in ('justmanjjj'):
        webbrowser.open_new('https://www.youtube.com/channel/UCaDJoIRovjEF64JtWKaRGWQ')





    #This can be used to create alarms. *NOTE* - These do not actually work.
    elif command in ("set alarm","alarm","alarm set","turn on an alarm","make an alarm","create an alarm"):
        alarmDate = input("\nWhat date would you like to set your alarm for?(dd/mm/yy)\n>>> ")
        alarmTime = input("What time would you like to set your alarm for?(hh:mm)\n>>> ".format(alarmDate))
        print("Your alarm has been successfully set on {}, at {}.".format(alarmDate,alarmTime))




    #Saying 'hello' will output another translation of hello into any language.
    elif command in ("hello","hi","hey","hola","sat sri akaal","bonjour"):
        print(random.choice(hello)+"!")




    #This command will copy whatever you say
    elif command in("simon says","copy me","say what i say","say whatever i say","say what i say","repeat after me"):
        repeat = input("\nWhat would you like me to say?\n>>> ")
        print(repeat+"\n")
        


    #Can search YouTube
    elif command in ("search youtube","youtube search","youtube"):
        ytsearch = input("YouTube Search> ")
        webbrowser.open_new('https://www.youtube.com/results?search_query={}'.format(ytsearch))
    



    #Saying 'how are you' can start conversations
    elif command in ("how are you", "howre you") :
        howareyou = input(random.choice(hello)+"!"+" How are you?\n>>>")

        if 'bad' or 'not good' or 'not great' or 'rubbish' or 'crappy' or 'crap' in howareyou:
            response_howareyou = input("Why is it {}?\n>>> ".format(response_hello))
            if response_howareyou == response_howareyou:
                print(random.choice(amazedExpressions))

        elif 'good' or 'great' or 'amazing' or 'very good' in howareyou:
            WhatdidYouDo = input("That's amazing! What exicing things did you do today?")
            print(random.choice(amazedExpressions))

        elif 'alright' or 'calm' in howareyou:
            print(random.choice(amazedExpressions))





    #if no command is valid, a random choice from the array 'failure' will print.
    else:
        print(random.choice(failure))
