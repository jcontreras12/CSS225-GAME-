
import time
def Chapter5():
    print("Chapter 5 Start:")
    time.sleep(3)
    print("STRANGER: HEY YOU!!! WHERE IS MY MONEY!!!")
    time.sleep(2)
    print("STRANGER: IVE BEEN LOOKING FOR YOU")
    time.sleep(2)
    print("STRANGER: OH IM GONNA GET YOU!!!")
    time.sleep(2)
    Ch5_1()
def Ch5_1():
    FinalChoice = input("Quickly! you have to make a choice-- 1: RUN  2: FIGHT 3: NOTHING")
    if FinalChoice == "1":
        time.sleep(1)
        print(" RUN: you run away and get chased by the strangers")
        time.sleep(2)
        print("You ran from the strangers far enough but now you are more lost than before,")
        time.sleep(2)
        print("YOU ARE IN FACT LOST")
    elif FinalChoice == "2":
        print("FIGHT: you fight off the Stranger and his Gang")
        time.sleep(1)
        print("*FIGHT ENSUES*")
        time.sleep(2)
        print("*BOTTLES BREAK*")
        time.sleep(2)
        print("punches are thrown")
        time.sleep(2)
        print("*TABLES BREAK*")
        time.sleep(2)
        print("you knock one out cold")
        time.sleep(2)
        print(" you are caught off guard and take a hit")
        time.sleep(2)
        print("Your counter punch knocks him to the ground")
        time.sleep(2)
        print("*YOU KNOCK OUT THE STRANGER AND THE REST RUN AWAY*")
        time.sleep(2)
        print("YOU WIN!!!")
    
    elif FinalChoice == "3":
        print("NOTHING: YOU DO NOTHING.")
        time.sleep(1)
        print("THE STRANGER CATCHES YOU")
        time.sleep(3)
        print("--YOU ARE BEATEN TO A PULP--")
        time.sleep(1)
        print("YOU LOSE...")

def ch5(name):
    print()
    Chapter5()
