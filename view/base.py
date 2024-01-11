class PassivView:
    """call the PlayerView"""

    def __init__(self, player_view, view):
        """Init the player view and the view"""

        self.player_view = player_view
        self.view = view

    def ask_player_identity(self):
        """call the player player view"""

        return self.player_view.ask_player_identity()
