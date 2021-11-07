from tkinter import *
from tkinter import messagebox

FONT = ("Arial", 14, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()


    # if len(website) == 0 or len(password) == 0:
    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {email} \nPassword: {password} \nIs this ok?")
        if is_ok:
            with open("data.txt","a") as file:
                print(file.write(f"{website} | {email} | {password}\n"))
            website_entry.delete(0,END)
            password_entry.delete(0,END)
        # ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_text = Label(text="Website: ")
website_text.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=3)

email_text = Label(text="Email/Username:")
email_text.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.insert(END, "leonordaluma@gmail.com")
email_entry.grid(row=2, column=1, columnspan=3)

password_text = Label(text="Password: ")
password_text.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_btn = Button(text="Generate Password")
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save_to_file)
add_btn.grid(row=4, column=1, columnspan=2)




window.mainloop()