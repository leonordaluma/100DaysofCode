from tkinter import *

window = Tk()
window.title("GUI")
window.minsize(width=500, height=500)

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
# line 1 character 0
print(text.get("1.0", END))
text.pack()

# Spinbox
def spinbox_value():
    print(spinbox.get())
spinbox = Spinbox(from_= 0, to=10, width=5, command=spinbox_value)
spinbox.pack()

# Scale
scale = Scale(from_=0, to=20)
scale.pack()

# Checkbutton
def checkbutton_used():
    print(check_state.get())
check_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=check_state, command=checkbutton_used)
checkbutton.pack()

# Radiobutton
def radiobutton_value():
    print(radio_state.get())

radio_state = IntVar()
r_btn1 = Radiobutton(text="True", value=1, variable=radio_state, command=radiobutton_value)
r_btn2 = Radiobutton(text="False", value=2, variable=radio_state, command=radiobutton_value)
r_btn1.pack()
r_btn2.pack()

# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=3)
cats = ["Grey", "Harley", "Mufasa"]
for c in cats:
    listbox.insert(cats.index(c), c)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()






window.mainloop()
