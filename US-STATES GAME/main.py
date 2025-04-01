import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

#writer for turtle
writer = t.Turtle()
writer.hideturtle()
writer.penup()

#Reading from csv
states_data = pd.read_csv("50_states.csv")

#Get hold of state column
state_column = states_data["state"]

#Function for writing text on x,y coordinates
def write_state(x, y, text):
    writer.goto(x, y)
    writer.write(text, align="center")

guesses = 0
correct_guesses = []
score = 0
all_states = states_data.state.to_list()
states_not_guessed = []

#Prompt for guessing the state
while guesses <= len(states_data.state):
    guess_state = screen.textinput(title=f"{guesses} / 50 states guessed", prompt="What's the next state name?")
    guess_state_title = guess_state.title()

    #Check if guess exists in states
    if guess_state_title == "Exit":
        for state in all_states:
            if state not in correct_guesses:
                states_not_guessed.append(state)
        states_to_learn_df = pd.DataFrame(states_not_guessed)
        states_to_learn_df.to_csv("states_to_learn.csv")
        break
    elif guess_state_title in state_column.values:
        x_coord = states_data[states_data.state == guess_state_title].x.item()
        y_coord = states_data[states_data.state == guess_state_title].y.item()
        write_state(x_coord, y_coord, guess_state_title)
        correct_guesses.append(guess_state_title)
        guesses += 1
    else:
        continue




screen.exitonclick()