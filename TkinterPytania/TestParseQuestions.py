import pytest
from ParseQuestions import ParseQuestions


class TestParseQuestions:
    list_with_questions = ["1. Linia pierwsza", "a. Linia druga", "b. Linia trzecia", "c. Linia czwarta", "correct Linia piąta",
             "2. Linia pierwsza", "a. Linia druga", "b. Linia trzecia", "c. Linia czwarta", "correct Linia piąta"]
    test_questions = ParseQuestions(list_with_questions)

    def test_give_question_list_indexes(self):
        given = TestParseQuestions.test_questions.question_list_indexes
        expected = [0, 5]
        assert given == expected

    def test_build_questions(self):
        given = TestParseQuestions.test_questions.build_questions()
        expected = {}
        assert type(given) == type(expected)

    def test_duplicate_number_of_q(self):
        # dwa razy ten sam numer pytania
        list_with_duplicate_questions = ["1. Linia pierwsza", "a. Linia druga", "b. Linia trzecia", "c. Linia czwarta", "correct Linia piąta",
                               "1. Linia pierwsza", "a. Linia druga", "b. Linia trzecia", "c. Linia czwarta", "correct Linia piąta"]
        duplicate_questions = ParseQuestions(list_with_duplicate_questions)
        with pytest.raises(Exception):
            assert duplicate_questions.build_questions()

    def test_incorrectly_given_question(self):
        # w pierwszym pytaniu odpowiedź a zaczyna się błędnie od litery b
        list_with_uncorrectly_given_question = ["1. Linia pierwsza", "b. Linia druga", "b. Linia trzecia", "c. Linia czwarta",
                                         "correct Linia piąta",
                                         "2. Linia pierwsza", "a. Linia druga", "b. Linia trzecia", "c. Linia czwarta",
                                         "correct Linia piąta"]
        incorrectly_given_questions = ParseQuestions(list_with_uncorrectly_given_question)
        with pytest.raises(Exception):
            assert incorrectly_given_questions.build_questions()

    def test_question_with_no_q_number(self):
        # w drugim pytaniu odpowiedź pytanie nie zaczyna się od "liczba. " brak numeru pytania
        list_with_no_q_number = ["1. Linia pierwsza", "b. Linia druga", "b. Linia trzecia", "c. Linia czwarta",
                                         "correct Linia piąta",
                                         ". Linia pierwsza", "a. Linia druga", "b. Linia trzecia", "c. Linia czwarta",
                                         "correct Linia piąta"]
        no_q_number = ParseQuestions(list_with_no_q_number)
        with pytest.raises(Exception):
            assert no_q_number.build_questions()

    def test_clearing_notes_and_removing_empty_lines(self):
        list_with_notes_to_clear = ["1. Linia pierwsza", "b. Linia druga", "b. Linia trzecia", "c. Linia czwarta",
                                         "correct Linia piąta", "", "", "# Ten komentarz nie będzie wczytany", "To są oczekiwane notatki", ""]
        clear_notes = ParseQuestions(list_with_notes_to_clear)
        assert clear_notes.give_clear_notes(0, None) == ["To są oczekiwane notatki"]

    def test_divide_question_sentence(self):
        given = "2. Pytanie"
        question_number, question_content = ParseQuestions.divide_question_sentence(given)
        assert question_number == 2
        assert question_content == "Pytanie"
