import random
from hangman_words import word_list
from hangman_art import stages, logo

num_lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

# Can I do this without the placeholder and go directly to display?
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:

    print(f"**************************** {num_lives}/6 LIVES LEFT ****************************")

    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed '{guess}'.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        num_lives -= 1
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")

        if num_lives == 0:
            game_over = True

            print(f"***********************YOU LOSE********************** \n The correct word was {chosen_word}.")

    if "_" not in display:
        game_over = True
        print("You Win")

    print(stages[num_lives])
