from Question import Question
from tkinter import messagebox as msb


class ParseTxt:
    def __init__(self, readed_file):
        self.questions_list_of_lines_readed = readed_file
        self.question_list_indexes = self.give_question_list_indexes()

    def give_question_list_indexes(self):
        question_list_indexes = []
        for line in self.questions_list_of_lines_readed:
            if len(line) == 0:
                continue
            elif line.startswith("#"):
                continue
            elif line[0].isdigit():
                question_list_index = self.questions_list_of_lines_readed.index(line)
                question_list_indexes.append(question_list_index)
        if len(question_list_indexes) == 0:
            msb.showinfo("Brak pliku", "We wskazanym pliku nie ma pytan do załadowania, wskaż inny plik.")
            raise Exception("Brak pytań w pliku")
        return question_list_indexes

    def build_questions(self):
        question_block_number = 0
        questions_dict = {}
        while question_block_number < len(self.question_list_indexes):
            new_question, question_number = self.load_one_question(question_block_number)
            good_question_block = self.check_question_block(question_number, questions_dict)
            if good_question_block:
                questions_dict[question_number] = new_question
                question_block_number += 1
            else:
                msb.showinfo("Brak pliku", "We wskazanym pliku są powtórzone pytania, wskaż inny plik.")
                raise Exception(f"Plik z zestawem pytań zawiera dwa pytania o numerze: {question_number}")
        return questions_dict

    @staticmethod
    def check_question_block(question_number, questions):
        if question_number in questions.keys():
            return False
        else:
            return True

    def load_one_question(self, question_block_number):
        q_start_index = self.question_list_indexes[question_block_number]
        q_stop_index = self.give_q_stop_index(q_start_index, question_block_number)
        question_sentence = self.questions_list_of_lines_readed[q_start_index]
        question_number, question_content = ParseTxt.divide_question_sentence(question_sentence)
        answer_a = self.questions_list_of_lines_readed[q_start_index + 1]
        answer_b = self.questions_list_of_lines_readed[q_start_index + 2]
        answer_c = self.questions_list_of_lines_readed[q_start_index + 3]
        correct_ans = self.questions_list_of_lines_readed[q_start_index + 4]
        clear_notes = self.give_clear_notes(q_start_index, q_stop_index)
        if answer_a.startswith("a. ") and answer_b.startswith("b. ") \
                and answer_c.startswith("c. ") and correct_ans.startswith("correct "):
            return Question(question_number, question_content, answer_a[3:], answer_b[3:], answer_c[3:],
                            correct_ans[8:], clear_notes), question_number
        else:
            msb.showinfo("Brak pliku", "We wskazanym pliku są błędne pytania, wskaż inny plik.")
            raise Exception(f"Błąd przy wczytywaniu pytania - wiersze {q_start_index}:{q_stop_index} pliku z pytaniami.")

    def give_q_stop_index(self, q_start_index, question_block_number):
        if q_start_index == self.question_list_indexes[-1]:
            q_stop_index = None
        else:
            q_stop_index = self.question_list_indexes[question_block_number + 1]
        return q_stop_index

    @staticmethod
    def divide_question_sentence(question_sentence):
        length_question_number = question_sentence.index(". ")
        question_number = int(question_sentence[0:length_question_number])
        question_content = question_sentence[length_question_number + 2:]
        return question_number, question_content

    def give_clear_notes(self, q_start_index, q_stop_index):
        notes = self.questions_list_of_lines_readed[q_start_index + 5:q_stop_index]
        for note in notes:
            if note.startswith("#"):
                notes.remove(note)
        for note in notes:
            if note.startswith("a. " or "b. " or "c. " or "correct "):
                msb.showinfo("Brak pliku", "We wskazanym pliku są błędne pytania, wskaż inny plik.")
                raise Exception(f"Pomiędzy wierszami {q_start_index} - {q_stop_index} znajduje się błędne pytanie")
        clear_notes = ParseTxt.remove_empty_lines(notes)
        return clear_notes

    @staticmethod
    def remove_empty_lines(notes):
        empty_line = True
        while empty_line:
            if len(notes) == 0:
                empty_line = False
            elif notes[0] == '':
                del notes[0]
            elif notes[-1] == '':
                del notes[-1]
            else:
                empty_line = False
        return notes

"""    Ten parser przekształca plik z pytaniami w formacie:
    2. Co znaczy powiedzenie „wpuścić kogoś w maliny” ?
    a. zostawić kogoś w krzakach
    b. wprowadzić kogoś w błąd
    c. spóźnić się
    correct b

    3. Kiedy Księżyc jest w pełni ?
    a. gdy ma kształt rogala
    b. gdy jest okrągły
    c. gdy wychodzi zza chmur
    correct b
    # To jest komentarz i nie będzie wczytany, poniżej jest notatka do pytania

    Wówczas to znajduje się on po przeciwnej stronie Ziemi niż Słońce i jego obszar zwrócony w stronę Ziemi jest cały przez Słońce oświetlony.
    Przeciwieństwem PEŁNI jest NÓW, kiedy to oświetlana przez Słońce jest niewidoczna z Ziemi strona Księżyca. PEŁNIA, NÓW i KWADRA to FAZY KSIĘŻYCA.

    4. Co znaczy powiedzenie „dzielić skórę na niedźwiedziu” ?
    a. kłócić się o nagrodę
    b. robić plany nie mające pokrycia w rzeczywistości
    c. zostać królem polowania
    correct b"""
