from Chapter3 import Chapter3
import time
def Chapter2():
    print(" *YOU WALK INTO TOWN* ")
    time.sleep(2)
    print("*YOU ARE BEING STARED DOWN BY THE LOCALS*")
    time.sleep(2)
    print("*you walk into a shop*")
    time.sleep(2)
    print(" DING! DING!")
    print("the Shop Owner Yells")
    time.sleep(2)
    print("SHOPKEEPER: HEY YOU! GET OUT OF MY STORE BEFORE YOU CAUSE MORE TROUBLE!!!")
    time.sleep(2)
    Ch2_2()
def Ch2_2():
    SecondChoice = input("--What is your response?--1: Reply with confusion 2: Leave the store 3: Defuse the shop owner 4: reply rudely")
    if SecondChoice == '1':
        print("huh?")
        time.sleep(1)
        print("What are you talking about??")
        time.sleep(1)
        print("SHOPKEEPER: You and some other fella was causing trouble, you need to be careful ")
        time.sleep(1)
        print("SHOPKEEPER: You also made someone really mad yesterday")
        time.sleep(1)
        print("YOU TO YOURSELF: Yeah, when don't I ever make someone mad...")
        time.sleep(2)
        print("SHOPKEEPER: Someone might be looking for you")
        time.sleep(2)
        Chapter3()

    elif SecondChoice == '2':
        print("Leave the store")
        time.sleep(2)
        print("you walk out of the store")
        print("I wonder why he was so mad.")
        time.sleep(1)
        print("I should probably ask him...")
        time.sleep(2)
        print("maybe you should walk back in")
        Ch2_2()
        # loop back to "walk into shop"

    elif SecondChoice == '3':
        print("Relax! I haven't done anything")
        time.sleep(2)
        print("SHOPKEEPER: YOU WERE CAUSING TROUBLE AROUND THESE PARTS YESTERDAY")
        time.sleep(2)
        print("SHOPKEEPER: You and someone else, you and him were causing a ruckus at the NIGHTCLUB...   ")
        time.sleep(2)
        print("SHOPKEEPER: Now, are you going to buy anything")
        time.sleep(2)
        print("uhh... yeah sure.")
        time.sleep(3)
        print("*YOU BUY A WATER")
        print("-$2.00")
        Chapter3()

    elif SecondChoice == '4':
        time.sleep(2)
        print("quite you! or I'll show you real trouble!!!")
        time.sleep(2)
        print("SHOPKEEPER: HEY GET OUT, I don't need your rudeness here")
        time.sleep(2)
        print("SHOPKEEPER: Leave or I will call the police.")
        Chapter3()

def ch2(name):
    print()
    Chapter2()
