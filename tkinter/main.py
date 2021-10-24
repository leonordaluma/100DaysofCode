import tkinter

window = tkinter.Tk()
window.title("GUI")
window.minsize(width=500, height=300)

# label 
my_lable = tkinter.Label(text="Label", font=("Poppins", 14))
my_lable.pack(side="left")

window.mainloop()
