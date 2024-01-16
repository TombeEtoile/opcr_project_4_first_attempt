from typing import List
import json

from model.player_model import PlayerModel
from view.player_view import PlayerView


class PlayerController:
    """Récupère les informations données par les joueurs et les vérifies avec le player model"""

    def __init__(self, view):
        # models
        self.players: List[PlayerModel] = []

        # view
        self.view = view

    @staticmethod
    def run_and_save():
        """call the view and save the player info into json file"""

        run_game = PlayerView.get_player_data()

        with open("data/player_data.json", "w") as f:
            json.dump(run_game, f)

        return run_game

# A FAIRE --> model.player_repository.save(player) --> data.json
