class ResumeView:

    def __init__(self):
        pass

    @staticmethod
    def general_information():
        """Menu choice"""

        print("Séléctionner les données que vous souhaitez analyser : ")
        input("1 - voir les résultats d'un joueur \n"
              "2 - voir résultats global du 1er round \n"
              "3 - voir résultats global du 2ème round \n"
              "4 - voir résultats global du 3ème round \n"
              "5 - voir résultats global du 4ème rounds \n"
              "6 - voir classement de tous les joueurs \n"
              "Tapez 1, 2, 3, 4, 5 ou 6 : ")


resume_view = ResumeView()
resume_view.general_information()
