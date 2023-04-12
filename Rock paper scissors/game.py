pimport random

print("Let's play Rock-Paper-Scissors!")

while True:
    user_choice = input("Choose rock (r), paper (p), or scissors (s): ")
    computer_choice = random.choice(['r', 'p', 's'])

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'r' and computer_choice == 's':
        print("You win! Rock smashes scissors.")
    elif user_choice == 'p' and computer_choice == 'r':
        print("You win! Paper covers rock.")
    elif user_choice == 's' and computer_choice == 'p':
        print("You win! Scissors cut paper.")
    else:
        print("You lose! " + computer_choice + " beats " + user_choice)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != 'y':
        break

print("Thanks for playing!")
