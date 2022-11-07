import os
from View import View


class FileChooser:
    @staticmethod
    def choose_file():
        while True:
            View.file_reviev()
            user_choice = View.give_user_answer("Wybierz 1, aby zmienić katalog\nWybierz 2, aby wskazać plik ")
            if user_choice == "1":
                choosed_dir = View.give_user_answer("Wskaż katalog, w którym znajduje się plik z pytaniami: ")
                os.chdir(choosed_dir)
            elif user_choice == "2":
                filename = View.give_user_answer("Wpisz nazwę pliku: ")
                FileChooser.explore_file(filename)
                return filename

    @staticmethod
    def explore_file(filename):
        file_exist = FileChooser.is_file_exist(filename)
        if not file_exist:
            raise FileNotFoundError("Brak pliku z pytaniami")
        file_not_empty = FileChooser.is_file_not_empty(filename)
        if not file_not_empty:
            raise Exception("Plik jest pusty")

    @staticmethod
    def is_file_exist(filename):
        return os.path.isfile(filename)

    @staticmethod
    def is_file_not_empty(filename):
        return os.stat(filename).st_size != 0
