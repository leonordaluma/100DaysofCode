from tkinter import *

window = Tk()
window.title("GUI")
window.minsize(width=500, height=300)

# label 
my_label = Label(text="Label", font=("Poppins", 14))
my_label.pack()

my_label["text"] = "New Label"
my_label.config(text="New Text")

# buttons
def button_clicked():
    my_label.config(text="Button Got Clicked!")

button = Button(text="Click Me", command=button_clicked)
button.pack()




window.mainloop()
