from high_low_art import logo, vs
from high_low_data import data
import random


def format_data(account):
    """Takes the account data and returns the account data into printable format"""
    # ["needs to match key from data exactly"]
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return user_guess == 'A'
    else:
        return user_guess == 'B'


# Print logo
print(logo)
score = 0
# Start while loop
# - set flag to turn off game ends
game_should_continue = True
# Generate a random account from the game data
account_a = random.choice(data)
account_b = random.choice(data)


# Make the game repeatable
# - start while game_should_continue flag is true
while game_should_continue:

    # Making account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)

    # if both a and b choose the same random item
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask the user for a guess
    user_guess = input(f"Who has more followers? Type 'A' or 'B': ").upper()

    # Clear the Screen
    print("\n" * 20)
    print(logo)

    # Check if user is correct
    # - Get follower count for each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    # - Use If statement to check if user is correct
    # - Define a separate function check_answer()

    is_correct = check_answer(user_guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right! Your score is: {score}")
    else:
        print(f"Sorry, game over. Final score: {score}")
        game_should_continue = False
