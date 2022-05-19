import tkinter


# take in an input and, on button click, 
# convert the entered number from miles to 
# Km
def button_clicked():
    miles_entered = float(miles_input.get())
    km_answer = miles_entered * 1.609344
    answer_label["text"] = round(km_answer, 2)
    # answer_label.config(text = round(km_answer, 2))

# build window
window = tkinter.Tk()
window.title("Miles to Km Converter")
# add padding between the window frame and the elements
window.config(padx = 27, pady = 27)

# Entry
miles_input = tkinter.Entry(width = 7)
miles_input.grid(row = 0, column = 1)

# label 1
miles_label = tkinter.Label(text = "Miles")
miles_label.grid(row = 0, column = 2)

# label 2
equal_label = tkinter.Label(text = "is equal to")
equal_label.grid(row = 1, column = 0)

# label 3
answer_label = tkinter.Label(text = "0")
answer_label.grid(row = 1, column = 1)

# label 4
km_label = tkinter.Label(text = "Km")
km_label.grid(row = 1, column = 2)

# button
button = tkinter.Button(text = "Calculate",
                        command = button_clicked,
                        fg = "white",
                        bg = "blue"
)
button.grid(row = 2, column = 1)


window.mainloop()
