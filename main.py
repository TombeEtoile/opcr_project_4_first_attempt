
from model.player_model import PlayerModel
from controller.player_controller import PlayerController
from view.player_view import PlayerView
from view.base import PassivView


def main():
    p_model = PlayerModel(p_name, p_surname, p_birthday, p_identifier)
    p_view = PlayerView()
    passiv_view = PassivView(player_view, view)
    p_controller = PlayerController(p_view)
    p_controller.run()


main()
