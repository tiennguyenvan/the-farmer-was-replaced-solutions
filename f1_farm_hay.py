import f0


def grass_care():
    f0.plant_care(Entities.Grass)


def farm_hay():
    while True:
        f0.full_board_action(grass_care)
