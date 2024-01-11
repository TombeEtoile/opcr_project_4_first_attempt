import uuid


class PlayerView:
    """Les joueurs entrent leur données"""

    def ask_player_identity(self, name: str, surname: str, birthday: str, identifier: str):

        PlayerView.ask_player_identity(self, name=name, surname=surname, birthday=birthday, identifier=identifier)
        name = input("Entrez votre nom : ")
        surname = input("Entrez votre prénoms : ")
        birthday = input("Entrez votre date d'anniversaire sous la forme jj/mm/aaaa : ")
        identifier = uuid.uuid1().__str__()
        if not name or surname or birthday or identifier:
            return
        return name, surname, birthday, identifier


player = PlayerView()
player.ask_player_identity(name=)  # --> PK forcément name= ???
