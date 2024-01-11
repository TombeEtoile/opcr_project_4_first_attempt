"""
from model import player_model

players:{0:
        {id: "AB12345", nom:"michel", score:0, prenom: "pasta"},
    1:
        {id: "AB12345", nom:"pierre", score:0, prenom: "rocher"}}



# Appeler la class PlayerSetUp
player_set_up = player_model.PlayerSetUp()

players = {"identity": player_set_up.player_identity(),
           "birthday": player_set_up.player_birthday(),
           "id": player_set_up.player_id()}


class AllPlayers:
    # Appeler 9 fois la fonction PlayerSetUp

    i = 9

    def __init__(self):
        pass

    def creat_one_player(self):
        pass
"""
