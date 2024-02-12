import json


class TournamentController:

    def __init__(self):
        pass

    @staticmethod
    def player_data():

        with open("../player_data.json", "r") as f:
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

        # user_input = tournament_view.TournamentView.get_player_info()
        # for val in self.tournament_data()
        print(type(self.player_data()))

        # return tournament_view.TournamentView.get_player_info(["Nom"] == user_input)

    @staticmethod
    def tournament_data():

        with open("../tournament_data.json", "r") as f:
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

        pairs = []
        player_list = self.player_data()
        player_list_min = 0
        player_list_max = len(player_list) - 1
        possible_pairs = int(len(player_list) / 2)

        for x in range(possible_pairs):
            pairs.append((player_list[player_list_min], player_list[player_list_max]))
            possible_pairs -= 1
            player_list_min += 1
            player_list_max -= 1
        return pairs


controller = TournamentController()
# print(controller.player_data())
# print(controller.creating_pairs())
# print(controller.show_player_name())
