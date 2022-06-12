import random

print('Welcome to a game of Rock Paper Scissors')
    
is_valid = True

while is_valid:
    user_choice = input('Select your move "R" "P" or "S": ').strip().lower()

    if user_choice == "r":
        user_choice = "Rock"
    elif user_choice == "s":
        user_choice = "Scissors"
    elif user_choice == "p":
        user_choice = "Paper"
    else:
        print('Invalid move selected, try again')
        continue
    
    possible_moves = ['Rock', 'Paper', 'Scissors']
    computer_move   = random.choice(possible_moves)

    print(f'`Player ({user_choice}) : CPU ({computer_move})`')
 

    if user_choice == computer_move:
        print("Same move, It's a tie!")
    elif user_choice == "Rock":
        if computer_move == "Scissors":
            print("Rock crushes Scissors! You win")
        else:
            print("Paper covers Rock! You lose!")
    elif user_choice == "Scissors":
        if computer_move == "Paper":
            print("Scissors cuts Paper! You win!")
        else:
            print("Rock crushes Scissors! You lose!")
    elif user_choice == "Paper":
        if computer_move == "Rock":
            print("Paper covers Rock! You win!")
        else:
            print("Scissors cuts Paper! You lose!")

    play_again = input("Would you like to play another round? (Y/N): ")
    if play_again.lower() == "y":
        pass

    elif play_again.lower() == "n":
        is_valid = False
    
    else: 
        is_valid = False
               