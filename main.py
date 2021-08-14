import turtle
import pandas as pd

screen = turtle.Screen()
# screen.title(f"U.S. States Game, Current Score: {SCORE}")
image = "India.gif"
screen.addshape(image)
turtle.shape(image)

SCORE = 0

data = pd.read_csv("India_States.csv")
all_states = data.state.to_list()


def update_score():
    global SCORE
    SCORE += 1


game_on = True

while game_on == True:
    screen.title(f"India States Game, Current Score: {SCORE}")
    answer_state = screen.textinput(
        title="Guess the State", prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state in all_states:
        update_score()
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

    if SCORE == 50:
        game_on = False


screen.exitonclick()
