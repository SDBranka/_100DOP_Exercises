# asking the questions

# check if the user's answer is correct

# check to see if we're at the end of the quiz


# create a class called QuizBrain
class QuizBrain:
    # write and __init__ method
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    # create a method called still_has_questions()
    # return a boolean depending on the value of question_number
    # use the while loop to show the next question until the end
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # create a method called next_question that will 
    # retrieve the item at the current question_number
    # from the question_list. Use the input()
    # function to show the user the Question text
    # and ask for their answer.
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False) ")
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        # format answers for comparison
        user_answer = user_answer.lower()
        correct_answer = correct_answer.lower()
        if user_answer == "t":
            user_answer = "true"
        if user_answer == "f":
            user_answer = "false"

        if user_answer == correct_answer:
            print("Correct!\n")
            self.score += 1
        else:
            print("Incorrect!\n")
        print(f"The correct answer is {correct_answer.title()}")
        print(f"Your score is {self.score}/{self.question_number}\n")
