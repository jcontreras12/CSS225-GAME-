from Chapter4 import Chapter4 
import time
def Chapter3():
    print(" Chapter 3 Start,")
    time.sleep(2)
    print("Confused You leave the store and continue further into town")
    time.sleep(2)
    print("You continue to walk through an unfamiliar part of town")
    time.sleep(2)
    print("A nightclub... ")
    time.sleep(2)
    print("If I was anywhere last night it was here")
    time.sleep(1)
    Ch3_1()
def Ch3_1():
    ThirdChoice = input("Walk into the nightclub ????(Yes/No): ")
    if ThirdChoice == 'Yes' or 'Y':
        print("*YOU WALK TOWARDS THE NIGHTCLUB*")
        time.sleep(2)
        print("*YOU ARRIVE AT THE NIGHTCLUB*")
        time.sleep(2)
        print("You enter the nightclub building")
        Chapter4()

    elif ThirdChoice == 'No' or 'N':
        time.sleep(1)
        print("Well Where else am I going to go")
        time.sleep(2)
        print("walk into the nightclub to ask for information about last night")
        Chapter4()

def ch3(name):
    print()
    Chapter3()
