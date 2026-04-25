full_size = get_world_size()
half_size = full_size/2
quad_size = full_size/4
octa_size = full_size/8
hexa_size = full_size/16

# module acts as a helper


def is_even(num):
    return num % 2 == 0


def is_odd(num):
    return num % 2 != 0


def is_chess_tile(x, y):
    return is_even(x) == is_even(y)


def chessboard_action(primary_action, secondary_action):
    if is_chess_tile():
        primary_action()
    else:
        secondary_action()


def go_to_xy(x, y):
    dx = x - get_pos_x()
    dy = y - get_pos_y()
    dir_x = East
    if dx < 0:
        dir_x = West
    dir_y = North
    if dy < 0:
        dir_y = South

    for _ in range(abs(dx)):
        if not can_move(dir_x):
            return False
        move(dir_x)

    for _ in range(abs(dy)):
        if not can_move(dir_y):
            return False
        move(dir_y)

    return True


def false_function():
    return False


def do_action_on_area(width, height, action, pad_left=0, should_stop=false_function):
    for row in range(height):
        for col in range(width):
            if should_stop():
                return

            action()
            if col == width - 1:
                break

            if is_even(row):
                move(East)
            else:
                if pad_left and col < pad_left:
                    continue
                move(West)

        if row == height - 1:
            break
        move(North)

    for _ in range(pad_left):
        move(West)
    for _ in range(height - 1):
        move(South)
    if is_odd(height):
        for _ in range(width - pad_left - 1):
            move(West)


def plant_care(entity_name, water_threshold=0.5):
    if get_entity_type() == Entities.Dead_Pumpkin:
        plant(Entities.Pumpkin)
        return

    if can_harvest():
        harvest()
    if get_entity_type() != Entities.Grass and get_entity_type() != Entities.Bush and get_entity_type() != Entities.Tree and get_ground_type() != Grounds.Soil:
        till()
    plant(entity_name)

    if get_water() < water_threshold:
        use_item(Items.Water)
    best_infect_pos = get_pos_x() % 3 == 1 and get_pos_y() % 3 == 1
    if best_infect_pos:
        use_item(Items.Fertilizer)
        use_item(Items.Weird_Substance)


def full_board_action(action, should_stop=false_function, soil_required=False):
    go_to_xy(0, 0)
    if soil_required:
        while num_drones() < max_drones():
            spawn_drone(do_action_on_area, full_size, full_size, till)
        do_action_on_area(full_size, full_size, till)
    while num_drones() < max_drones():
        spawn_drone(do_action_on_area, full_size,
                    full_size, action, 0, should_stop)
        print(num_drones())
    do_action_on_area(full_size, full_size, action, 0, should_stop)
