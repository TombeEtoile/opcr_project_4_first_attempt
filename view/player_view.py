import random
import string


class PlayerView:
    """Les joueurs entrent leur données"""

    @staticmethod
    def get_player_data():
        name = PlayerView.get_player_name()
        surname = PlayerView.get_player_surname()
        birthday = PlayerView.get_player_birthday()
        identifier = PlayerView.get_player_identifier()
        player_test = {"Nom": name, "Prenom": surname, "Date de naissance": birthday, "ID": identifier}
        return player_test

    @staticmethod
    def get_player_name():
        while True:
            user_input = input("Entrez votre nom : ")
            try:
                user_input = int(user_input)
                print("Votre nom doit contenir uniquement des lettres.")
            except ValueError:
                break
        return user_input

    @staticmethod
    def get_player_surname():
        while True:
            user_input = input("Entrez votre prénom : ")
            try:
                user_input = int(user_input)
                print("Votre prénom doit contenir uniquement des lettres.")
            except ValueError:
                break
        return user_input

    @staticmethod
    def get_player_birthday():
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

            print(f"Votre date de naissance est : {user_input_day}/{user_input_month}/{user_input_year}")
            return f"{user_input_day}/{user_input_month}/{user_input_year}"

    @staticmethod
    def get_player_identifier():
        user_id = (f"{random.randint(1000, 9999)}"
                   f"{random.choice(string.ascii_letters)}"
                   f"{random.choice(string.ascii_letters)}"
                   f"{random.choice(string.ascii_letters)}"
                   f"{random.randint(1000, 9999)}")
        print("Voici votre ID : ", user_id)
        return user_id
