from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE = ("Arial", 18, "italic")
WORD = ("Arial", 30, "bold")


def generate_word():
    data = pd.read_csv("./data/french_words.csv")
    data_dict = data.to_dict(orient='records')
    random_word = random.choice(data_dict)
    french_word = random_word["French"]
    # english_word = random_word["English"]
    canvas.itemconfig(french_text, text=f"{french_word}")


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=0, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=640, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400,300, image=card_img)
french_text = canvas.create_text(400, 200, text="French", font=TITLE)
french_text = canvas.create_text(400, 300, text=f"", font=WORD)
canvas.grid(column=0, row=0, columnspan=2)



wrong_image = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_image, highlightthickness=0, command=generate_word)
wrong_btn.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_image, highlightthickness=0, command=generate_word)
right_btn.grid(column=1, row=1)


window.mainloop()