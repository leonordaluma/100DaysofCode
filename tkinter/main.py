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
    new_text = entry.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.pack()

# entry
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with")
entry.pack()

# textbox
text = Text(height=5, width=30)
text.focus()
text.insert(END,"this is a text")
text.pack()








window.mainloop()
