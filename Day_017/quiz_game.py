from question_model import Question
from quiz_data import question_data
from quiz_brain import QuizBrain
from more_quiz_data import question_data

# create question bank
question_bank = []

# for loop to iterate over the question_data.
for question in question_data:

    # commented out to test the next block with the more_quiz_data file
    # question_text = question["text"]
    # question_answer = question["answer"]

    # using the more_quiz_data file
    question_text = question["question"]
    question_answer = question["correct_answer"]

    # create a Question object from each entry in question_data.
    new_question = Question(question_text, question_answer)

    # append each Question object to the question_bank
    question_bank.append(new_question)

# Create new quiz
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz. Your final score is {quiz.score}/{quiz.question_number}")





