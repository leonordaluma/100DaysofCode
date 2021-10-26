from tkinter import *

def button_clicked():
    new_text = entry.get()
    my_label.config(text=new_text)

window = Tk()
window.title("GUI")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# label 
my_label = Label(text="Label", font=("Poppins", 14))
my_label.grid(column=0, row=0)

my_label["text"] = "New Label"
my_label.config(text="New Text")

# buttons

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
button.config(padx=100, pady=20)

button2 = Button(text="New Button")
button2.grid(column=2, row=0)
# entry
entry = Entry(width=10)
entry.grid(column=3, row=2)

window.mainloop()
