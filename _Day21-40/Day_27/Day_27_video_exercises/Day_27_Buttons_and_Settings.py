import tkinter

window = tkinter.Tk()

window.title("My First GUI Project")
window.minsize(width = 500, height = 300)

# label
my_label = tkinter.Label(text = "I am a label", font = ("Arial", 24, "bold"))
# place my_label onto screen and horizontally
# center it 
my_label.pack()
# my_label.pack(side = "left")
# my_label.pack(expand = True)

my_label["text"] = "New Text"
my_label.config(text = "New Text Again")


# button
# def button_clicked():
#     print("I got clicked")

# button = tkinter.Button(text = "Click Me!", command = button_clicked)
# button.pack()

# # change the label with a button click
# def button_clicked():
#     my_label["text"] = "Button got clicked"

# button = tkinter.Button(text = "Click Me!", command = button_clicked)
# button.pack()


# Entry
input = tkinter.Entry(width = 10)
input.pack()
# print(input.get())

# take in an input and, on button click, 
# use it to replace label text

def button_clicked():
    my_label["text"] = input.get()

button = tkinter.Button(text = "Click Me!", 
                        command = button_clicked,
                        fg = "white",
                        bg = "black"
)
button.pack()






# keep window onscreen and listens for what
# user will do to interact with it
window.mainloop()





