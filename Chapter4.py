from Chapter5 import Chapter5 
import time
def Chapter4():
    print("Begin, Chapter 4")
    time.sleep(2)
    print("*YOU WALK THROUGH THE PEOPLE TO GET TO THE BAR*")
    time.sleep(2)
    print("The club is blasting music")
    time.sleep(2)
    print("Although it was early afternoon it was still crowded")
    time.sleep(2)
    print("*YOU walk up to the bar")
    time.sleep(1)
    print("YOU: Hey I was wondering if you can help me for a second")
    time.sleep(2)
    print("BARKEEPER: What are you still doing here")
    time.sleep(2)
    Ch4_1()
def Ch4_1():
    FourthChoice = input("-- Your respond with: -- 1: ask what happened  2: Leave the bar  3:Order a Drink")
    if FourthChoice == "1":
        time.sleep(2)
        print(" What happened last night?")
        time.sleep(2)
        print("BARKEEPER: Don't you remember???")
        time.sleep(2)
        print("---PLAYER IS INTERRUPTED---")
        Chapter5()
    elif FourthChoice == "2":
        time.sleep(2)
        print("*leave the Bar*")
        time.sleep(1)
        print(" you begin to walk away when suddenly")
        time.sleep(2)
        print("--PLAYER IS INTERRUPTED--")
        Chapter5()
    elif FourthChoice == "3":
        time.sleep(2)
        print("*Order a Drink*")
        time.sleep(2)
        print("-- PLAYER IS INTERRUPTED --")
        Chapter5()
     
def ch4(name):
    print()
    Chapter4()

