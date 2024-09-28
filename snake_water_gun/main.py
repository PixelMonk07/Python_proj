import random  # Importing the random module to allow the computer to choose randomly

# Function to get a random choice from the list of choices
def get_computer_choice(choices):
    return random.choice(choices)

# Function to determine the winner based on user and computer choices
def determine_winner(user, computer):
    # Dictionary that defines which choice beats which
    win_conditions = {
        "snake": "water",   # Snake defeats Water
        "water": "gun",     # Water defeats Gun
        "gun": "snake"      # Gun defeats Snake
    }
    
    # If both choices are the same, it's a draw
    if user == computer:
        return "It's a draw!"
    # If the user's choice defeats the computer's, the user wins
    elif win_conditions[user] == computer:
        return f"{user.capitalize()} wins!.....{user.capitalize()} defeats {computer.capitalize()}."
    # Otherwise, the computer wins
    else:
        return f"{computer.capitalize()} wins!.....{computer.capitalize()} defeats {user.capitalize()}."

# Main function to run the game
def main():
    # List of valid choices for the game
    choices = ["snake", "water", "gun"]
    
    # Prompt the user to enter their choice and convert it to lowercase
    user_input = input("Snake, Water, or Gun: ").lower()
    
    # Check if the user's input is valid
    if user_input in choices:
        # Get a random choice for the computer
        computer_choice = get_computer_choice(choices)
        print(f"Computer chose: {computer_choice.capitalize()}")
        
        # Determine and print the result of the game
        result = determine_winner(user_input, computer_choice)
        print(result)
    else:
        # If the user input is invalid, display an error message
        print("Invalid input! Please choose Snake, Water, or Gun.")

# Entry point of the program
if __name__ == "__main__":
    main()