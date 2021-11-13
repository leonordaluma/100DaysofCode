from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE = ("Arial", 18, "italic")
WORD = ("Arial", 30, "bold")
FLIP_SEC = 3
t = None


def select_random_word():
    data = pd.read_csv("./data/french_words.csv")
    data_dict = data.to_dict(orient='records')
    return random.choice(data_dict)
    

def generate_word():
    window.after_cancel(window)
    word = select_random_word()
    canvas.itemconfig(canvas_img, image=card_img)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(french_word, text=f"{word['French']}", fill="black")
    delay()

def flip_card():
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(french_word, text=f"{word['English']}", fill="white")
    


def delay():
    # delay_time = FLIP_SEC * 60
    window.after(3000, flip_card)
    

word = select_random_word()
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=0, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=640, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400,300, image=card_img)
canvas_title = canvas.create_text(400, 200, text="French", font=TITLE)
french_word = canvas.create_text(400, 300, text=f"{word['French']}", font=WORD)
delay()
canvas.grid(column=0, row=0, columnspan=2)



wrong_image = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_image, highlightthickness=0, command=generate_word)
wrong_btn.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_image, highlightthickness=0, command=generate_word)
right_btn.grid(column=1, row=1)




window.mainloop()