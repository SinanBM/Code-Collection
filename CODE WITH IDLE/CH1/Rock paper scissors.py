import random

while True:

    winner = ""

    random_choice = random.randint(0,2)

    if random_choice == 0:
        computer_choice = "rock"

    elif random_choice == 1:
        computer_choice = "paper"

    else:
        computer_choice = "scissors"

    user_choice = input("Rock, paper or scissors? ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Please enter a valid choice!")
        continue
                                
    if computer_choice == user_choice:
        print("It's a tie!")

    else:
        if (computer_choice == "paper" and user_choice == "rock") or \
        (computer_choice == "rock" and user_choice == "scissors") or \
        (computer_choice == "scissors" and user_choice == "paper"):
            winner = "Computer"

        else:
            winner = "User"

        print("The", winner, "wins!", "The computer chose " + computer_choice + ".")
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ["yes", "no"]:
            print("Please enter yes or no. ")
            
        elif play_again == "yes":
            break
        else:
            print("Thanks for playing!")
            
            
    
