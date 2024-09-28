import random

correct_choice = ["rock", "paper", "scissors"]
play_again = "yes"

while play_again.lower() == "yes":
    user_move = input("Enter your move (rock, paper, or scissors): ")
    
    while user_move not in correct_choice:
        print("Invalid move. Please choose either rock, paper, or scissors.")
        user_move = input("Enter your move: ")
        
    moves = ["rock", "paper", "scissors"]
    computer_move = random.choice(moves)

    if user_move == computer_move:
        result = "It's a tie!"
    elif (user_move == "rock" and computer_move == "scissors") or (user_move == "paper" and computer_move == "rock") or (user_move == "scissors" and computer_move == "paper"):
        result = "Congratulations! You win!"
    else:
        result = "Sorry, the computer wins!"
        
    print(f"You chose: {user_move}")
    print(f"The computer chose: {computer_move}")
    print(result)
    
    play_again = input("Do you want to play again? (yes/no): ")