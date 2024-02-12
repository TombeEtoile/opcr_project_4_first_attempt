from controller.tournament_controller import TournamentController


class TournamentView:

    @staticmethod
    def get_general_tournament_info():

        print("1 - voir les pairs de joueurs, "
              "2 - voir la fiche d'un joueur, "
              "3 - voir la fiche d'un tournoi.")
        user_input = input("Tapez 1, 2 ou 3 : ")
        return user_input

    @staticmethod
    def get_player_info():

        print("Voici le nom des joueurs :"
              f"{TournamentController().show_player_name()}")
        user_input = input("Copiez collez le nom du joueur dont vous voulez voir la fiche : ")

        return user_input

    @staticmethod
    def get_tournament_info():

        print("Voici le nom des tournois :"
              f"{TournamentController().show_tournament_name()}")
        user_input = input("Copiez collez le nom du tournois dont vous voulez voir la fiche : ")

        return user_input


test_view = TournamentView
# test_view.get_general_tournament_info()
# test_view.get_player_info()
# test_view.get_tournament_info()
