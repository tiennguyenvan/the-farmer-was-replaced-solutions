import f0


def is_wood_low():
    return num_items(Items.Wood) < 10000000000


def is_wood_high():
    return num_items(Items.Wood) > 12000000000


def farm_wood(stop_check=f0.none_func):
    clear()
    f0.go_to(0, 0)

    def __plant_bush():
        f0.plant_care(Entities.Bush, True)

    def __plant_tree():
        f0.plant_care(Entities.Tree, True)

    def __cell_care():
        f0.chessboard_action(__plant_tree, __plant_bush)

    for i in range(max_drones()-1):
        spawn_drone(f0.action_on_area, 0, i, f0.FULL_SIZE,
                    1, __cell_care, stop_check)
        f0.go_to(0, i+1)

    f0.action_on_area(0, get_pos_y(), f0.FULL_SIZE,
                      1, __cell_care, stop_check)


if __name__ == "__main__":
    farm_wood()
