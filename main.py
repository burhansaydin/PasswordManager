from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for a in range(randint(8, 10))]

    password_list += [choice(symbols) for b in range(randint(2, 4))]

    password_list += [choice(numbers) for c in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.delete(0, END)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def find_info():
    website = web_entry.get()
    try:
        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email : {email}\nPassword : {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exist.")


def add():
    websites = web_entry.get()
    mail = mail_entry.get()
    password = password_entry.get()
    new_data = {
        websites: {
            "email": mail,
            "password": password,
        }
    }

    if websites == "" or password == "":
        messagebox.showwarning(title="Opps", message="There are empty details")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            mail_entry.delete(0, END)
            mail_entry.insert(0, "user@gmail.com")
            messagebox.showinfo(title='Success', message=f"Added {websites} to the data store")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg="white")


canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)


web_label = Label(text="Website:")
web_label.grid(column=0, row=1)


mail_label = Label(text="Email/Username:")
mail_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

web_entry = Entry(width=27)
web_entry.grid(column=1, row=1)
web_entry.focus()

mail_entry = Entry(width=45)
mail_entry.grid(column=1, row=2, columnspan=2)
mail_entry.insert(0, "user@gmail.com")

password_entry = Entry(width=27)
password_entry.grid(column=1, row=3)


generate_button = Button(text="Generate Password", bg="white", command=generate_password)
generate_button.grid(column=2, row=3)

search_button = Button(text="Search", width=14, bg="white", command=find_info)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=38, bg="white", command=add)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
