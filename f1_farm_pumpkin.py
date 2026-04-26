import f0


PUMPKIN_MAP = {}


def farm_pumpkin():
    def __clear_map():
        global PUMPKIN_MAP
        PUMPKIN_MAP = {}

    def __row_finished():
        global PUMPKIN_MAP
        return len(PUMPKIN_MAP) >= f0.FULL_SIZE

    def _one_cell_care():
        if get_entity_type() != Entities.Pumpkin:
            f0.plant_care(Entities.Pumpkin)
            return
        if get_entity_type() == Entities.Dead_Pumpkin:
            harvest()
            f0.plant_care(Entities.Pumpkin)
            return
        if not can_harvest():
            return
        global PUMPKIN_MAP
        PUMPKIN_MAP[(get_pos_x(), get_pos_y())] = True
        return not __row_finished()

    def __one_drone_care(y):
        while not __row_finished():
            f0.go_to(0, y)
            # print(y)
            f0.action_on_area(f0.FULL_SIZE, 1, _one_cell_care)

    f0.all_till_full_board()
    while True:
        f0.all_action_w_index(__one_drone_care)
        f0.all_action(__clear_map)
        harvest()


farm_pumpkin()
