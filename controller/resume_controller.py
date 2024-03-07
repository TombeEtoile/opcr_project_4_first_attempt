from view.resume_view import ResumeView


class ResumeController:
    """accès à la data"""

    def __init__(self):
        pass

    def general_responses(self):

        user_input = ResumeView.general_information()

        try:
            if user_input == "1":
                self.player_result()

            elif user_input == "2":
                self.first_round_result()

            elif user_input == "3":
                self.second_round_result()

            elif user_input == "4":
                self.third_round_result()

            elif user_input == "5":
                self.fourth_round_result()

            elif user_input == "6":
                self.ranking_result()

            elif user_input != "1" or "2" or "3" or "4" or "5" or "6":
                print("ERREUR : Votre réponse n'est pas valable.")
                self.general_responses()

        except TypeError or ValueError:
            print(f"Votre réponse n'est pas valable, tapez 1, 2, 3, 4, 5 ou 6 {self.general_responses()}")

    def player_result(self):
        """voir résultats d'un joueur"""


        pass

    def first_round_result(self):
        """voir résultats global du 1er round"""
        pass

    def second_round_result(self):
        """voir résultats global du 2ème round"""
        pass

    def third_round_result(self):
        """voir résultats global du 3ème round"""
        pass

    def fourth_round_result(self):
        """voir résultats global du 4ème rounds"""
        pass

    def ranking_result(self):
        """voir classement de tous les joueurs"""
        pass