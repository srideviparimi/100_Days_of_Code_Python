class QuizBrain:
    def __init__(self,q_list,q_no=0,score=0):
        self.q_no=q_no
        self.q_list=q_list
        self.score=score
    def next_question(self):
        """always returns the next question object from the list"""
        current_question=self.q_list[self.q_no]
        self.q_no+=1
        user_answer=input(f"Q{self.q_no}:{current_question.text}? True/False: ")
        self.check_answer(user_answer,current_question.answer)

    def still_have_questions(self):
        return self.q_no<len(self.q_list)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("You are right")
            self.score+=1
        else:
            print("Oops You are wrong")
        print(f"The right answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.q_no}")

    def get_final_score(self):
        return self.score
