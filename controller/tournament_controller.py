import json

from view import tournament_view


class TournamentController:

    def __init__(self):
        pass

    @staticmethod
    def player_data():

        with open("data/player_data.json", "r") as f:
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

    @staticmethod
    def get_player_info():

        user_input = tournament_view.TournamentView.get_player_info()
        tournament_view.TournamentView.get_player_info(["Nom"] == user_input)

        return tournament_view.TournamentView.get_player_info(["Nom"] == user_input)

    @staticmethod
    def tournament_data():

        with open("data/tournament_data.json", "r") as f:
            tournament_dict = f.read()
            tournament_data = json.loads(tournament_dict)

            return tournament_data

    def show_tournament_name(self):

        all_tournament_name = []

        tournaments = self.tournament_data()
        for row in tournaments:
            tournament_name = row["Nom"]
            all_tournament_name.append(tournament_name)

        return all_tournament_name

    def creating_pairs(self):

        first_pair_of_players = [self.show_player_name()[0, 1]]
        second_pair_of_players = [self.show_player_name()[2, 3]]
        third_pair_of_players = [self.show_player_name()[4, 5]]
        fourth_pair_of_players = [self.show_player_name()[6, 7]]

        return first_pair_of_players, second_pair_of_players, third_pair_of_players, fourth_pair_of_players


controller = TournamentController()
print(controller.show_player_name())
