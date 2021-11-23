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
    

while len(correct_guesses) < 50:
    guess = screen.textinput(title=f"{len(correct_guesses)}/{total_states} States Correct", prompt="What's another state's name?").title()

    if guess == "Exit":
        state_data = [s for s in data.state if s not in correct_guesses]
        df = pandas.DataFrame(state_data)
        df.to_csv("learn.csv")
        break

    for s in data.state:
        if guess == s:
            if guess not in correct_guesses:
                correct_guesses.append(guess)
                write_guess(guess)
