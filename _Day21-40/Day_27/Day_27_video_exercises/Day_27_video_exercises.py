import tkinter

window = tkinter.Tk()

window.title("My First GUI Project")
window.minsize(width = 500, height = 300)

# label
my_label = tkinter.Label(text = "I am a label", font = ("Arial", 24, "bold"))
# place my_label onto screen and 
# horizontally center it 
# my_label.pack()
# my_label.pack(side = "left")
my_label.pack(expand = True)

# keep window onscreen and listens for what
# user will do to interact with it
window.mainloop()





