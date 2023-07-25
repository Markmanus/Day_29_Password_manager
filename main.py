from tkinter import *



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")
window.minsize(width=200, height=200)

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)


email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3, sticky="w")


#entries
website_entry = Entry(width=35, bg="white", highlightthickness=0, borderwidth=1, relief="solid")
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_entry = Entry(width=35, bg="white", highlightthickness=0, borderwidth=1, relief="solid")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")


password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")
#buttons
generate_password_button = Button(width=14 ,text="Generate Password", bg="white")
generate_password_button.grid(column=2, row=3, sticky="W")
add_button = Button(width=36, text="Add", bg="white")
add_button.grid(column=1, row=4, columnspan=2, sticky="W")


window.mainloop()