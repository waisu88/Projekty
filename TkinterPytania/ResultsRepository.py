import json


class ResultsRepository:
    def __init__(self, user_results):
        self._user_results = user_results
        self._user_total_points = self._user_results[0]
        self._user_questions_statistics = self._user_results[1]
        self._database_type = "json"

    def give_updated_user_results(self, question_statistics, question_number):
        updated_single_question_statistics = question_statistics.give_question_statistics()
        self._user_questions_statistics[question_number] = updated_single_question_statistics
        self._user_results[0] = self._user_total_points
        self._user_results[1] = self._user_questions_statistics
        updated_user_results = self._user_results
        return updated_user_results

    @staticmethod
    def get_user_results_from_db(name):
        filename = ResultsRepository.get_filename(name)
        try:
            user_results = ResultsRepository.load_results_from_json(filename)
            return user_results
        except FileNotFoundError:
            print(f"Witaj {name}!")
            user_results = [0, {}]
            return user_results



    @staticmethod
    def load_results_from_json(filename):
        with open(filename, "r") as file:
            user_results = json.load(file)
            return user_results

    # os.path.splitext(filename)
    @staticmethod
    def save_results_to_json(name, updated_user_results):
        filename = ResultsRepository.get_filename(name)
        with open(filename, "w+") as file:
            json.dump(updated_user_results, file, indent=1)

    @staticmethod
    def get_filename(name):
        filename = name + ".json"
        return filename

    def give_single_question_statistics(self, question_number):
        if question_number in self._user_questions_statistics.keys():
            return self._user_questions_statistics[question_number]
        else:
            single_question_statistics = [0, 0, 0, None, None]
            return single_question_statistics

    def add_point(self):
        self._user_total_points += 1

    def subtract_point(self):
        self._user_total_points -= 1

        #
        #
        #
        # try:
        #     if result_file:
        #         file = open(result_file, "r")
        #         results = json.load(file)
        #         return results
        #     else:
        #         results = {}
        #         return results
        # except JSONDecodeError:
        #     results = {}
        #     return results
        # except FileNotFoundError:
        #     results = {}
        #     return results
        #

