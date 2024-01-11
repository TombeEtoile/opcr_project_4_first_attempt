from typing import List

from model.player_model import PlayerModel


class PlayerController:
    """Récupère les informations données par les joueurs et les vérifies avec le player model"""

    def __init__(self, view):
        # models
        self.players: List[PlayerModel] = []

        # view
        self.view = view

    def get_players(self, p_name, p_surname, p_birthday, p_identifier):
        """Check player view with player model"""

        while len(self.players) < 9:
            p_name = self.view.PlayerView.ask_player_identity(name=p_name)
            p_surname = self.view.PlayerView.ask_player_identity(surname=p_surname)
            p_birthday = self.view.PlayerView.ask_player_identity(birthday=p_birthday)
            p_identifier = self.view.PlayerView.ask_player_identity(identifier=p_identifier)
            if not p_name or p_surname or p_birthday or p_identifier:
                return
            return p_name, p_surname, p_birthday, p_identifier

        player = PlayerModel(p_name, p_surname, p_birthday, p_identifier)
        self.players.append(player)

        # A FAIRE --> model.player_repository.save(player) --> data.json
