import json


class TournamentView:

    @staticmethod
    def get_general_tournament_info():

        print("1 - voir la fiche d'un joueur, "
              "2 - voir la fiche d'un tournoi, "
              "3 - passer aux résultats du tournoi")
        user_input = input("Tapez 1, 2 ou 3 : ")
        return user_input

    @staticmethod
    def player_data():

        with open("player_data.json", "r") as f:
            player_dict = f.read()
            player_data = json.loads(player_dict)

            return player_data

    def show_player_name(self):

        all_players_name = []

        players = self.player_data()
        for row in players:
            player_name = row["Nom"]
            all_players_name.append(player_name)

        return all_players_name

    def get_player_info(self):

        print("Voici le nom des joueurs :"
              f"{self.show_player_name()}")
        user_input = input("Copiez collez le nom du joueur dont vous voulez voir la fiche : ")

        return user_input

    @staticmethod
    def tournament_data():

        with open("tournament_data.json", "r") as f:
            tournament_dict = f.read()
            tournament_data = json.loads(tournament_dict)

            return tournament_data

    def show_tournament_name(self):

        all_tournament_name = []

        tournaments = self.tournament_data()
        print(tournaments)
        for row in tournaments:
            tournament_name = row["Nom"]
            all_tournament_name.append(tournament_name)

        return all_tournament_name

    def get_tournament_info(self):

        print("Voici le nom des tournois :"
              f"{self.show_tournament_name()}")
        user_input = input("Copiez collez le nom du tournois dont vous voulez voir la fiche : ")

        return user_input


test_view = TournamentView()
# test_view.get_general_tournament_info()
# print(test_view.player_data())
# print(test_view.tournament_data())
# test_view.get_player_info()
# test_view.get_tournament_info()
# test_view.show_player_name()
# test_view.show_tournament_name()
