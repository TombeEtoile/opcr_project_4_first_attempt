import json
from typing import List

import view
import model
from data import all_data


class TournamentController:

    def __init__(self):
        pass

    @staticmethod
    def player_list():

        player_data = all_data.AllData.player_data()
        return player_data

    @staticmethod
    def tournament_list():

        tournament_data = all_data.AllData.tournament_data()
        for row in tournament_data:
            print(row["Nom"])

        return tournament_data

    @staticmethod
    def show_player_name(self):

        players = TournamentController.player_list()
        for row in players:
            print(row["Nom"])

        return players


controller = TournamentController()
print(controller.player_list())
