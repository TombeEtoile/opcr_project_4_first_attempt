import json

import view
import model
import data

from typing import List


class TournamentController:

    def __init__(self, tournament, view):

        # model
        self.model = tournament

        # view
        self.view = view

    def set_tournament(self):


