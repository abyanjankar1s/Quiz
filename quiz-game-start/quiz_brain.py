
class QuizBrain:
  def __init__(self, question_list):
    self.question_num = 0 
    self.score = 0
    self.question_list = question_list 

  def still_has_question(self):
    return self.question_num < len(self.question_list) 
      
  def next_question(self):
    curr_question = self.question_list[self.question_num]
    self.question_num += 1 
    user_ans = input(f"Q.{self.question_num}: {curr_question.text} (True/False?) ") 
    self.check_answer(user_ans, curr_question.answer)
    
  def check_answer(self, user_ans, correct_ans):
    if user_ans.lower() == correct_ans.lower():
      self.score += 1 
      print("You are correct!")
    else:
      print("You are Incorrect!")
    print(f"Your Score: {self.score}/{self.question_num}")

    
    
    