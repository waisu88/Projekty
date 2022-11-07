import tkinter.messagebox as msb
import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    large_font = ("Verdana", 20)
    medium_font = ("Verdana", 15)

    def __init__(self, controller):
        super().__init__()
        self.title("Pytania v1.0")
        self.geometry("800x450")
        self.controller = controller
        self.frames = self.create_frames()
        self.main_menu_frame = self.frames[MainMenu]
        self.game_menu_frame = self.frames[GameMenu]
        self.delete_user_frame = self.frames[DeletePlayerMenu]

    def create_frames(self):
        frames = {}
        container = tk.Frame(self, width=500, height=500)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        for F in (MainMenu, GameMenu, DeletePlayerMenu):
            frame = F(container, self)
            frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        return frames

    def main(self):
        self.show_frame(MainMenu)
        self.mainloop()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainMenu(tk.Frame):
    def __init__(self, parent, view):
        super().__init__(parent)
        self.view = view
        self.main_menu_label = ttk.Label(self, text="Pytania z wiedzy ogólnej", font=("Verdana", 20))
        self.main_menu_label.grid(row=0, column=0, padx=10, pady=10)
        self.welcome_label = ttk.Label(self, text="Witaj w programie do odpytywania:\nPrzedstaw się, aby zagrać", anchor="w")
        self.welcome_label.grid(row=2, column=0)
        self.name_entry = ttk.Entry(self, textvariable=str, width=40)
        self.name_entry.grid(row=3, column=0)
        self.button_enter_game = tk.Button(self, text="Graj!", command=self.enter_game_new_player)
        self.button_enter_game.grid(row=3, column=1)
        self.choose_name_label = ttk.Label(self, text="lub wybierz imię z listy graczy")
        self.choose_name_label.grid(row=4, column=0)
        self.combobox_players_already_played = ttk.Combobox(self, textvariable=tk.StringVar())
        self.combobox_players_already_played.grid(row=5, column=0)
        self.combobox_players_already_played['values'] = view.controller._all_players
        self.combobox_players_already_played.current()
        self.combobox_players_already_played.bind("<<ComboboxSelected>>", self.enter_game_player_already_played)
        self.button_delete_player = tk.Button(self, text="Usuń gracza", command=self.enter_delete_player_menu)
        self.button_delete_player.grid(row=0, column=1)

    def enter_game_player_already_played(self, event):
        name = self.combobox_players_already_played.get()
        self.view.controller.enter_game(name)

    def enter_game_new_player(self):
        name = str(self.name_entry.get())
        if name != "":
            self.view.controller.add_player(name)
        else:
            msb.showinfo("", "Podaj imię")

    def enter_delete_player_menu(self):
        self.view.show_frame(DeletePlayerMenu)


