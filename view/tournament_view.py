from controller import tournament_controller


class TournamentView:

    @staticmethod
    def get_general_tournament_info():

        user_input = input("1 - voir les pairs de joueurs"
                           "2 - voir la fiche d'un joueur"
                           "3 - voir la fiche d'un tournoi"
                           "Tapez 1, 2 ou 3 : ")
        return user_input

    @staticmethod
    def get_player_info():

        user_input = input("Voici le nom des joueurs : "
                           f"{tournament_controller.TournamentController().show_player_name()}"
                           "De quel joueur voulez-vous voir la fiche ? Copiez collez le nom du joueur : ")

        return user_input

    @staticmethod
    def get_tournament_info():

        user_input = input("Voici le nom des tournois : "
                           f"{tournament_controller.TournamentController().show_tournament_name()}"
                           "De quel joueur voulez-vous voir la fiche ? Copiez collez le nom du tournois : ")

        return user_input


test_view = TournamentView
# test_view.get_player_info()
