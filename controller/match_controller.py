import json


class MatchController:

    def __init__(self):
        pass

    @staticmethod
    def get_player_data():

        with open("../player_data.json", "r") as f:
            player_dict = f.read()
            player_data = json.loads(player_dict)

            return player_data

    def tri_elo(self):
        """Tri par point elo"""

        data = self.get_player_data()

        return sorted(data, key=lambda x: x["Elo"])

    def elo_pair(self):

        pairs = []
        player_list = self.tri_elo()
        player_list_min = 0
        player_list_max = len(player_list) - 1
        possible_pairs = int(len(player_list) / 2)

        for x in range(possible_pairs):
            pairs.append((player_list[player_list_min], player_list[player_list_max]))
            possible_pairs -= 1
            player_list_min += 1
            player_list_max -= 1
        return pairs

    def tri_point(self):
        """Tri par point competition"""

        data = self.get_player_data()

        return sorted(data, key=lambda x: x['age'])

    def point_distribution(self):
        """Distribution des point en fonction du résultat"""

        victoire = 1
        defaite = 0
        egalite = 0.5

    def creat_pair(self):
        """Paire par point elo"""
        pass

    def result_round(self):
        """Attribution des points aux joueurs"""
        pass

    def random_result(self):
        pass


match_controller = MatchController()
# print(match_controller.get_player_data())
print(match_controller.tri_elo())
print(match_controller.elo_pair())
