from typing import List


class Question:
    def __init__(self, num_of_q, q_content, ans_a, ans_b, ans_c, correct_ans, notes):
        self._num_of_q = num_of_q
        self._q_content = q_content
        self._ans_a = ans_a
        self._ans_b = ans_b
        self._ans_c = ans_c
        self._notes = notes
        self._a_is_correct = "a" in correct_ans
        self._b_is_correct = "b" in correct_ans
        self._c_is_correct = "c" in correct_ans

    def give_question_number(self):
        question_number = self._num_of_q
        return question_number

    def give_correct_answers(self):
        correct_answers = [self._a_is_correct, self._b_is_correct, self._c_is_correct]
        return correct_answers

    def give_question_and_answers(self) -> List:
        return [self._num_of_q, self._q_content, self._ans_a, self._ans_b, self._ans_c]
