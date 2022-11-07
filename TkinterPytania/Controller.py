import random
import tkinter.messagebox as msb
import tkinter.filedialog as fd
from View import View, GameMenu
from Answers import Answers
from FileInfo import FileInfo
from QuestionStatistics import QuestionStatistics
from MySqlConnector import MySqlConnector
from ParseFile import ParseFile


class Controller:
    def __init__(self):
        self._my_sql_connector = MySqlConnector(self)
        self._all_players = self._my_sql_connector.give_players()
        self._view = View(self)
        self._name = "default"
        self._user_id = None
        self._user_points = 0
        self._filename = None
        self._questions_dict = None
        self._question = None
        self._num_of_q = None
        self._answers = Answers()
        self._question_statistics = None
        self._user_pointed_good_answer = None

    def main(self):
        self._view.main()

    def enter_game(self, name):
        self._name = name
        self._prepare_for_game()
        self._view.show_frame(GameMenu)

    def _prepare_for_game(self):
        user_id_user_points = self._my_sql_connector.give_user_id(self._name)
        self._user_id = user_id_user_points[0]
        self._user_points = user_id_user_points[1]

    def back_to_main_menu(self):
        self._view.destroy()
        new_controller = Controller()
        new_controller.main()

    def add_player(self, name):
        self._my_sql_connector.add_player(name)
        self.enter_game(name)

    def delete_player(self, name):
        self._my_sql_connector.delete_player_from_db(name)
        self._all_players.remove(f"{name}")
        self._view.main_menu_frame.combobox_players_already_played['values'] = self._all_players
        self._view.delete_user_frame.combobox_players_already_played['values'] = self._all_players
        self._view.delete_user_frame.combobox_players_already_played.set("")

    def choose_file_with_questions(self):
        filename = fd.askopenfilename(filetypes=[("Plik tekstowy", "*.txt")])
        self._filename = filename
        self._questions_dict = self.give_questions_dict_from_file()
        self.answer_question()

    def give_questions_dict_from_file(self):
        file = FileInfo(self._filename)
        set_parser = ParseFile(ParseFile.choose_parser(file))
        questions_dict = set_parser.parse_file(file)
        return questions_dict

    def answer_question(self):
        self.draw_question()
        q_and_a = self._question.give_question_and_answers()
        self._view.game_menu_frame.show_question(q_and_a)
        single_question_statistics = self._my_sql_connector.give_question_statistics(self._user_id, self._num_of_q)
        if single_question_statistics:
            self._question_statistics = QuestionStatistics(single_question_statistics[0])
        else:
            empty_scores = [0, 0, 0, None, None]
            self._question_statistics = QuestionStatistics(empty_scores)
        self._view.game_menu_frame.show_answer_sheet()

    def draw_question(self):
        possible_numbers = list(self._questions_dict.keys())
        random_question = random.choice(possible_numbers)
        self._question = self._questions_dict[random_question]
        self._num_of_q = self._question.give_question_number()

    # TODO 1 wariant gdzie dla odpowiedzi nie jest tworzona klasa, odpowiedź pobierana jest z checkboxów
    #  i przechowywana w marked_answers
    def confirm_answer(self):
        marked_answers = self._view.game_menu_frame.give_marked_answers()
        if True in marked_answers:
            self._question_statistics.update_tries_stats()
            self._check_answer(marked_answers)
        else:
            msb.showinfo("", "Nie udzieliłe/aś odpowiedzi!")

    def _check_answer(self, marked_answers):
        correct_answers = self._question.give_correct_answers()
        if correct_answers == marked_answers:
            self._update_scores_good_answer()
            self._user_pointed_good_answer = True
        else:
            self._update_scores_bad_answer()
            self._user_pointed_good_answer = False
        self._my_sql_connector.save_question_statistics(self._user_id, self._num_of_q)
        self._my_sql_connector.save_user_points(self._user_points, self._name)
        self._show_question_statistics()


    # TODO 2 wariant gdzie dla odpowiedzi tworzona jest klasa - dodatkowe 2 metody zaznaczenia i zwrotu wskazanych odpowiedzi
    # def confirm_answer(self):
    #     self.mark_user_answers()
    #     marked_answers = self._answers.give_marked_answers()
    #     if True in marked_answers:
    #         self._question_statistics.update_tries_stats()
    #         self.check_answer()
    #     else:
    #         msb.showinfo("", "Nie udzieliłe/aś odpowiedzi!")
    #
    # def mark_user_answers(self):
    #     marked_answers = self._view.game_menu_frame.give_marked_answers()
    #     self._answers.mark_answers(marked_answers)

    def _update_scores_good_answer(self):
        self._question_statistics.update_win_stats()
        self._user_points += 1

    def _update_scores_bad_answer(self):
        self._question_statistics.update_fail_stats()
        self._user_points -= 1

    def _show_question_statistics(self):
        self._view.game_menu_frame.show_question_statistics(self._question_statistics, self._user_pointed_good_answer)

    def is_player_want_continue(self, player_want_continue):
        if player_want_continue:
            self.answer_question()
        else:
            self.back_to_main_menu()


if __name__ == "__main__":
    controller = Controller()
    controller.main()
