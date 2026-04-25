# module acts as a helper

SOLO_FARMING = False
CATUS_TO_PUMPKIN_RATE = 64
PUMPKIN_TO_CARROT_RATE = 512
CARROT_TO_HAY_RATE = 512
CARROT_TO_WOOD_RATE = 512
APPLE_TO_CACTUS_RATE = 16


def needed_items_for_target(target_amount, item_name, source_amount=0, rate=1):
    """Return how many more source items are needed for a target amount."""
    remaining_target = target_amount - num_items(item_name)
    if remaining_target <= 0:
        return 0

    needed_source = remaining_target * rate
    needed_source -= source_amount
    if needed_source <= 0:
        return 0

    return needed_source


def pumpkin_needed_more_for_target_cactus(target_cactus):
    return needed_items_for_target(
        target_cactus,
        Items.Cactus,
        num_items(Items.Pumpkin),
        CATUS_TO_PUMPKIN_RATE,
    )


def carrot_needed_more_for_target_pumpkin(target_pumpkin):
    return needed_items_for_target(
        target_pumpkin,
        Items.Pumpkin,
        num_items(Items.Carrot),
        PUMPKIN_TO_CARROT_RATE,
    )


def hay_needed_more_for_target_carrot(target_carrot):
    return needed_items_for_target(
        target_carrot,
        Items.Carrot,
        num_items(Items.Hay),
        CARROT_TO_HAY_RATE,
    )


def wood_needed_more_for_target_carrot(target_carrot):
    return needed_items_for_target(
        target_carrot,
        Items.Carrot,
        num_items(Items.Wood),
        CARROT_TO_WOOD_RATE,
    )


def cactus_needed_more_for_target_apple(target_apple):
    return needed_items_for_target(
        target_apple,
        Items.Bone,
        num_items(Items.Cactus),
        APPLE_TO_CACTUS_RATE,
    )


def carrot_needed_more_for_sunflower(target_sunflower):
    return needed_items_for_target(
        target_sunflower,
        Items.Power,
        num_items(Items.Carrot),
    )


def is_even(num):
    return num % 2 == 0


def is_odd(num):
    return num % 2 != 0


def is_checkerboard_tile(x=None, y=None):
    if x is None:
        x = get_pos_x()
    if y is None:
        y = get_pos_y()
    return is_even(x) == is_even(y)


def go_to_xy(x, y):
    cur_x = get_pos_x()
    cur_y = get_pos_y()
    dx = x - cur_x
    dy = y - cur_y
    moved_cleanly = True

    if SOLO_FARMING and random() < 0.01:
        do_a_flip()

    for _ in range(abs(dx)):
        if dx < 0:
            if not can_move(West):
                moved_cleanly = False
            move(West)
        else:
            if not can_move(East):
                moved_cleanly = False
            move(East)

    for _ in range(abs(dy)):
        if dy < 0:
            if not can_move(South):
                moved_cleanly = False
            move(South)
        else:
            if not can_move(North):
                moved_cleanly = False
            move(North)

    return moved_cleanly


def move_whole_area_do_action(width, height, action, pad_left=0, should_stop=None):
    for row in range(height):
        for col in range(width):
            if should_stop and should_stop():
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


def ensure_soil(start_x, start_y, width, height):
    go_to_xy(start_x, start_y)
    if get_ground_type() != Grounds.Soil:
        move_whole_area_do_action(width, height, till)


def plant_care_harvest(entity_name, water_threshold=0.5):
    if get_entity_type() == Entities.Dead_Pumpkin:
        plant(Entities.Pumpkin)
        return

    if can_harvest():
        harvest()

    plant(entity_name)

    if get_water() < water_threshold:
        use_item(Items.Water)


def checkerboard_action(primary_action, secondary_action):
    if is_checkerboard_tile():
        primary_action()
    else:
        secondary_action()


def farm_entity_forever(start_x, start_y, width, height, entity_name, needs_soil=True):
    if needs_soil:
        ensure_soil(start_x, start_y, width, height)
    else:
        go_to_xy(start_x, start_y)

    def action():
        plant_care_harvest(entity_name)

    while True:
        move_whole_area_do_action(width, height, action)
