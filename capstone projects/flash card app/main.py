from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=640, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400,300, image=card_img)
canvas.grid(column=1, row=0, columnspan=2)


# my_image = PhotoImage(file="./images/wrong.png")
# x_btn = Button(image=my_image, highlightthickness=0)
# x_btn.pack()



window.mainloop()