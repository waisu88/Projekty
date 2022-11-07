from typing import List
import datetime


class QuestionStatistics:
    def __init__(self, single_question_statistics):
        self._number_of_tries = single_question_statistics[0]
        self._number_of_wins = single_question_statistics[1]
        self._number_of_fails = single_question_statistics[2]
        self._date_of_last_win = single_question_statistics[3]
        self._date_of_last_fail = single_question_statistics[4]

    def update_number_of_tries(self):
        self._number_of_tries += 1

    def update_win_stats(self):
        self._number_of_wins += 1
        self._date_of_last_win = datetime.datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")

    def update_fail_stats(self):
        self._number_of_fails += 1
        self._date_of_last_fail = datetime.datetime.now().replace(microsecond=0).strftime("%d/%m/%Y %H:%M:%S")

    def update_tries_stats(self):
        self._number_of_tries += 1

    def give_question_statistics(self) -> List:
        question_statistics = [self._number_of_tries, self._number_of_wins,
                               self._number_of_fails, self._date_of_last_win, self._date_of_last_fail]
        return question_statistics
