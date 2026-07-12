import random

def rock_paper_scissors_game():
    choices = ["rock", "paper", "scissors"]
    user_wins = 0
    computer_wins = 0
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, scissors) or q to quit: ").lower()
    if user_choice == "q":
        print("goodbye!")
        quit()
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {user_choice}")
    
    if user_choice == computer_choice:
            print("It's a tie!")
            quit()
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
          print("You win!")
          user_wins += 1
    else:
           print("Computer wins!")
           computer_wins += 1   
    print("you won", user_wins, "times.", "computer wins", computer_wins, "times.")

rock_paper_scissors_game()