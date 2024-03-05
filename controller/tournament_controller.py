from view.tournament_view import TournamentView
# from player_controller import PlayerController


class TournamentController:

    def __init__(self):
        pass

    def response_general_information(self):
        """
        Si 1 ==> appelle creating_pairs() pour créer des paires de tournois
        Si 2 ==> appelle find_player_card() pour afficher la fiche d'un joueur
        Si 3 ==> appelle find_tournament_card() pour afficher la fiche d'un tournois
        """

        # TournamentView.get_general_tournament_info()
        answer = TournamentView.get_general_tournament_info()

        try:
            """
            if answer == "1":
                self.creating_pairs()
                print(self.creating_pairs())
                self.response_general_information()
                return self.creating_pairs()
            """
            if answer == "2":
                self.find_player_card()
                self.response_general_information()

            elif answer == "3":
                self.find_tournament_card()
                self.response_general_information()

            elif answer != "1" or "2" or "3":
                print("ERREUR : Votre réponse n'est pas valable.")
                TournamentView.get_general_tournament_info()

        except TypeError or ValueError:
            print(f"Votre réponse n'est pas valable, tapez 1, 2 ou 3 {TournamentView.get_general_tournament_info()}")

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

        for localisation in tournament:
            if user_input in localisation.values():
                return print(f"Voici la fiche du tournoi {user_input} - {localisation}")
        return print("Ce tournois n'est pas dans notre liste")


"""    
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
"""


view = TournamentView()
# controller = TournamentController()
# controller.response_general_information()
# print(controller.find_player_card())
# print(controller.find_tournament_card())
# print(controller.creating_pairs())
# print(controller.show_player_name())
