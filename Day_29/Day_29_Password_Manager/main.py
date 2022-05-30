import tkinter
from tkinter import messagebox
import random
import pyperclip


LABEL_FONT = ("Arial", 12, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pw_button_clicked():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for i in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for i in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    # combine the password_list to a single string with no separation between elements
    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_input.insert(tkinter.END, password)
    # stores the password to users clipboard to enable pasting elsewhere
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# on add_button click take in the inputs and 
# add the entries to data.txt in format:
# Company | email | password
def add_button_clicked():
    website_entered = website_input.get()
    email_entered = email_input.get()
    password_entered = password_input.get()

    if len(website_entered) == 0 or len(email_entered) == 0 or len(password_entered) == 0:
        messagebox.showerror('error', 'No field may be left empty')
    else:
        # show a message box to confirm inputs
        # messagebox.showinfo(title = "Title", message = "Message")
        # askokcancel returns a boolean value
        is_ok = messagebox.askokcancel(title = website_entered, 
                                message = f"These are the details entered:\n Email entered: {email_entered}\nPassword entered: {password_entered}\n Is it okay to save?"
        )
        if is_ok:
            # append data to file
            with open("data.txt", "a") as file:
                file.write(f"{website_entered} | {email_entered} | {password_entered}\n")
                # clear the input fields (from first character to the last)
                website_input.delete(0, tkinter.END)
                password_input.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #

# build window
window = tkinter.Tk()
window.title("Password Manager")
# add padding between the window frame and the elements
window.config(padx = 27, pady = 27)

# column 0
# website label
website_label = tkinter.Label(text = "Website:",
                                font = LABEL_FONT
)
website_label.grid(row = 1, column = 0)

# email label
email_label = tkinter.Label(text = "Email/Username:",
                                font = LABEL_FONT
)
email_label.grid(row = 2, column = 0)

# password label
password_label = tkinter.Label(text = "Password:",
                                font = LABEL_FONT
)
password_label.grid(row = 3, column = 0)

# column 1
# canvas
canvas = tkinter.Canvas(width = 207, height = 207,
                        highlightthickness = 0
)
mypass_img = tkinter.PhotoImage(file = "logo.png")
canvas.create_image(102, 102, image = mypass_img)
canvas.grid(row = 0, column = 1)

# website entry
website_input = tkinter.Entry(width = 36)
# place the tying cursor inside the field
website_input.focus()
website_input.grid(row = 1, column = 1, columnspan = 2)

# email entry
email_input = tkinter.Entry(width = 36)
# prepopulate field with the most common entry
# email_input.insert(index(where to insert text), field(the text to insert))
# 0 means the first character END starts it at the end
email_input.insert(tkinter.END, "exampleEmail@something.com")
email_input.grid(row = 2, column = 1, columnspan = 2)

# password entry
password_input = tkinter.Entry(width = 21)
password_input.grid(row = 3, column = 1)

# add_button
add_button = tkinter.Button(text = "Add",
                        command = add_button_clicked,
                        fg = "white",
                        bg = "blue",
                        width = 36
)
add_button.grid(row = 4, column = 1, columnspan = 2)

# column 2
# genpass_button
genpass_button = tkinter.Button(text = "Generate Password",
                        command = gen_pw_button_clicked,
                        fg = "white",
                        bg = "blue"
)
genpass_button.grid(row = 3, column = 2)





window.mainloop()