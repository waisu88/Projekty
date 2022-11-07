

class Answers:
    def __init__(self):
        self._user_marked_a = False
        self._user_marked_b = False
        self._user_marked_c = False

    def give_marked_answers(self):
        marked_answers = [self._user_marked_a, self._user_marked_b, self._user_marked_c]
        return marked_answers

    def mark_answers(self, marked_answers):
        self._user_marked_a = marked_answers[0]
        self._user_marked_b = marked_answers[1]
        self._user_marked_c = marked_answers[2]
