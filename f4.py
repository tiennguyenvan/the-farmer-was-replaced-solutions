import f0
import f3
import f8

PUMPKIN_MAP = {}


def farm_pumpkin(stop_check=f0.none_func):

    def __clear_map():
        global PUMPKIN_MAP
        PUMPKIN_MAP = {}

    def __row_finished():
        global PUMPKIN_MAP
        return len(PUMPKIN_MAP) >= f0.FULL_SIZE

    def _one_cell_care():
        if get_entity_type() != Entities.Pumpkin or get_entity_type() == Entities.Dead_Pumpkin:
            f0.plant_care(Entities.Pumpkin, True)
            return

        if not can_harvest():
            return
        global PUMPKIN_MAP
        PUMPKIN_MAP[(get_pos_x(), get_pos_y())] = True
        return not __row_finished()

    y = 0
    y_step = 1
    while stop_check() != True:
        for _ in range(max_drones()-1):
            spawn_drone(f0.action_on_area, 0, y, f0.FULL_SIZE,
                        1, _one_cell_care, stop_check)
            y += y_step
            f0.go_to(0, y)

        f0.action_on_area(0, get_pos_y(), f0.FULL_SIZE,
                          1, _one_cell_care, stop_check)
        f0.wait_all_clones_finished()
        f0.all_drones_action(__clear_map)
        harvest()
        y_step = -y_step
        quick_print(f3.is_carrot_low())
        quick_print(num_items(Items.Carrot))

        if f3.is_carrot_low():
            f3.farm_carrot(f3.is_carrot_high)
        if f8.is_power_low():
            f8.farm_power(f8.is_power_high)


if __name__ == "__main__":
    farm_pumpkin()
