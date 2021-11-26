import random
options = ['Rock', 'Paper', 'Scissors']


player = False
Loss = 0
Win = 0
Tie = 0

while player == False:
    Computer = options[random.randint(0,2)]
    User = input("Rock, Paper, Scissors or End? ")
    if User == Computer:
        print("Tie")
        Tie = Tie + 1
    elif User == "Rock":
        if Computer == "Paper":
            print("You lose!")
            Loss = Loss + 1
        else:
            print("You win!")
            Win = Win + 1
    elif User == "Paper":
        if Computer == "Scissors":
            print("You lose!")
            Loss = Loss + 1
        else:
            print("You win!")
            Win = Win + 1
    elif User == "Scissors":
        if Computer == "Rock":
            print("you lose!")
            Loss = Loss + 1
        else:
            print("You win!")
            Win = Win + 1
    elif User == "End":
        player = True
    else:
        print("Please enter a valid option")
    
    print("Your total losses: ", Loss)
    print("Your total Wins: ", Win)
    print("Your total Tie's: ",Tie)
    print("\n")