from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    question_new = Question(question['text'], question['answer'])
    question_bank.append(question_new)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print(f"You've completed the quiz\n"
      f"Your final score was: {quiz.score}/{quiz.question_number}\n")
