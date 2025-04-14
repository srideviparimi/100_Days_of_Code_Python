from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank=[]
for question in question_data:
    #TODO :"create question object for each item and append it to question bank")
    new_question_obj=Question(question["question"],question["correct_answer"])
    question_bank.append(new_question_obj)

#question bank have all the question objects ready
#TODO : "create a quiz brain obj that takes question_bank list and have next question()
quiz_brain_obj=QuizBrain(question_bank)

while quiz_brain_obj.still_have_questions():
    answer=quiz_brain_obj.next_question()

print(f" You have completed the game . Your final score is {quiz_brain_obj.get_final_score()}/{len(question_bank)}")