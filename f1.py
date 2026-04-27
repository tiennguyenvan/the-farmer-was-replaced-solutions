import f0


def is_hay_low():
    return num_items(Items.Hay) <= 1100000000


def is_hay_high():
    return num_items(Items.Hay) > 1200000000


def farm_hay(stop_check=f0.none_func):
    clear()
    f0.go_to(0, 0)
    for i in range(max_drones()-1):
        spawn_drone(f0.action_on_area, 0, i, f0.FULL_SIZE,
                    1, harvest, stop_check)
        f0.go_to(0, i+1)

    f0.action_on_area(0, get_pos_y(), f0.FULL_SIZE,
                      1, harvest, stop_check)


if __name__ == "__main__":
    farm_hay()
