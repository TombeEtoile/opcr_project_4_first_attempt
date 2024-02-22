import json

from view.tournament_view import TournamentView


class TournamentController:

    def __init__(self):
        pass

    @staticmethod
    def get_player_info():

        all_player = TournamentView.player_data()
        user_input = TournamentView.get_player_info(view)
        # d = all_player[0:len(all_player)]
        max_size = len(all_player)

        for min_size in range(max_size):
            test_3 = all_player[min_size]
            min_size += 1

        print(f"test_3 = {test_3}")

        for k, val in test_3.items():
            if user_input == val:
                user_player = {k: val}
                return user_player
            return "Ce joueur n'existe pas"

        # print(all_player.index("AA"))

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
print(controller.get_player_info())
# print(controller.creating_pairs())
# print(controller.show_player_name())
