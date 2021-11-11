from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
TITLE = ("Arial", 18, "italic")
WORD = ("Arial", 30, "bold")

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=0, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=640, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400,300, image=card_img)
french_text = canvas.create_text(400, 200, text="French", font=TITLE)
french_word = canvas.create_text(400, 300, text="mettre", font=WORD)
canvas.grid(column=0, row=0, columnspan=2)



wrong_image = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=wrong_image, highlightthickness=0)
wrong_btn.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_btn = Button(image=right_image, highlightthickness=0)
right_btn.grid(column=1, row=1)


window.mainloop()