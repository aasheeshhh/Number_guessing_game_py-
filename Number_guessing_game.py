import random 
def Number_guessing_game():

    print("******Number Guessing Game******\n") 

    select_range = int(input("Enter the range of Numbers you want to guess\n"))
    count = 0
    computer_guess = (random.randint(1,select_range))

    Difficulty_level =input("""Select the Difficulty level
E = Easy (You have 15 attempts)
M = Medium (You have 10 attempts)
H = Hard (You have 5 attempts)                            
\n""").upper()
    if(Difficulty_level=='E'):
        Max_attempts = 15
    elif(Difficulty_level=='M'):
        Max_attempts = 10
    elif(Difficulty_level=='H'):
        Max_attempts = 5
    else:
        print("Enter a Valid character please\n")
        return
    
    while(count<Max_attempts):
        player_guess = int(input("Take a Guess: "))
        count += 1

        if player_guess < computer_guess:
            print("Higher\n")
        elif player_guess > computer_guess:
            print("Lower\n")
        else:
            print(f"You won in {count} guesses!\n")
            break

    else:
        print("\nOut of Guesses!")
        print("Computer selected:", computer_guess)

    retry = input("Want to play again? (Y/N): ").upper()
    if retry == 'Y':
        Number_guessing_game()
    elif retry == 'N':
        print("Thanks for playing!")
    else:
        print("Enter a valid character Y or N.\n")
  
'''Run the game'''
Number_guessing_game()


    


