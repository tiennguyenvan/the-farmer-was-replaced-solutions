import f0


def farm_hay():

    def grass_care():
        f0.plant_care(Entities.Grass)

    while True:
        # f0.full_board_action(grass_care)
        f0.full_board_action(grass_care, True)


PUMPKIN_MAP = {}


def farm_pumpkin():
    def clear_pumpkin_map():
        global PUMPKIN_MAP
        PUMPKIN_MAP = {}

    def harvest_all_pumpkins():
        while num_drones() > 1:
            continue
        for i in range(1, max_drones()):
            spawn_drone(clear_pumpkin_map)
            continue
        clear_pumpkin_map()
        harvest()

    def row_finished():
        global PUMPKIN_MAP
        return len(PUMPKIN_MAP) >= f0.FULL_SIZE

    def pumpkin_care():
        if get_entity_type() != Entities.Pumpkin:
            plant(Entities.Pumpkin)
            return
        if get_entity_type() == Entities.Dead_Pumpkin:
            harvest()
            plant(Entities.Pumpkin)
            return
        if not can_harvest():
            return
        global PUMPKIN_MAP
        PUMPKIN_MAP[(get_pos_x(), get_pos_y())] = True
        return not row_finished()

    f0.full_board_action(pumpkin_care, True, row_finished,
                         harvest_all_pumpkins)

    # while row_finished() == False:
    #    f0.go_to(0, 0)
    #    f0.do_action_on_area(f0.FULL_SIZE, 1, pumpkin_care)


farm_pumpkin()
