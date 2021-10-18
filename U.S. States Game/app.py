from turtle import Turtle, Screen
import pandas as pd

turtle = Turtle()
screen = Screen()

correct_answers = 0
IMAGE = "blank_states_img.gif"

data = pd.read_csv("50_states.csv")
data["state"] = data["state"].str.lower()
states = data["state"].to_list()

turtle.hideturtle()
turtle.penup()
turtle.speed(0)

screen.title("U.S. States Game")
screen.setup(width=0.53, height=0.65)
screen.bgpic(IMAGE)

while correct_answers < 50:
    answer_state = screen.textinput(
        f"{correct_answers}/50 States Correct", "What's the state name?")

    if answer_state in states:

        state = data[data["state"] == answer_state]

        turtle.goto(int(state["x"]), int(state["y"]))
        turtle.write(answer_state)

        correct_answers += 1

# The window does not get closed until you click inside the window
screen.exitonclick()