class GameMenu(tk.Frame):
    def __init__(self, parent, view):
        super().__init__(parent)
        self.view = view
        self.question_content = tk.StringVar()
        self.answer_a = tk.StringVar()
        self.answer_b = tk.StringVar()
        self.answer_c = tk.StringVar()
        self.game_menu_label = ttk.Label(self, text="Odpowiadaj na pytania", font=("TimesNewRoman", 15))
        self.game_menu_label.grid(row=0, column=0, padx=10, pady=10)
        self.button_back_to_main_menu = ttk.Button(self, text="Wróć do menu głównego",
                                                   command=self.view.controller.back_to_main_menu)
        self.button_back_to_main_menu.grid(row=0, column=5, padx=10, pady=10)
        self.open_file_button = ttk.Button(self, text="Wybierz plik z pytaniami",
                                           command=self.view.controller.choose_file_with_questions)
        self.open_file_button.grid(row=1, column=0, padx=10, pady=10)
        self.question_label = ttk.Label(self, text="", textvariable=self.question_content, font=View.large_font,
                                        width=35, wraplength=600)
        self.question_label.grid(row=5, column=0, padx=5, pady=10, sticky='w')
        self.answer_a_label = ttk.Label(self, text="", textvariable=self.answer_a, font=View.medium_font, width=45,
                                        wraplength=600)
        self.answer_a_label.grid(row=6, column=0, padx=5, pady=10, sticky='w')
        self.answer_b_label = ttk.Label(self, text="", textvariable=self.answer_b, font=View.medium_font, width=45,
                                        wraplength=600)
        self.answer_b_label.grid(row=7, column=0, padx=5, pady=10, sticky='w')
        self.answer_c_label = ttk.Label(self, text="", textvariable=self.answer_c, font=View.medium_font, width=45,
                                        wraplength=600)
        self.answer_c_label.grid(row=8, column=0, padx=5, pady=10, sticky='w')
        self.a_checkbox = False
        self.b_checkbox = False
        self.c_checkbox = False
        self.confirm_answer_button = None

    def show_answer_sheet(self):
        self.a_checkbox = ttk.Checkbutton(self, text="A")
        self.a_checkbox.grid(row=6, column=4)
        self.b_checkbox = ttk.Checkbutton(self, text="B")
        self.b_checkbox.grid(row=7, column=4)
        self.c_checkbox = ttk.Checkbutton(self, text="C")
        self.c_checkbox.grid(row=8, column=4)
        self.confirm_answer_button = ttk.Button(self, text="Sprawdź", command=self.view.controller.confirm_answer)
        self.confirm_answer_button.grid(row=8, column=5)

    def show_question(self, q_and_a):
        self.question_content.set(f"{q_and_a[0]}. {q_and_a[1]}")
        self.answer_a.set(f"a) {q_and_a[2]}")
        self.answer_b.set(f"b) {q_and_a[3]}")
        self.answer_c.set(f"c) {q_and_a[4]}")
        self.open_file_button.destroy()

    def give_marked_answers(self):
        user_marked_a = self.a_checkbox.instate(['selected'])
        user_marked_b = self.b_checkbox.instate(['selected'])
        user_marked_c = self.c_checkbox.instate(['selected'])
        marked_answers = [user_marked_a, user_marked_b, user_marked_c]
        return marked_answers

    def show_question_statistics(self, question_statistics, user_pointed_good_answer):
        showinfo_title = "Świetnie" if user_pointed_good_answer else "Niestety odpowiedź jest nieprawidłowa"
        showinfo_content = f"To jest {question_statistics._number_of_tries} odpowiedź na to pytanie, z czego " \
                           f"\n{question_statistics._number_of_wins} razy odpowiedziałeś dobrze i \n{question_statistics._number_of_fails} " \
                           f"razy odpowiedziałeś źle. \nOstatnia dobra odpowiedź na pytanie była {question_statistics._date_of_last_win if question_statistics._date_of_last_win else '---'}, " \
                           f"a zła {question_statistics._date_of_last_fail if question_statistics._date_of_last_fail else '---'}. \nNastępnie pytanie?"
        player_want_continue = msb.askokcancel(showinfo_title, showinfo_content)
        self.view.controller.is_player_want_continue(player_want_continue)


class DeletePlayerMenu(tk.Frame):
    def __init__(self, parent, view):
        super().__init__(parent)
        self.view = view
        self.delete_menu_label = ttk.Label(self, text="Wybierz gracza do usunięcia", font=("Verdana", 20))
        self.delete_menu_label.grid(row=0, column=0, padx=10, pady=10)
        self.combobox_players_already_played = ttk.Combobox(self, textvariable=tk.StringVar())
        self.combobox_players_already_played.grid(row=1, column=0)
        self.combobox_players_already_played['values'] = view.controller._all_players
        self.combobox_players_already_played.current()
        self.combobox_players_already_played.bind("<<ComboboxSelected>>", self.confirm_delete_player)
        self.button_back_to_main_menu = ttk.Button(self, text="Wróć do menu głównego",
                                                   command=self.view.controller.back_to_main_menu)
        self.button_back_to_main_menu.grid(row=0, column=5, padx=10, pady=10)

    def confirm_delete_player(self, event):
        name = self.combobox_players_already_played.get()
        if msb.askokcancel("Usunięcie gracza", f"Czy napewno chcesz usunąć gracza: {name}"):
            self.view.controller.delete_player(name)
            self.view.show_frame(MainMenu)


