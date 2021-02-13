from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    Q_text = question["text"]
    Q_answer = question["answer"]
    new_question = Question(Q_text, Q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.new_question()

print("You have completed the quiz.")
print(f"Your final score is : {quiz.score}/12")