import json

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

    @staticmethod
    def get_player_data():

        with open("../player_data.json", "r") as f:
            player_dict = f.read()
            player_data = json.loads(player_dict)

            return player_data

    def player_result(self):
        """voir résultats d'un joueur"""

        all_players_name = []

        players = self.get_player_data()
        for row in players:
            player_name = row["Nom"]
            all_players_name.append(player_name)

        all_players_name = []

        for row in players:
            player_name = row["Nom"]
            all_players_name.append(player_name)

        print("Voici le nom des joueurs :"
              f"{all_players_name}")
        user_input = input("Copiez collez le nom du joueur dont vous voulez voir la fiche : ")

        for player in players:
            if user_input in player.values():
                return print(f"Voici la fiche du joueur {user_input} - {player}")
        return print("Ce joueur n'est pas dans notre liste")

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

        result = self.get_player_data()

        return sorted(result, key=lambda x: x["Point"])


resume_controller = ResumeController()
# resume_controller.player_result()
resume_controller.ranking_result()
