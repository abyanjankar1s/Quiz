from question_model import Question 
from data import question_data 
from quiz_brain import QuizBrain 

question_bank = [] 

for question in question_data:
  text = question["question"]
  answer = question["correct_answer"]
  new_question = Question(text,answer)
  question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
  quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score is {quiz.score}/{len(question_bank)}")

