from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q_data in question_data:
    text = q_data["question"]
    answer = q_data["correct_answer"]
    question_bank.append(Question(text, answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("you have completed the quiz")
print(f"The final score is {quiz.score}/{quiz.question_number}")
