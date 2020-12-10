from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

web_entry = Entry(width=45)
web_entry.grid(column=1, row=1, columnspan=2)

mail_entry = Entry(width=45)
mail_entry.grid(column=1, row=2, columnspan=2)
mail_entry.insert(0, "user@gmail.com")

password_entry = Entry(width=27)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", bg="white")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=38, bg="white")
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
