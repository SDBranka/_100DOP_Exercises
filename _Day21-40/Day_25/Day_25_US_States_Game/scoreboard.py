import turtle as t

class Scoreboard(t.Turtle):
    def __init__(self, states_names_list):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("black")
        self.score = 0
        # self.missed_states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California",
        #                         "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", 
        #                         "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", 
        #                         "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", 
        #                         "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri",
        #                         "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", 
        #                         "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", 
        #                         "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", 
        #                         "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", 
        #                         "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
        # ]
        self.missed_states = states_names_list


    def correct_guess(self, x, y, state_name):
        self.score += 1
        self.missed_states.remove(state_name)
        self.goto(x, y)
        self.write(state_name, align = "center",
                    font = ("Courier", 9, "normal")
        )
