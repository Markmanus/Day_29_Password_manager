from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json




# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showinfo(title="Success", message="Password saved")

    ############################## JSON better option, tested ##############################
    # new_data = {
    #     website: {
    #         "email": email,
    #         "password": password,
    #     }
    # }
    # if len(website) == 0 or len(password) == 0:
    #     messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    # elif "@" not in email:
    #     messagebox.showinfo(title="Oops", message="Please make sure you have entered a valid email")
    # else:
    #     try:
    #         with open("data.json", "r") as data_file:
    #             # Reading old data
    #             data = json.load(data_file)
    #     except FileNotFoundError:
    #         with open("data.json", "w") as data_file:
    #             json.dump(new_data, data_file, indent=4)
    #     else:
    #         # Updating old data with new data
    #         data.update(new_data)
    #
    #         with open("data.json", "w") as data_file:
    #             # Saving updated data
    #             json.dump(data, data_file, indent=4)
    #     finally:
    #         website_entry.delete(0, END)
    #         password_entry.delete(0, END)
    #         messagebox.showinfo(title="Success", message="Password saved")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
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

email_entry = Entry(width=35, bg="white",  borderwidth=1, relief="solid")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "insert email")


password_entry = Entry(width=21 ,bg="white", borderwidth=1, relief="solid")
password_entry.grid(column=1, row=3, sticky="EW")
#buttons
generate_password_button = Button(width=14 ,text="Generate Password", bg="white")
generate_password_button.grid(column=2, row=3, sticky="W")
add_button = Button(width=36, text="Add", bg="white", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="W")


window.mainloop()