import mysql.connector


class MySqlConnector:
    select_users_query = "SELECT username FROM users"

    def __init__(self, controller):
        self.controller = controller
        self.connection = mysql.connector.connect(user="root", password="sqlpython", host="127.0.0.1",
                                                  database="python", auth_plugin="mysql_native_password")
        self.players_in_db = self.give_players()

    def give_players(self):
        cursor = self.connection.cursor()
        cursor.execute(MySqlConnector.select_users_query)
        players = []
        for row in cursor:
            players.append(row[0])
        return players

    def give_user_id(self, name):
        give_user_id_query = f"SELECT user_id, user_points FROM users WHERE username='{name}'"
        cursor = self.connection.cursor()
        cursor.execute(give_user_id_query)
        user_id_user_points = cursor.fetchone()
        return user_id_user_points

    def add_player(self, name):
        if f"{name}" not in self.controller._all_players:
            add_user_query = f"INSERT IGNORE INTO users(user_id, username, user_points) SELECT MAX(user_id)+1, '{name}', 0 FROM users"
            cursor = self.connection.cursor()
            cursor.execute(add_user_query)
            self.connection.commit()

    def give_question_statistics(self, user_id, num_of_q):
        select_ques_stat_query = f"SELECT number_of_question from results WHERE user_id={user_id}"
        cursor1 = self.connection.cursor()
        cursor1.execute(select_ques_stat_query)
        answered_questions = []
        for row in cursor1:
            answered_questions.append(row[0])
        if num_of_q in answered_questions:
            give_scores_query = f"SELECT number_of_tries, number_of_wins, number_of_fails, date_of_last_win, " \
                                f"date_of_last_fail FROM results WHERE number_of_question={num_of_q} AND user_id={user_id}"
            cursor2 = self.connection.cursor()
            cursor2.execute(give_scores_query)
            return cursor2.fetchall()

    def save_question_statistics(self, user_id, num_of_q):
        save_ques_stat_query = f"INSERT INTO results(user_id, number_of_question, number_of_tries, number_of_wins, number_of_fails, date_of_last_win, " \
                               f"date_of_last_fail) VALUES ({user_id}, {num_of_q}, {self.controller._question_statistics._number_of_tries}, " \
                               f"{self.controller._question_statistics._number_of_wins}, " \
                               f"{self.controller._question_statistics._number_of_fails}, " \
                               f"'{self.controller._question_statistics._date_of_last_win}', " \
                               f"'{self.controller._question_statistics._date_of_last_fail}')" \
                               f"ON DUPLICATE KEY UPDATE " \
                               f"user_id={user_id}, " \
                               f"number_of_question={num_of_q}, " \
                               f"number_of_tries={self.controller._question_statistics._number_of_tries}, " \
                               f"number_of_wins={self.controller._question_statistics._number_of_wins}, " \
                               f"number_of_fails={self.controller._question_statistics._number_of_fails}, " \
                               f"date_of_last_win='{self.controller._question_statistics._date_of_last_win}', " \
                               f"date_of_last_fail='{self.controller._question_statistics._date_of_last_fail}'"
        cursor = self.connection.cursor()
        cursor.execute(save_ques_stat_query)
        self.connection.commit()

    def save_user_points(self, user_points, name):
        save_user_points_query = f"UPDATE users SET user_points={user_points} WHERE username='{name}'"
        cursor = self.connection.cursor()
        cursor.execute(save_user_points_query)
        self.connection.commit()

    def delete_player_from_db(self, name):
        delete_player_results_query = f"DELETE FROM results WHERE user_id=(SELECT user_id FROM users WHERE username='{name}')"
        cursor1 = self.connection.cursor()
        cursor1.execute(delete_player_results_query)
        self.connection.commit()
        delete_player_query = f"DELETE FROM users WHERE username='{name}'"
        cursor2 = self.connection.cursor()
        cursor2.execute(delete_player_query)
        self.connection.commit()
