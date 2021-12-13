from Chapter2 import Chapter2
import time
def Chapter1_intro():
    print(" Chapter 1:")
    time.sleep(1)
    print("The hot beaming sun shines down on the player who has awaken in the middle on no where next to a road, cellphone is dead and no wallet")
    time.sleep(1)
    print("You awaken in the middle of nowhere, what are you going to do")
    Ch1_1()
def Ch1_1():
    FirstChoice = input(" Explore the area or Follow the road into town").lower().strip()
    if FirstChoice == "Explore the area" or FirstChoice == "explore the area":
        print("*YOU FOUND NOTHING INTERESTING *.")
        Ch1_1()
    elif FirstChoice == "Follow the road into town" or "follow the road to town":
        print("*YOU WALK DOWN THE ROAD*")
        time.sleep(1)
        print("Man, How did I get here?")
        time.sleep(1)
        print("*TRUCK BRUSHES PAST YOU*")
        time.sleep(1)
        print("Whoa that was close!")
        time.sleep(1.5)
        print("Why can't I remember anything")
        time.sleep(1.5)
        print("this headache doesn't help me think either")
        time.sleep(2)
        print("*YOU ARRIVE AT A TOWN*")
        time.sleep(3)
        print(" Start, Chapter 2")
        Chapter2()
def ch1(name):
    print()
    Chapter1_intro()

