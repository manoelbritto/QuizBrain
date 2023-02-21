class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        correct_answer = self.question_list[self.question_number].answer
        current_answer = input(f"Q.{self.question_number + 1}: "
                               f"{self.question_list[self.question_number].text} (True/False)? ")
        self.question_number += 1
        self.check_answer(current_answer, correct_answer)

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That is wrong.")
        print(f"The correct answer is {c_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")


