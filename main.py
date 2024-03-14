from controller.player_controller import PlayerController
from controller.tournament_controller import TournamentController
from controller.match_controller import MatchController
from controller.resume_controller import ResumeController


def main():

    player_controller = PlayerController(view=True)
    player_controller.add_new_player()

    tournament_controller = TournamentController()
    tournament_controller.response_general_information()

    match_controller = MatchController()
    match_controller.response_round_1()

    resume_controller = ResumeController()
    resume_controller.general_responses()


print(main())
