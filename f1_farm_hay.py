import f0


def farm_hay():

    def grass_care():
        f0.plant_care(Entities.Grass, False)

    while True:
        # f0.full_board_action(grass_care)
        f0.full_board_action(grass_care, True)
