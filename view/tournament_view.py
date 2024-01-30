import view
from controller import player_controller
from model import player_model
import data


class TournamentView:

    @staticmethod
    def get_tournament_info():

        user_input = input("1 - voir tous les matchs de tous les tournois"
                           "2 - voir les résultats d'un joueur"
                           "3 - voir les résultats d'un tournoi"
                           "Tapez 1, 2 ou 3 : ")
        return user_input

    @staticmethod
    def get_player_performance():

        user_input = input(f"Quel joueur voulez-vous voir ? ")
        return user_input

    @staticmethod
    def get_tournament_list():

        user_input = input("Quel tournoi voulez-vous voir ? ")
        return user_input


test_view = TournamentView
test_view.get_player_performance()
