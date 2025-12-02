from game_logic import RockPaperScissors

game = RockPaperScissors()

def get_user_choice():
    while True:
        try:
            user_input = input("\nEnter rock, paper, scissors or quit: ").lower()
            if user_input == "quit":
                return "quit"
            if user_input not in game.options:
                raise ValueError("Invalid choice! Try again.")
            return user_input
        except ValueError as e:
            print(e)

def play_game():
    while True:
        user = get_user_choice()
        if user == "quit":
            break

        computer = game.get_computer_choice()
        print("Computer chose:", computer)

        winner = game.get_winner(user, computer)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
        else:
            print("Computer wins this round!")

        game.update_score(winner)

        print(f"Score -> You: {game.user_score} | Computer: {game.computer_score}")

    print("\nFinal Score:")
    print(f"You: {game.user_score}, Computer: {game.computer_score}")
    print("Thanks for playing!")

play_game()
