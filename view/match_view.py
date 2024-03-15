import json


class MatchView:

    def __init__(self):
        pass

    @staticmethod
    def round_1_organisation():
        """1 - voir l'organisation du round 1
           2 - inscrire les résultats du round 1
           3 - voir le classement suite au round 1
           4 - passer à la création des autres rounds"""

        print("Tapez le chiffre associé à votre choix : ")
        print("1 - Voir l'organisation du round 1,\n "
              "2 - Inscrire les résultats du round 1,\n "
              "3 - Voir le classement des joueurs suite au round 1,\n",
              "4 - Passer à l'inscription des rounds suivants")

        user_input = input("Tapez 1, 2, 3 ou 4 : ")

        return user_input

    @staticmethod
    def other_rounds_organisation():

        print("Tapez le chiffre associé à votre choix : \n"
              "1 - Inscrire les résultats du round suivant\n"
              "2 - Voir le classement des joueurs suite au dernier round\n"
              "3 - Voir les nouvelles pairs pour le prochain round\n"
              "4 - Passer à l'analyse des résultats")

        user_input = input("Tapez 1, 2, 3 ou 4 : ")

        return user_input

    @staticmethod
    def get_pair_round_1_data():

        with open("paires_round_1.json", "r") as f:
            player_dict = f.read()
            player_data = json.loads(player_dict)

            return player_data

    @staticmethod
    def show_player_name():

        all_players_name = []
        maxi = len(MatchView.get_pair_round_1_data())

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
        for x in range(len(MatchView.show_player_name()) // 2):
            print(f"Match {x + 1} - "
                  f"{MatchView.show_player_name()[a]} "
                  f"vs "
                  f"{MatchView.show_player_name()[b]}")
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


test_view = MatchView()
# print(test_view.show_player_name())
# print(test_view.result_round_1())
