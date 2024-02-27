class PlayerModel:

    def __init__(self, p_name, p_surname, p_birthday, p_identifier, p_elo):
        """define a player with a name, surname, birthday and id"""

        self.name = p_name
        self.surname = p_surname
        self.birthday = p_birthday
        self.identifier = p_identifier
        self.elo = p_elo
