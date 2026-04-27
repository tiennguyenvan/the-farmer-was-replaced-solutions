import f0
import f1
import f2


def is_carrot_low():
    return num_items(Items.Carrot) < 1000000000


def is_carrot_high():
    return num_items(Items.Carrot) > 1200000000


def farm_carrot(stop_check=f0.none_func):

    def own_stop_check():
        return stop_check() == True or f1.is_hay_low() or f2.is_wood_low()

    def __plant_carrot():
        f0.plant_care(Entities.Carrot, True)
    while stop_check() != True:
        f0.go_to(0, 0)
        for i in range(max_drones()-1):
            spawn_drone(f0.action_on_area, 0, i, f0.FULL_SIZE,
                        1, __plant_carrot, own_stop_check)
            f0.go_to(0, i+1)

        f0.action_on_area(0, get_pos_y(), f0.FULL_SIZE,
                          1, __plant_carrot, own_stop_check)
        if f1.is_hay_low():
            f1.farm_hay(f1.is_hay_high)
        if f2.is_wood_low():
            f2.farm_wood(f2.is_wood_high)


if __name__ == "__main__":
    farm_carrot()
