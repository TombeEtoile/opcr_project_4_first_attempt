"""
from typing import List
import json

from model.player_model import PlayerModel
from view.player_view import PlayerView, AddAnotherPlayer


class PlayerController:
    # Récupère les informations données par les joueurs et les vérifies avec le player model

    def __init__(self, view):
        # models
        self.players: List[PlayerModel] = []

        # view
        self.view = view

    @staticmethod
    def run_save_and_add():

        # call the view and save the player info into json file

        all_players = []
        # user_input = PlayerView.get_player_data()
        user_input = AddAnotherPlayer.asking_to_add_player()
        all_players.append(user_input)

        with open("data/player_data.json", "w") as f:
            json.dump(all_players, f, indent=2)
            # json.dump(user_input, f, indent=2)

        return all_players


# A FAIRE --> model.player_repository.save(player) --> data.json
"""