from controller.player_controller import PlayerController
# from controller.tournament_controller import TournamentController
from controller import data


def test():
    x = input("lsdjs : ")
    if x != str(1):
        return test()
    return x


def test2():
    """
    all_list = []
    list_test = [1, 2, 3, 4, 5, 6, 7, 8]
    list_min = 0
    list_max = len(list_test) - 1
    possible_pairs = int(len(list_test) / 2)
    # print((list_test[list_min], list_test[list_max]))

    for x in range(possible_pairs):
        all_list.append((list_test[list_min], list_test[list_max]))
        possible_pairs -= 1
        list_min += 1
        list_max -= 1
    return all_list
    """


def main():

    player_controller = PlayerController(view=True)
    player_controller.add_new_player()
    # Ne pas lancer avant tous les test, tous les joueurs sont déjà instanciés

    # tournament_controller = TournamentController()
    # tournament_controller.creating_pairs()


print(main())


