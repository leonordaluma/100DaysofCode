from scoreboard import Scoreboard
import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
st = turtle.Turtle()
st.hideturtle()

data = pandas.read_csv("50_states.csv")
total_states = len(data.state)
score = 0
correct_guesses = []

def write_guess(guess):
    st.penup()
    sf = data[data.state == guess]
    x_cor = int(sf.x)
    y_cor = int(sf.y)
    st.goto(x_cor, y_cor)
    st.write(guess)
    correct_guesses.append(guess)

is_game_on = True
while is_game_on:
    guess = screen.textinput(title=f"{score}/{total_states} States Correct", prompt="What's another state's name?").title()
    for s in data.state:
        if guess == s:
            write_guess(guess)
            score += 1
            
            

        