import random
import uuid


class PlayerSetUp:
    """Création d'un joueur random"""

    def __init__(self):
        pass

    def player_identity(self):
        """Nom + prénoms"""

        name_list = ("Dubois", "Martin", "Lefèvre", "Leroy", "Moreau", "Simon", "Laurent", "Michel", "Garcia", "Dupont", "Fournier", "Lopez", "Roux", "Fontaine", "Chevalier", "Girard", "Dufour", "Garnier", "Leclerc", "Rousseau")
        surname_list = ("Léa", "Thomas", "Clara", "Nathan", "Manon", "Hugo", "Camille", "Ethan", "Inès", "Lucas", "Jade", "Enzo", "Zoé", "Gabriel", "Émilie", "Théo", "Sarah", "Noah", "Lucie", "Liam")
        random_name = random.randint(0, len(name_list) - 1)
        random_surname = random.randint(0, len(surname_list) - 1)
        return print(f"{name_list[random_name]} {surname_list[random_surname]}")

    def player_birthday(self):
        """Date d'anniversaire"""

        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(1964, 2006)
        birthday = f"{day}/{month}/{year}"
        return print(birthday)

    def player_id(self):
        """ID du joueur"""

        id = uuid.uuid1()
        return print(id)



# Appeler la class PlayerSetUp()

player = PlayerSetUp()
player.player_identity()
player.player_birthday()
player.player_id()
