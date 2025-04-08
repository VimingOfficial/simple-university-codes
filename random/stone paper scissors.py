#stone paper scissors game with random
import random
list=["sang","kaghaz","gheychi"]
wins=0
while True:
    com=random.choice(list)
    user = input("Enter your chose: ")
    if com==user:
        print("mosvi")
    elif com=="sang":
        if user=="kaghaz":
            print("user win")
            wins=wins+1
        elif user=="gheychi":
            print("computer win")
    elif com=="kaghaz":
        if user=="sang":
            print("computer win")
        elif user=="gheychi":
            print("user win")
            wins=wins+1
    elif com=="gheychi":
        if user=="sang":
            print("user win")
            wins=wins+1
        elif user=="kaghaz":
            print("computer win")
    if wins==3:
        print("User wins 3 times!")
        break