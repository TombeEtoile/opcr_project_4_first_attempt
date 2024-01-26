from typing import List
import json

from model.player_model import PlayerModel
from view.player_view import PlayerView, AskingPlayer


class PlayerController:
    """Récupère les informations données par les joueurs et les vérifies avec le player model"""

    def __init__(self, view):
        # models
        self.players: List[PlayerModel] = []

        # view
        self.view = view

    def add_new_player(self):

        response = AskingPlayer.asking_for_new_player()
        if response == 1:
            self.players.append(PlayerView.get_player_data())
            print(self.players)
            return self.players
        elif response == 2:
            print("Vous n'avez rentré aucun joueur")

    def call_for_asking_new_player(self):

        x = 1

        if len(self.add_new_player()) == x:
            AskingPlayer.asking_for_new_player()
            x += 1

        if len(self.add_new_player()) == x - 1:
            self.run_save_and_add()

    def run_save_and_add(self):
        """add player in Json"""

        with open("data/player_data.json", "w") as f:
            json.dump(self.players, f, indent=2)


# test = PlayerController(view=2)
# test.add_new_player()
