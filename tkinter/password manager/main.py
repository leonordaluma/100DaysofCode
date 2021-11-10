from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
# import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, password)
    # pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password
        }
    }

    # if len(website) == 0 or len(password) == 0:
    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json","r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as file:
                json.dump(data, file, indent=4)
        finally:        
            website_entry.delete(0,END)
            password_entry.delete(0,END)
        # ---------------------------- SEARCH ------------------------------- #
def find_password():
        user_text = website_entry.get()
        
        with open("data.json", "r") as file:
            data = json.load(file)
            for val in data:
                if user_text == val:
                    website = data[val]
                    email = website["email"]
                    password = website["password"]
                    messagebox.showinfo(title=user_text, message=f"Email: {email} \nPassword: {password}")
        
        
        
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
email_text = Label(text="Email/Username:")
email_text.grid(row=2, column=0)
password_text = Label(text="Password: ")
password_text.grid(row=3, column=0)


website_entry = Entry(width=24)
website_entry.focus()
website_entry.grid(row=1, column=1)
email_entry = Entry(width=42)
email_entry.insert(END, "leonordaluma@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=24)
password_entry.grid(row=3, column=1)


search_btn = Button(text="Search", command=find_password)
search_btn.grid(row=1, column=2)
generate_btn = Button(text="Generate Password",command=generate_password)
generate_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=36, command=save_to_file)
add_btn.grid(row=4, column=1, columnspan=2)




window.mainloop()