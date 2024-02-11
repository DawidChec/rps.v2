
user_choice = input('Welcome in "Rock Paper Scissors" game!, do you wish to start the game? (Y/n): ').lower()
if user_choice == "y":

    while True:

        first_player = input("Enter the name of the first player: ")
        second_player = input("Enter the name of the second player: ")

        first_player_weapon = input(f"Okey, its time for {first_player} to choose his/her weapon: ")
        second_player_weapon = input(f"Okey, its time for {second_player} to choose his/her weapon: ")

        if first_player_weapon == "rock" and second_player_weapon == "paper":
            print(f"Congratulations {second_player}, you won!")
        elif first_player_weapon == "paper" and second_player_weapon == "scissors":
            print(f"Congratulations {second_player}, you won!")
        elif first_player_weapon == "scissors" and second_player_weapon == "paper":
            print(f"Congratulations {first_player}, you won!")
        elif first_player_weapon == "rock" and second_player_weapon == "scissors":
            print(f"Congratulations {first_player}, you won!")
        elif first_player_weapon == "paper" and second_player_weapon == "rock":
            print(f"Congratulations {first_player}, you won!")
        elif first_player_weapon == "scissors" and second_player_weapon == "rock":
            print(f"Congratulations {second_player}, you won!")
        elif first_player_weapon != "rock" or "paper" or "scissor" or first_player_weapon != "rock" or "paper" or "scissor":
            print("Wrong input")
        else:
            print("It's a tie!")

        play_again = input("Do you wish to play again? (Y/n): ").lower()

        if play_again == "y":
            pass
        else:
            print("It was nice to play with you.")
            break

elif user_choice == "n":
    print("Okey, have a nice day!")

elif user_choice != "n" or "y":
    print("Wrong input!")












