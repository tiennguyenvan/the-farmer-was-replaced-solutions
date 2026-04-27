

import f0
import f3
SUNFLOWERS = {}


def is_power_low():
    return num_items(Items.Power) < 500000


def is_power_high():
    return num_items(Items.Power) > 1000000


def farm_power(stop_check=f0.none_func):
    f0.go_to(0, 0)

    def __clear_map():
        global SUNFLOWERS
        SUNFLOWERS = {}

    def __one_row_care():
        global SUNFLOWERS
        f0.plant_care(Entities.Sunflower)
        power = measure()
        if not (power in SUNFLOWERS):
            SUNFLOWERS[power] = []
        SUNFLOWERS[power].append((get_pos_x(), get_pos_y()))
        return get_pos_x() != f0.FULL_SIZE - 1

    def __one_drone_care(y):
        global SUNFLOWERS
        f0.action_on_area(0, y, f0.FULL_SIZE, 1, __one_row_care)
        return SUNFLOWERS

    def __harvest_at_positions(positions):
        for pos in positions:
            f0.go_to(pos[0], pos[1])
            harvest()

    while stop_check() != False:
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
                    spawn_drone(__harvest_at_positions, indexed[y][power])
                y = y + y_step
                f0.go_to(0, y)
            if power in indexed[y]:
                f0.wait_available_drone()
                spawn_drone(__harvest_at_positions, indexed[y][power])
            f0.wait_all_clones_finished()
            y_step = -y_step

        f0.all_drones_action(__clear_map)


if __name__ == "__main__":
    farm_power()
