"""import random
import string

from controller import player_controller


class PlayerView:
    """Les joueurs entrent leur données"""

    @staticmethod
    def get_player_name():
        """Player name"""

        user_input = input("Entrez votre nom : ")
        try:
            user_input = int(user_input)
            print("ERREUR - Vous devez écrire uniquement des lettres.")
            return PlayerView.get_player_name()
        except ValueError:
            return user_input

    @staticmethod
    def get_player_surname():
        """Player surname"""

        user_input = input("Entrez votre prénom : ")
        try:
            user_input = int(user_input)
            print("ERREUR - Vous devez écrire uniquement des lettres.")
            return PlayerView.get_player_name()
        except ValueError:
            return user_input

    @staticmethod
    def get_player_birthday():
        """Player birthday"""

        while True:
            print("Entrez votre date de naissance sous la forme jj/mm/aaaa :")
            user_input_day = input("jj : ")
            user_input_month = input("mm : ")
            user_input_year = input("aaaa : ")
            try:
                user_input_day = int(user_input_day)
                user_input_month = int(user_input_month)
                user_input_year = int(user_input_year)
                break
            except ValueError:
                print("Votre date de naissance doit contenir uniquement des chiffres.")

        print(f"Votre date de naissance est - {user_input_day}/{user_input_month}/{user_input_year}")
        return f"{str(user_input_day)}/{str(user_input_month)}/{str(user_input_year)}"

    @staticmethod
    def get_player_identifier():
        """player ID"""

        user_id = (f"{random.randint(1000, 9999)}"
                   f"{random.choice(string.ascii_letters)}"
                   f"{random.choice(string.ascii_letters)}"
                   f"{random.choice(string.ascii_letters)}"
                   f"{random.randint(1000, 9999)}")
        print("Voici votre ID : ", user_id)
        return user_id

    @staticmethod
    def get_player_data():
        """Creat player profil"""

        name = PlayerView.get_player_name()
        surname = PlayerView.get_player_surname()
        birthday = PlayerView.get_player_birthday()
        identifier = PlayerView.get_player_identifier()
        player_profil = {"Nom": name, "Prenom": surname, "Date de naissance": birthday, "ID": identifier}
        return player_profil


class AskingPlayer:

    @staticmethod
    def asking_for_new_player():
        """Ask for adding a player"""

        user_input = int(input(f"1 - pour ajouter un nouveau joueur \n"
                               f"2 - pour cloturer l'inscription de nouveau joueur \n"
                               f"Taper 1 ou 2 - "))
        return user_input


# save = PlayerView
# print(save.get_player_data())
# add = AskingPlayer
# print(add.asking_for_new_player())
"""