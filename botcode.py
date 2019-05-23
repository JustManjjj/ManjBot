from functions import *

greetings()
command()
while True:
    if command in ("change my name","change name","name change"):
        askName()

    else:
        print("Sorry, I don't know that.")
        command()
        
