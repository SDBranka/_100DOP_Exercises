import tkinter


window = tkinter.Tk()

window.title("My First GUI Project")
window.minsize(width = 500, height = 300)
# add padding between the window frame and the elements
window.config(padx = 60, pady = 60)

# # Using pack()
# # label
# my_label = tkinter.Label(text = "I am a label", font = ("Arial", 24, "bold"))
# my_label["text"] = "New Text"
# # place my_label onto screen and horizontally
# # center it 
# my_label.pack(side = "left")

# # button
# # change the label with a button click
# def button_clicked():
#     my_label["text"] = "Button got clicked"

# button = tkinter.Button(text = "Click Me!", command = button_clicked)
# button.pack(side="left")

# # entry
# input = tkinter.Entry(width = 10)
# print(input.get())
# input.pack(side="left")


# using place()
# we can use x, y coordinates (0,0 is top left corner)
# label
my_label = tkinter.Label(text = "I am a label", font = ("Arial", 24, "bold"))
my_label["text"] = "New Text"
# my_label.place(x = 100, y = 0)


# using grid
# label
my_label = tkinter.Label(text = "I am a label", font = ("Arial", 24, "bold"))
my_label["text"] = "New Text"
# add padding around an element
my_label.config(padx = 60, pady = 60)
my_label.grid(column = 0, row = 0)

# new button
new_button = tkinter.Button(text = "new button")
# add padding around text inside of button
new_button.config(padx = 60, pady = 60)
new_button.grid(column = 2, row = 0)


# button
# change the label with a button click
def button_clicked():
    my_label["text"] = "Button got clicked"

button = tkinter.Button(text = "Click Me!", command = button_clicked)
button.grid(column = 1, row = 1)

# entry
input = tkinter.Entry(width = 10)
print(input.get())
input.grid(column = 3, row = 2)










# keep window onscreen and listens for what
# user will do to interact with it
window.mainloop()








