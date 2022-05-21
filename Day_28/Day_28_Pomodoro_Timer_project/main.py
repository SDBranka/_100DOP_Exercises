import tkinter
import math


def add_checkmark(marks_list):
    marks_list.append("✔")
    return marks_list


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # print(count)
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60


    canvas.itemconfig(f"{count_minutes}:{count_seconds}", text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx = 108, pady = 54, bg = YELLOW)

# canvas
# so that we can use an image in the window
# highlightthickness = 0 to get rid of visible
# border around the canvas
canvas = tkinter.Canvas(width=200, height=226, bg = YELLOW, highlightthickness = 0)
tomato_img = tkinter.PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 135, text = "00:00", 
                    fill = "white", 
                    font = (FONT_NAME, 35, "bold")
)
# canvas.pack()
canvas.grid(row = 1, column = 1)




#"Timer" label
timer_label = tkinter.Label(text = "Timer", 
                            font = ("Arial", 35, "normal"), 
                            fg = GREEN, bg = YELLOW
)
timer_label.grid(row = 0, column = 1)

# start button
start_button = tkinter.Button(text = "Start",
                                command = start_timer,
                                font = ("Arial", 18, "normal"), 
                                fg = "white", bg = "blue"
)
start_button.grid(row = 2, column = 0)

# reset button
reset_button = tkinter.Button(text = "Reset",
                                font = ("Arial", 18, "normal"),
                                fg = "white", bg = "blue"
)
reset_button.grid(row = 2, column = 2)

# check marks
# marks = ["✔", "✔"]
marks = []
check_marks = tkinter.Label(text = marks, 
                            font = ("Arial", 16, "bold"),
                            fg = GREEN, bg = YELLOW
)
check_marks.grid(row = 3, column = 1)





window.mainloop()