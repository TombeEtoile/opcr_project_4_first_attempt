import uuid


class PlayerView:
    """Les joueurs entrent leur données"""

    @staticmethod
    def get_player_data():
        name = PlayerView.get_player_name()
        surname = PlayerView.get_player_surname()
        birthday = PlayerView.get_player_birthday()
        identifier = PlayerView.get_player_identifier()
        player_test = {name, surname, birthday, identifier}
        return player_test

    @staticmethod
    def get_player_name():
        return input("Entrez votre nom : ")

    @staticmethod
    def get_player_surname():
        return input("Entrez votre prénom : ")  # Faire du récursif pur la validation de champ

    @staticmethod
    def get_player_birthday():
        return input("Entrez votre date de naissance (sous la forme jj/mm/aaa) : ")

    @staticmethod
    def get_player_identifier():
        return uuid.uuid1()


player = PlayerView()
print(player.get_player_data())
