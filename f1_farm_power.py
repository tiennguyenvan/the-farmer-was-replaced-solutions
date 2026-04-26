

import f0
SUNFLOWERS = {}


def farm_power():
    def __clear_map():
        global SUNFLOWERS
        SUNFLOWERS = {}

    def __one_row_care():
        global SUNFLOWERS
        f0.plant_care(Entities.Sunflower, False)
        power = measure()
        if not (power in SUNFLOWERS):
            SUNFLOWERS[power] = []
        SUNFLOWERS[power].append((get_pos_x(), get_pos_y()))

    def __one_drone_care(y):
        global SUNFLOWERS
        f0.go_to(0, y)
        f0.action_on_area(f0.FULL_SIZE, 1, __one_row_care)
        return SUNFLOWERS

    f0.all_till_full_board()
    while True:
        handles = f0.all_action_w_index(__one_drone_care)
        for i in range(1, max_drones()):
            single_sunflower = wait_for(handles[i])
            for power in single_sunflower:
                for pos in single_sunflower[power]:
                    if not (power in SUNFLOWERS):
                        SUNFLOWERS[power] = []
                    SUNFLOWERS[power].append(pos)
        for power in range(15, 6, -1):
            if not (power in SUNFLOWERS):
                continue
            while len(SUNFLOWERS[power]) > 0:
                pos = SUNFLOWERS[power].pop()
                f0.go_to(pos[0], pos[1])
                harvest()
        f0.all_action(__clear_map)


farm_power()
