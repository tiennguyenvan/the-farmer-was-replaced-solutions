

import f0
SUNFLOWERS = {}

clear()


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

    def __harvest_in_power(positions):
        for pos in positions:
            f0.go_to(pos[0], pos[1])
            harvest()

    indexed = {}
    y_step = 1
    handles = {}
    y = 0
    for _ in range(max_drones()-1):
        handles[y] = spawn_drone(__one_drone_care, y)
        y = y + y_step
        f0.go_to(0, y)
    f0.wait_available_drone()
    handles[y] = spawn_drone(__one_drone_care, y)
    f0.wait_all_clones_finished()
    y_step = -y_step

    for row in range(max_drones()):
        indexed[row] = wait_for(handles[row])

    for power in range(15, 6, -1):
        for i in range(max_drones()-1):
            if power in indexed[y]:
                spawn_drone(__harvest_in_power, indexed[y][power])
            y = y + y_step
            f0.go_to(0, y)
        if power in indexed[y]:
            f0.wait_available_drone()
            spawn_drone(__harvest_in_power, indexed[y][power])
        f0.wait_all_clones_finished()
        y_step = -y_step

    f0.all_action(__clear_map)


while True:
    farm_power()
