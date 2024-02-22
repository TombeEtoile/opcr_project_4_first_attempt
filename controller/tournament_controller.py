import json

from view.tournament_view import TournamentView


class TournamentController:

    def __init__(self):
        pass

    @staticmethod
    def find_player_card():

        players = TournamentView.player_data()
        user_input = TournamentView.get_player_info(view)

        for player in players:
            if user_input in player.values():
                return print(f"Voici la fiche du joueur {user_input} - {player}")
        return print("Ce joueur n'est pas dans notre liste")

    @staticmethod
    def find_tournament_card():

        tournament = TournamentView.tournament_data()
        user_input = TournamentView.get_tournament_info(view)

        for player in tournament:
            if user_input in player.values():
                return print(f"Voici la fiche du tournoi {user_input} - {player}")
        return print("Ce trounoi n'est pas dans notre liste")

    @staticmethod
    def creating_pairs():

        pairs = []
        player_list = TournamentView.player_data()
        player_list_min = 0
        player_list_max = len(player_list) - 1
        possible_pairs = int(len(player_list) / 2)

        for x in range(possible_pairs):
            pairs.append((player_list[player_list_min], player_list[player_list_max]))
            possible_pairs -= 1
            player_list_min += 1
            player_list_max -= 1
        return pairs


view = TournamentView()
controller = TournamentController()
print(controller.find_player_card())
print(controller.find_tournament_card())
# print(controller.creating_pairs())
# print(controller.show_player_name())
