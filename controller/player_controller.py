from typing import List
import json

from model.player_model import PlayerModel
from view.player_view import PlayerView, AskingPlayer
# from tournament_controller import TournamentController


class PlayerController:
    """Retrieves information from players and checks it with the player model"""

    def __init__(self, view):

        # models
        self.players: List[PlayerModel] = []

        # view
        self.view = view

    def add_new_player(self):

        response = AskingPlayer.asking_for_new_player()

        try:
            if response == 1:
                """Si 1 ==> calls the view to create a player and calls call_for_asking_new_player()"""
                self.players.append(PlayerView.get_player_data())
                print(self.players)
                self.call_for_asking_new_player()
                return self.players

            elif response == 2:
                """Si 2 ==> registers players"""
                print("Les joueurs ont été enregistrés")
                self.run_save_and_add()
                # TournamentController.response_general_information(self=TournamentController)

        except ValueError:
            print("Veuillez écrire 1 ou 2")
            return self.add_new_player()

    def call_for_asking_new_player(self):
        """calls up the previous function to add another player"""

        self.add_new_player()

    def run_save_and_add(self):
        """add player in Json"""

        with open("player_data.json", "w") as f:
            json.dump(self.players, f, indent=2)
