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

    # player_view = PlayerView
    # player_model = PlayerModel
    # player_controller = PlayerController.run_and_save_and_add()
    player_controller = PlayerController
    player_controller.run_save_and_add()

    # with open("data/player_data.json", "w") as f:
        # json.dump(player_controller, f, indent=2)


print(main())


