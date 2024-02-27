class MatchView:

    def __init__(self):
        pass

    @staticmethod
    def round_resume():
        """Voir la fiche des rounds"""

        print("1 - voir le résumé du round 1, "
              "2 - voir le résumé du round 2, "
              "3 - voir le résumé du round 3, "
              "4 - voir le résumé du round 4")
        user_input = input("Tapez 1, 2, 3 ou 4 : ")
        return user_input
        pass
