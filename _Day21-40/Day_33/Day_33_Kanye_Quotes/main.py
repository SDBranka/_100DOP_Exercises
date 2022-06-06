import tkinter
import requests


def get_quote():
    # make a get() request to the Kanye Rest API
    response = requests.get(url="https://api.kanye.rest")
    # raise an exception if the request returned an unsuccesful status code
    response.raise_for_status()
    # parse the JSON to obtain the quote text
    quote = response.json()["quote"]
    # print(f"quote:\n{quote}")
    # Display the quote in the canvas' quote_text widget
    canvas.itemconfig(quote_text, 
                        text=quote, 
                        fill="black"
        )


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=300, height=414)
background_img = tkinter.PhotoImage(file="images/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, 
                                text="Click Kanye to get a quote", 
                                width=250, 
                                font=("Arial", 30, "bold"), 
                                fill="white"
)
canvas.grid(row=0, column=0)

kanye_img = tkinter.PhotoImage(file="images/kanye.png")
kanye_button = tkinter.Button(image=kanye_img, 
                                highlightthickness=0, 
                                command=get_quote
)
kanye_button.grid(row=1, column=0)


window.mainloop()