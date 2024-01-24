from typing import List
import json

from model.player_model import PlayerModel
from view import player_view


class PlayerController:
    """Récupère les informations données par les joueurs et les vérifies avec le player model"""

    def __init__(self, view):
        # models
        self.players: List[PlayerModel] = []

        # view
        self.view = view

    @staticmethod
    def asking_for_new_player():
        """Ask for adding a player"""

        user_input = int(input(f"1 - pour ajouter un nouveau joueur \n2 - pour cloturer l'inscription de nouveau joueur \nTaper 1 ou 2 - "))
        if user_input == 1:
            player_view.PlayerView.get_player_data()
        if user_input == 2:
            print("Les joueurs ont bien été enregistrés")
            PlayerController.run_save_and_add()

    @staticmethod
    def add_player():
        all_players = [player_view.PlayerView.get_player_data()]
        return all_players

    @staticmethod
    def run_save_and_add():
        """add player in Json"""

        with open("data/player_data.json", "w") as f:
            json.dump(PlayerController.add_player(), f, indent=2)
