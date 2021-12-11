from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question["question"]
    answer = question["correct_answer"]
    question_bank.append(Question(text, answer))

new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_questions():
    new_quiz.next_question()
print(f"You've completed the quiz. Thank you for playing.")
