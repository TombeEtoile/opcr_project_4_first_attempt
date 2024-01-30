import view
from controller import player_controller
from model import player_model


class TournamentView:

    @staticmethod
    def tournament_general_info():

        print("Entrez les informations du tournois")

    @staticmethod
    def tournament_name():

        user_input = input("Nom du tournoi :")
        return user_input

    @staticmethod
    def tournament_place():
        user_input = input("Emplacement du tournoi :")
        return user_input

    @staticmethod
    def tournament_start():
        user_input = input("Date du début du tournoi :")
        return user_input

    @staticmethod
    def tournament_end():
        user_input = input("Date dde fin du tournoi :")
        return user_input

    @staticmethod
    def tournament_round_number():
        user_input = input("Nombre de tour du tournoi :")
        return user_input

    @staticmethod
    def tournament_rond_list():
        pass

    @staticmethod
    def tournament_player_list():
        pass

    @staticmethod
    def tournament_jury_remark():
        pass


test_view = TournamentView
