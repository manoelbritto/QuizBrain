class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank

    def next_question(self):
        input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)? ")
        self.question_number += 1

    def still_has_question(self):
        return len(self.question_list) > self.question_number
