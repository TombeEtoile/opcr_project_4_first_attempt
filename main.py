from controller.player_controller import PlayerController
from controller.tournament_controller import TournamentController, TournamentView


def test():
    x = input("lsdjs : ")
    if x != str(1):
        return test()
    return x


def main():

    player_controller = PlayerController(view=True)
    player_controller.add_new_player()

    tournament_controller = TournamentController()
    tournament_controller.response_general_information()

    # Ne pas lancer avant tous les test, tous les joueurs sont déjà instanciés


print(main())
