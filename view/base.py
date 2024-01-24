import random
import string
from controller import player_controller


# from controller.player_controller import PlayerController


class PlayerViewTest:
    """Les joueurs entrent leur données"""

    @staticmethod
    def get_player_name():

        user_input = input("Entrez votre nom : ")
        try:
            user_input = int(user_input)
            print("ERREUR - Vous devez écrire uniquement des lettres.")
            return PlayerViewTest.get_player_name()
        except ValueError:
            return user_input

    @staticmethod
    def get_player_surname():

        user_input = input("Entrez votre prénom : ")
        try:
            user_input = int(user_input)
            print("ERREUR - Vous devez écrire uniquement des lettres.")
            return PlayerViewTest.get_player_name()
        except ValueError:
            return user_input

    @staticmethod
    def test():
        x = input("lsdjs : ")
        if x != str(1):
            return test()
        return x


       while True:
            print("Entrez votre date de naissance sous la forme jj/mm/aaaa :")
            try:
                user_input_day = int(user_input_day)
                user_input_month = int(user_input_month)
                user_input_year = int(user_input_year)
                break
            except ValueError:
                print("Votre date de naissance doit contenir uniquement des chiffres.")

        print(f"Votre date de naissance est - {user_input_day}/{user_input_month}/{user_input_year}")
        return f"{str(user_input_day)}/{str(user_input_month)}/{str(user_input_year)}"

    def get_player_day():
        user_input_day = input("jj : ")
        return user_input_day

    def get_player_month():
        user_input_month = input("mm : ")
        return user_input_month

    def get_player_year():

        user_input_year = input("aaaa : ")
        return user_input_year

    def get_player_birthday(day, month, year):

        p_day = PlayerViewTest.get_player_name()
        p_day = day
        get_player_month() = month
        get_player_year() = year


    @staticmethod
    def get_player_identifier():
        user_id = (f"{random.randint(1000, 9999)}"
                   f"{random.choice(string.ascii_letters)}"
                   f"{random.choice(string.ascii_letters)}"
                   f"{random.choice(string.ascii_letters)}"
                   f"{random.randint(1000, 9999)}")
        print("Voici votre ID : ", user_id)
        return user_id

    @staticmethod
    def get_player_data():
        name = PlayerViewTest.get_player_name()
        surname = PlayerViewTest.get_player_surname()
        birthday = PlayerViewTest.get_player_birthday()
        identifier = PlayerViewTest.get_player_identifier()
        player_test = {"Nom": name, "Prenom": surname, "Date de naissance": birthday, "ID": identifier}
        AddAnotherPlayer.asking_to_add_player()
        return player_test


class AddAnotherPlayer:
    """Ask if the programme should add another player"""

    @staticmethod
    def asking_to_add_player():

        asking = int(input(f"1 - pour ajouter un nouveau joueur \n"
                           f"2 - pour cloturer l'inscription de nouveau joueur \n"
                           f"Taper 1 ou 2 - "))
        # while asking == ValueError:
        # print("Vous devez écrire 1 ou 2")
        # break
        if asking == 1:
            # print(PlayerView.get_player_data())
            print(player_controller.PlayerController.run_save_and_add())
        elif asking == 2:
            print("Les joueurs ont bien été enregistrés")
        else:
            while asking != 1 or 2 or asking == ValueError:
                print("Vous devez écrire 1 ou 2")
                print(AddAnotherPlayer.asking_to_add_player())
                break

save = PlayerViewTest
print(save.get_player_data())
# add = AddAnotherPlayer
# print(add.asking_to_add_player())
