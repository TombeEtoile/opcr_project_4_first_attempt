import json


class AllData:

    @staticmethod
    def tournament_data():

        with open("../../tournament_data.json", "r") as f:
            tournament_dict = f.read()
            tournament_data = json.loads(tournament_dict)

            return tournament_data

    @staticmethod
    def player_data():

        with open("../../player_data.json", "r") as f:
            player_dict = f.read()
            player_data = json.loads(player_dict)

            return player_data


all_data = AllData
# print(all_data.player_data())
# print(all_data.tournament_data())
