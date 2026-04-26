FULL_SIZE = get_world_size()
HALF_SIZE = FULL_SIZE/2
QUAD_SIZE = FULL_SIZE/4
OCTA_SIZE = FULL_SIZE/8
HEXA_SIZE = FULL_SIZE/16


def is_even(num):
    return num % 2 == 0


def is_odd(num):
    return num % 2 != 0


def none_func(any_arg=None):
    return


def is_chess_tile(x, y):
    return is_even(x) == is_even(y)


def chessboard_action(primary_action, secondary_action):
    if is_chess_tile(get_pos_x(), get_pos_y()):
        primary_action()
    else:
        secondary_action()


def go_to(x, y, action_during_move=none_func):
    dx = x - get_pos_x()
    dy = y - get_pos_y()
    dir_x = East
    if dx < 0:
        dir_x = West
    dir_y = North
    if dy < 0:
        dir_y = South

    for _ in range(abs(dx)):
        if action_during_move() == False or not can_move(dir_x):
            return False

        move(dir_x)

    for _ in range(abs(dy)):
        if action_during_move() == False or not can_move(dir_y):
            return False
        move(dir_y)

    return True


def action_on_area(width, height, action):
    for row in range(height):
        for col in range(width):
            if action() == False:
                return
            if col == width - 1:
                break

            if is_even(row):
                move(East)
            else:
                move(West)

        if row == height - 1:
            break
        move(North)


def soil_required(entity_name):
    return entity_name != Entities.Grass and entity_name != Entities.Bush and entity_name != Entities.Tree and get_ground_type() != Grounds.Soil


def plant_care(entity_name, auto_harvest=False):
    if get_entity_type() == Entities.Dead_Pumpkin:
        plant(Entities.Pumpkin)
        return

    if auto_harvest and can_harvest():
        harvest()
    if soil_required(entity_name):
        till()
    if entity_name != Entities.Grass:
        plant(entity_name)

    if get_water() < 0.5:
        use_item(Items.Water)
    best_infect_pos = get_pos_x() % 3 == 1 and get_pos_y() % 3 == 1
    if best_infect_pos:
        use_item(Items.Fertilizer)
        use_item(Items.Weird_Substance)


def all_clones_finished():
    return num_drones() == 1


def till_one_row(y):
    go_to(0, y)
    action_on_area(FULL_SIZE, 1, till)


def all_till_full_board():
    clear()
    all_action_w_index(till_one_row)


def all_action_w_index_w_arg(action, arg, n=None):
    hanles = {}
    if n == None:
        n = max_drones()
    for i in range(1, n):
        hanles[i] = spawn_drone(action, i, arg)
    hanles[0] = action(0, arg)
    while not all_clones_finished():
        continue
    return hanles


def all_action_w_index(action, n=None):
    hanles = {}
    if n == None:
        n = max_drones()
    for i in range(1, n):
        hanles[i] = spawn_drone(action, i)
    hanles[0] = action(0)
    while not all_clones_finished():
        continue
    return hanles


def all_action(action, n=None):
    hanles = {}
    if n == None:
        n = max_drones()
    for i in range(1, n):
        hanles[i] = spawn_drone(action)
    hanles[0] = action()
    while not all_clones_finished():
        continue
    return hanles


def all_action_w_arg(action, arg, n=None):
    hanles = {}
    if n == None:
        n = max_drones()
    for i in range(1, n):
        hanles[i] = spawn_drone(action, arg)
    hanles[0] = action(arg)
    while not all_clones_finished():
        continue
    return hanles
