import json

from model.player_model import PlayerModel
from controller.player_controller import PlayerController
from view.player_view import PlayerView


def test():
    x = input("lsdjs : ")
    if x != str(1):
        return test()
    return x


def main():

    player_controller = PlayerController
    player_controller.asking_for_new_player()


print(main())
