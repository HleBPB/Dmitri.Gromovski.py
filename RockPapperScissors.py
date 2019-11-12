import random
 
print("---Game---")
print("Stone/Scissors/Paper")
app = random.randint(1, 3)
if app == 1:
    gg = "Stone"
elif app == 2:
    gg = "Scissors"
else:
    gg = "Paper"
print("1)Stone")
print("2)Scissors")
print("3)Paper")
try:
    x = int(input("Write the number:/n> "))
    if x == 1:
        print("")
        print("Your choise: Stone")
        print("Opponent choise: " + str(gg))
        print("")
        if app == 1:
            print("Draw :/")
        elif app == 2:
            print("You win! :3")
        else:
            print("Opponent win\n Your Lose! :c")
            print("")
    elif x == 2:
        print("")
        print("Your choise: Scissors")
        print("Opponent choise: " + str(gg))
        print("")
        if app == 1:
            print("Opponent win\n Your Lose! :c")
        elif app == 2:
            print("Draw :/")
        else:
            print("You win! :3")
            print("")
    elif x == 3:
        print("")
        print("Your choise: Paper")
        print("Opponent choise " + str(gg))
        print("")
        if app == 1:
            print("You win! :3")
        elif app == 2:
            print("Opponent win\n Your Lose! :c")
        else:
            print("Draw :/")
        print("")
    else:
        print("Write only numbers: 1/2/3!")
except ValueError:
    print("ERROR: Write only INT numbers!")