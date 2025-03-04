# Imports
import turtle
import pandas

# Set Screen
screen = turtle.Screen()  # create screen
screen.title("U.S. States Game")  # name screen

# Add Background Image
image = "blank_states_img.gif"  # set image variable
screen.addshape(image)  # add image as a shape
turtle.shape(image)  # assign the image to the turtle shape

data = pandas.read_csv("50_states.csv")  # pandas read csv and set the content to variable
all_states = data.state.to_list()  # get the data series of the first column and assign to list variable
guessed_states = []  # create empty list to hold the states as they are guessed

while len(guessed_states) < 50:  # while the list is under the total of 50 states
    # Create prompt pop up box and assign input variable & add a "score"
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} States Correct",
                                    prompt="What's another state's name?").lower()

    # Convert all_states to lowercase for case-insensitive comparison
    all_states_lower = [state.lower() for state in all_states]

    if answer_state == "exit":  # option to exit and report
        missing_states = []  # create new list for missing states
        for state in all_states:  # for every state in the all_states list
            if state not in guessed_states:  # if it is not in the list of guessed states
                missing_states.append(state)  # add the missed state to the missing_states list
        missed_data = pandas.DataFrame(missing_states)  # create a data frame for that missing_states list
        missed_data.to_csv("missing_states.csv")  # save new missed_data list to a csv
        print(missed_data)
        break

    # if answer_state is one of the states in all the states of the csv file
    # if they go it right:
    # Create a turtle to write the name of the state at the coordinates
    if answer_state in all_states_lower:
        # find correct capitalized version of the state.
        correct_state = data[data.state.str.lower() == answer_state].state.item()
        guessed_states.append(correct_state)  # append the state to guessed_states list
        t = turtle.Turtle()  # create new turtle
        t.hideturtle()  # hide turtle
        t.penup()  # penup so it doesn't draw
        # check if the answer matches a state in the list assign to variable
        state_data = data[data.state.str.lower() == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())  # go to the coordinates of the state by single item in series
        t.write(state_data.state.item())  # write the name of the state


