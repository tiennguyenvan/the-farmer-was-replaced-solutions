

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
        pos = (get_pos_x(), get_pos_y())
        if f0.is_even(get_pos_y()):
            SUNFLOWERS[power].append(pos)
        else:
            SUNFLOWERS[power].insert(0, pos)

    def __one_drone_care(y):
        global SUNFLOWERS
        f0.go_to(0, y)
        f0.action_on_area(f0.FULL_SIZE, 1, __one_row_care)
        return SUNFLOWERS

    handles = f0.all_action_w_index(__one_drone_care)
    indexed = {}
    for row in range(1, max_drones()):
        indexed[row] = wait_for(handles[row])
    indexed[0] = SUNFLOWERS

    SCHEDULE = []
    sweep_up = True
    for power in range(15, 6, -1):
        if sweep_up:
            row_start = 0
            row_stop = max_drones()
            row_step = 1
        else:
            row_start = max_drones() - 1
            row_stop = -1
            row_step = -1

        for row in range(row_start, row_stop, row_step):
            if not (power in indexed[row]):
                continue
            row_positions = indexed[row][power]
            if sweep_up:
                for j in range(len(row_positions)):
                    SCHEDULE.append(row_positions[j])
            else:
                for j in range(len(row_positions) - 1, -1, -1):
                    SCHEDULE.append(row_positions[j])
        sweep_up = not sweep_up

    row = 0
    while row < len(SCHEDULE):
        pos = SCHEDULE[row]
        f0.go_to(pos[0], pos[1])
        harvest()
        row += 1

    f0.all_action(__clear_map)


while True:
    farm_power()
