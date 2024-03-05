import json


class MatchView:

    def __init__(self):
        pass

    @staticmethod
    def get_pair_round_1_data():

        with open("../paires_round_1.json", "r") as f:
            player_dict = f.read()
            player_data = json.loads(player_dict)

            return player_data

    @staticmethod
    def show_player_name():

        all_players_name = []
        maxi = len(MatchView.get_pair_round_1_data())
        # x = 0

        players = MatchView.get_pair_round_1_data()
        for x in range(maxi):
            for row in players[x]:
                player_name = row["Nom"]
                all_players_name.append(player_name)
                x += 1

        return all_players_name

    @staticmethod
    def result_round_1():
        """Résultats du round 1"""

        all_winner = []
        all_loser = []
        all_equality_1 = []
        all_equality_2 = []

        print("Voici la liste des match : ")
        a = 0
        b = 1
        for x in range(len(MatchView.show_player_name())//2):
            print(f"Match {x+1} - {MatchView.show_player_name()[a]} vs {MatchView.show_player_name()[b]}")
            a += 2
            b += 2
            winner = input("Vainqueur = ")
            all_winner.append(winner)
            loser = input("Perdant = ")
            all_loser.append(loser)
            equality_1 = input("Égalité (j1) : ")
            all_equality_1.append(equality_1)
            equality_2 = input("Égalité (j2) : ")
            all_equality_2.append(equality_2)

        return all_winner, all_loser, all_equality_1, all_equality_2

    @staticmethod
    def result_round_3():
        """Résultats du round 3"""
        pass

    @staticmethod
    def result_round_4():
        """Résultats du round 4"""
        pass

    @staticmethod
    def round_resume():
        """Voir la fiche des rounds"""

        print("1 - voir le résumé du round 1, "
              "2 - voir le résumé du round 2, "
              "3 - voir le résumé du round 3, "
              "4 - voir le résumé du round 4")
        user_input = input("Tapez 1, 2, 3 ou 4 : ")
        return user_input


test_view = MatchView()
# print(test_view.show_player_name())
# print(test_view.result_round_1())

""" 
@staticmethod
def result_round_1():
       
        all_user_input = []

        print("Qui sont les vainqueurs du premier round ?")
        print("Sélectionnez le nom du vainqueur ou écrivé -Nul- en cas d'égalité")

        for paire in MatchView.get_pair_round_1_data():
            print(paire)
            user_input = input("Résultat : ")

            all_user_input.append(user_input)

        return all_user_input
"""
