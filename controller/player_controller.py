from typing import List

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
    def check_player():
        """Check player view with player model"""

        for p in range(9):
            player = PlayerView.get_player_data()
            return player


    @staticmethod
    def run():

        run_game = PlayerView.get_player_data()
        return run_game

        # A FAIRE --> model.player_repository.save(player) --> data.json

