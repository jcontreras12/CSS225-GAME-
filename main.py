# Jose Contreras
# 11/15/21danny
import Chapter1
def gameintro():
# Use a breakpoint in the code line below to debug your script.
    print("*" * 67)
    print("**           Game written and created by Jose Contreras          **")
    print("**                                                               **")
    print("**     This game takes place in a futuristic cyber dystopia      **")
    print("**    Your goal is to recount what took place the day before     **")
    print("** Own up to the consequences of your actions as you play through **")
    print("*" * 67)

def main():
    print("Enter your name before starting")
    player = input("[Player Name: ]")
    gameintro()
    answer = input("\n Start the Game ???(Y/N): ")
    answer = answer.upper()
    if answer == 'Y':
        print("Start, Chapter 1")
        Chapter1.ch1(player)
    elif answer == 'N':
        print(" Nope?, to late.")
        Chapter1.ch1(player)

main()
