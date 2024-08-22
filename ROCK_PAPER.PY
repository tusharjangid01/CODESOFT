import random
def game():
    while True:
        user_choice = input("Enter your choice (stone/paper/scissor) or 'q' to quit: ").lower()
        if user_choice == 'q':
            break

        if user_choice not in ['stone', 'paper', 'scissor']:
            print("Invalid choice. Please try again.")
            continue

        choices = ['stone', 'paper', 'scissor']
        computer_choice = random.choice(choices)

        print(f"\nUser: {user_choice}")
        print(f"Computer: {computer_choice}\n")

        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == 'stone':
            if computer_choice == 'scissor':
                print("Stone smashes scissor! You win!")
            else:
                print("Paper covers stone! You lose.")
        elif user_choice == 'paper':
            if computer_choice == 'stone':
                print("Paper covers stone! You win!")
            else:
                print("Scissor cuts paper! You lose.")
        elif user_choice == 'scissor':
            if computer_choice == 'paper':
                print("Scissor cuts paper! You win!")
            else:
                print("Stone smashes scissor! You lose.")

game()