class ResumeView:

    def __init__(self):
        pass

    @staticmethod
    def general_information():
        """Menu choice"""

        print("Sélectionnez les données que vous souhaitez analyser : ")
        return input("1 - voir les résultats d'un joueur \n"
                     "2 - voir les résultats globaux du tournois \n"
                     "3 - terminer le tournois \n"
                     "Tapez 1, 2 ou 3 : ")


resume_view = ResumeView()
# resume_view.general_information()
