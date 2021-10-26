from tkinter import *

def miles_to_km():
    miles_value = float(miles.get())
    km_result = round(miles_value * 1.609)
    km_value.config(text=f"{km_result}")

window = Tk()
window.title("Mile to KM converter")
window.minsize(width=200, height=100)
window.config(padx=30, pady=20)

miles = Entry(width=10)
miles.insert(END, "0")
miles.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

km_value = Label(text="0")
km_value.grid(column=1, row=1)

km = Label(text="KM")
km.grid(column=2, row=1)

calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row=2)



window.mainloop()
