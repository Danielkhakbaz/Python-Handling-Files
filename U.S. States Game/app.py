import pandas as pd
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

answer_state = ""
correct_answers = 0
IMAGE = "blank_states_img.gif"

data = pd.read_csv("50_states.csv")

# Make the state names lowercase
data["state"] = data["state"].str.lower()

# Make the state DataFrame to a list
listed_states = data["state"].to_list()

# Set the screen title
screen.title("U.S. States Game")

# Set the screen size
screen.setup(width=0.53, height=0.65)

# The Actuall Code for the game
screen.bgpic(IMAGE)
# turtle.shape(IMAGE)

while correct_answers < 50:
    answer_state = screen.textinput(
        f"{correct_answers}/50 States Correct", "What's the state name?")

    if answer_state in listed_states:
        turtle.hideturtle()
        turtle.penup()
        
        state = data[data["state"] == answer_state]
        
        turtle.goto(int(state["x"]), int(state["y"]))
        turtle.write(answer_state)

        correct_answers += 1

# The window does not get closed until you click inside the window
screen.exitonclick()
