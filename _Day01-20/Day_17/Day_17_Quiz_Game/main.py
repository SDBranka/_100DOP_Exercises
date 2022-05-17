from question_model import Question
from data import question_data, question_data1
from quiz_brain import QuizBrain


# write a for loop to iterate over the question_data.
# create a Question object from each entry in question_data.
# append the Question object to the questions_bank
# question_bank = []
# for question in question_data:
#     question_text = question["text"]
#     question_answer = question["answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

question_bank = []
for question in question_data1:
    question_bank.append(Question(question["text"], question["answer"]))

# print(question_bank)
# print(question_bank[0].answer)

# initialize a quiz
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is {quiz.score}/{len(question_bank)}")



