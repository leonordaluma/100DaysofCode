import tkinter

window = tkinter.Tk()
window.title("GUI")
window.minsize(width=500, height=300)

# label 
my_label = tkinter.Label(text="Label", font=("Poppins", 14))
my_label.pack(side="left")

my_label["text"] = "New Label"
my_label.config(text="New Text")
window.mainloop()
