from controller.player_controller import PlayerController


def test():
    x = input("lsdjs : ")
    if x != str(1):
        return test()
    return x


def main():

    player_controller = PlayerController(view=True)
    player_controller.add_new_player()


print(main())
