
# dummy drone module for testing
# def clear(): return None
# def move(direction): return None
# def tile(): return None
# def plant(name): return None
# def harvest(): return None
# def abs(num): return None
# def can_harvest(): return None
# def can_move(): return None
# def change_hat(hat): return None
# def clear(): return None
# def do_a_flip(): return None
# def get_companion(): return None
# def get_entity_type(): return None
# def get_ground_type(): return None
# def get_pos_x(): return None
# def get_pos_y(): return None
# def get_tick_count(): return None
# def get_time(): return None
# def get_water(): return None
# def get_world_size(): return None
# def harvest(): return None
# def has_finished(): return None
# def len(obj): return None
# def list(obj): return None
# def max(obj): return None
# def max_drones(): return None
# def measure(): return None
# def min(obj): return None
# def move(direction): return None
# def num_drones(): return None
# def num_items(): return None
# def num_unlocked(): return None
# def pet_the_piggy(): return None
# def plant(id): return None
# def print(obj): return None
# def quick_print(obj): return None
# def random(): return None
# def range(start, stop=None, step=None): return None
# def set_execution_speed(speed): return None
# def set_world_size(size): return None
# def spawn_drone(x, *y): return None
# def str(obj): return None
# def swap(a, b): return None
# def tap(x, y): return None
# def till(x, y): return None
# def use_item(id): return None
# def wait_for(condition): return None


# East = "right"
# West = "left"
# North = "up"
# South = "down"


# class Entities:
#    Apple = "Apple"
#    Bush = "Bush"
#    Cactus = "Cactus"
#    Carrot = "Carrot"
#    Dead_Pumpkin = "Dead_Pumpkin"
#    Dinosaur = "Dinosaur"
#    Grass = "Grass"
#    Hedge = "Hedge"
#    Pumpkin = "Pumpkin"
#    Sunflower = "Sunflower"
#    Treasure = "Treasure"
#    Tree = "Tree"


# class Items:
#    Hay = "Hay"
#    Wood = "Wood"
#    Carrot = "Carrot"
#    Pumpkin = "Pumpkin"
#    Cactus = "Cactus"
#    Bone = "Bone"
#    Weird_Substance = "Weird_Substance"
#    Gold = "Gold"
#    Water = "Water"
#    Fertilizer = "Fertilizer"
#    Power = "Power"


# class Unlocks:
#    Cactus = "Cactus"
#    Carrots = "Carrots"
#    Debug = "Debug"
#    Debug_2 = "Debug_2"
#    Dinosaurs = "Dinosaurs"
#    Expand = "Expand"
#    Expand_2 = "Expand_2"
#    Fertilizer = "Fertilizer"
#    Functions = "Functions"
#    Grass = "Grass"
#    Hats = "Hats"
#    Lists = "Lists"
#    Loops = "Loops"
#    Mazes = "Mazes"
#    Megafarm = "Megafarm"
#    Operators = "Operators"
#    Plant = "Plant"
#    Polyculture = "Polyculture"
#    Pumpkins = "Pumpkins"
#    Senses = "Senses"
#    Speed = "Speed"
#    Sunflowers = "Sunflowers"
#    Timing = "Timing"
#    Trees = "Trees"
#    Utilities = "Utilities"
#    Variables = "Variables"
#    Watering = "Watering"


# class Hats:
#    Gray_Hat = "Gray_Hat"
#    Purple_Hat = "Purple_Hat"
#    Green_Hat = "Green_Hat"
#    Brown_Hat = "Brown_Hat"
#    Dinosaur_Hat = "Dinosaur_Hat"


# class Grounds:
#    Soil = "Soil"
#    Sand = "Sand"
#    Grass = "Grass"
#    Stone = "Stone"
#    Water = "Water"


# carrot needs: 512 hay, 512 wood
# pumpkin needs: 512 carrot
# catus needs: 64 pumpkin
# apple needs: 16 cactus
# treasure/hedge needs: 1 weird substance
# target = 10M catus
SOLO_FARMING = False
CATUS_TO_PUMPKIN_RATE = 64
PUMPKIN_TO_CARROT_RATE = 512
CARROT_TO_HAY_RATE = 512
CARROT_TO_WOOD_RATE = 512
APPLE_TO_CACTUS_RATE = 16


def pumpking_needed_more_for_target_cactus(target_cactus):
    remaining_needed_cactus = target_cactus - num_items(Items.Cactus)
    if remaining_needed_cactus <= 0:
        return 0
    needed_pumpkin = remaining_needed_cactus * CATUS_TO_PUMPKIN_RATE
    needed_pumpkin -= num_items(Items.Pumpkin)
    if (needed_pumpkin <= 0):
        return 0
    return needed_pumpkin


def carrot_needed_more_for_target_pumpkin(target_pumpkin):
    remaining_needed_pumpkin = target_pumpkin - num_items(Items.Pumpkin)
    if remaining_needed_pumpkin <= 0:
        return 0
    needed_carrot = remaining_needed_pumpkin * PUMPKIN_TO_CARROT_RATE
    needed_carrot -= num_items(Items.Carrot)
    if (needed_carrot <= 0):
        return 0
    return needed_carrot


def hay_needed_more_for_target_carrot(target_carrot):
    remaining_needed_carrot = target_carrot - num_items(Items.Carrot)
    if remaining_needed_carrot <= 0:
        return 0
    needed_hay = remaining_needed_carrot * CARROT_TO_HAY_RATE
    needed_hay -= num_items(Items.Hay)
    if (needed_hay <= 0):
        return 0
    return needed_hay


def wood_needed_more_for_target_carrot(target_carrot):
    remaining_needed_carrot = target_carrot - num_items(Items.Carrot)
    if remaining_needed_carrot <= 0:
        return 0
    needed_wood = remaining_needed_carrot * CARROT_TO_WOOD_RATE
    needed_wood -= num_items(Items.Wood)
    if (needed_wood <= 0):
        return 0
    return needed_wood


def cactus_needed_more_for_target_apple(target_apple):
    remaining_needed_apple = target_apple - num_items(Items.Bone)
    if remaining_needed_apple <= 0:
        return 0
    needed_cactus = remaining_needed_apple * APPLE_TO_CACTUS_RATE
    needed_cactus -= num_items(Items.Cactus)
    if (needed_cactus <= 0):
        return 0
    return needed_cactus


def carrot_needed_more_for_sunflower(target_sunflower):
    remaining_needed_sunflower = target_sunflower - num_items(Items.Power)
    if remaining_needed_sunflower <= 0:
        return 0
    needed_carrot = remaining_needed_sunflower
    needed_carrot -= num_items(Items.Carrot)
    if (needed_carrot <= 0):
        return 0
    return needed_carrot


target_apple = 100000000
target_catus = 10000000 + cactus_needed_more_for_target_apple(target_apple)
target_pumpkin = pumpking_needed_more_for_target_cactus(target_catus)
target_carrot = carrot_needed_more_for_target_pumpkin(target_pumpkin)
target_hay = hay_needed_more_for_target_carrot(target_carrot)
target_wood = wood_needed_more_for_target_carrot(target_carrot)
min_energy = 100000

# plant and havest by id
clear()
full_size = get_world_size()
half_size = full_size/2
quad_size = full_size/4
octa_size = full_size/8
hexa_size = full_size/16


def go_to_xy(x, y):
    cur_x = get_pos_x()
    cur_y = get_pos_y()
    x = x - cur_x
    y = y - cur_y
    ret = True
    if random() < 0.01 and SOLO_FARMING:
        do_a_flip()
    for i in range(abs(x)):
        if x < 0:
            if not can_move(West):
                ret = False
            move(West)
        else:
            if not can_move(East):
                ret = False
            move(East)
    for i in range(abs(y)):
        if y < 0:
            if not can_move(South):
                ret = False
            move(South)
        else:
            if not can_move(North):
                ret = False
            move(North)
    return ret


def is_even(num):
    return num % 2 == 0


def is_odd(num):
    return num % 2 != 0


def move_whole_area_do_action(width, height, action, pad_left=0, should_check_stop=False, stop_check=None):
    for i in range(height):
        for j in range(width):
            if should_check_stop and stop_check():
                return
            action()
            if j == width-1:
                break

            if is_even(i):
                move(East)
            else:
                if pad_left and j < pad_left:
                    continue
                move(West)
        if i == height-1:
            break
        move(North)

    # reset position
    for i in range(pad_left):
        move(West)
    for i in range(height-1):
        move(South)
    if is_odd(height):
        for i in range(height):
            move(West)


def plant_care_harvest(plantName):
    if get_entity_type() == Entities.Dead_Pumpkin:
        plant(Entities.Pumpkin)
        return
    if can_harvest():
        harvest()
    plant(plantName)
    if get_water() < 0.5:
        use_item(Items.Water)
    # if random() < 0.1 and num_items(Items.Fertilizer) > 0:
    #    use_item(Items.Fertilizer)


def start_and_till_if_needed(start_x, start_y, width, height):
    go_to_xy(start_x, start_y)
    if get_ground_type() != Grounds.Soil:
        move_whole_area_do_action(width, height, till)


def farm_pumpkin(start_x, start_y, width, height):
    start_and_till_if_needed(start_x, start_y, width, height)

    def plant_and_harvest_pumpkin():
        plant_care_harvest(Entities.Pumpkin)

    while True:
        move_whole_area_do_action(width, height, plant_and_harvest_pumpkin)


def farm_carrot(start_x, start_y, width, height):
    start_and_till_if_needed(start_x, start_y, width, height)

    def plant_and_harvest_carrot():
        plant_care_harvest(Entities.Carrot)

    while True:
        move_whole_area_do_action(width, height, plant_and_harvest_carrot)


def farm_hay(start_x, start_y, width, height):
    go_to_xy(start_x, start_y)

    def plant_and_harvest_hay():
        if can_harvest():
            harvest()
        plant(Entities.Grass)

    while True:
        move_whole_area_do_action(width, height, plant_and_harvest_hay)


def farm_hay_and_tree(start_x, start_y, width, height):
    go_to_xy(start_x, start_y)

    def plant_and_harvest_hay_and_tree():
        odd_row = is_odd(get_pos_y())
        odd_col = is_odd(get_pos_x())
        even_row = not odd_row
        even_col = not odd_col
        if odd_row and odd_col or (even_row and even_col):
            plant_care_harvest(Entities.Tree)
        else:
            harvest()
    while True:
        move_whole_area_do_action(
            width, height, plant_and_harvest_hay_and_tree)


def farm_bush_and_tree(start_x, start_y, width, height):
    go_to_xy(start_x, start_y)

    def plant_and_harvest_bush_and_tree():
        odd_row = is_odd(get_pos_y())
        odd_col = is_odd(get_pos_x())
        even_row = not odd_row
        even_col = not odd_col
        if odd_row and odd_col or (even_row and even_col):
            plant_care_harvest(Entities.Tree)
        else:
            plant_care_harvest(Entities.Bush)
    while True:
        move_whole_area_do_action(
            width, height, plant_and_harvest_bush_and_tree)


def farm_sunflower(start_x, start_y, width, height):
    start_and_till_if_needed(start_x, start_y, width, height)

    def plant_and_harvest_sunflower():
        plant_care_harvest(Entities.Sunflower)

    while True:
        move_whole_area_do_action(width, height, plant_and_harvest_sunflower)


def farm_cactus(start_x, start_y, width, height):
    start_and_till_if_needed(start_x, start_y, width, height)

    def plant_and_harvest_cactus():
        plant_care_harvest(Entities.Cactus)

    while True:
        move_whole_area_do_action(width, height, plant_and_harvest_cactus)


def farm_bush(start_x, start_y, width, height):
    start_and_till_if_needed(start_x, start_y, width, height)

    def plant_and_harvest_bush():
        plant_care_harvest(Entities.Bush)

    while True:
        move_whole_area_do_action(width, height, plant_and_harvest_bush)


def solve_maze():
    maze_pos = measure()
    if maze_pos == None:
        return
    dir = [North, East, South, West]
    d_len = len(dir)
    i = 0
    while get_entity_type() != Entities.Treasure:
        if measure() == None:
            break
        right = (i+1) % d_len
        left = (i-1) % d_len
        front = i
        back = (i+2) % d_len
        for d in [right, front, left, back]:
            if can_move(dir[d]):
                move(dir[d])
                i = d
                break
    harvest()


def loop_solve_maze(start_x, start_y, width, height):
    go_to_xy(start_x+width//2, start_y+height//2)
    do_a_flip()

    def out_of_maze():
        return get_pos_x() >= start_x+width or get_pos_x() < start_x or get_pos_y() >= start_y+height or get_pos_y() < start_y

    def come_back_to_maze():
        return go_to_xy(start_x+width//2, start_y+height//2)
    while True:
        solve_maze()
        while out_of_maze():
            come_back_to_maze()


def farm_maze(start_x, start_y, width, height):
    do_a_flip()
    while True:
        go_to_xy(start_x+width//2, start_y+height//2)
        plant(Entities.Bush)
        use_item(Items.Weird_Substance, width * 2 **
                 (num_unlocked(Unlocks.Mazes) - 1))
        solve_maze()


# solo farming
def solo_farm(farm_func):
    while num_drones() < max_drones():
        spawn_drone(farm_func, 0, 0, full_size, full_size)
        do_a_flip()
    farm_func(0, 0, full_size, full_size)


def till_full_board():
    if get_ground_type() == Grounds.Soil:
        return
    height = get_world_size() / max_drones()

    for i in range(0, max_drones()):
        go_to_xy(0, i * height)
        spawn_drone(move_whole_area_do_action, full_size, height, till)
    move_whole_area_do_action(full_size, height, till)


def farm_hay_to_target(target_hay):
    if target_hay <= num_items(Items.Hay):
        return
    clear()
    # move_whole_area_do_action(full_size, full_size, till)
    while num_items(Items.Hay) < target_hay:
        solo_farm(farm_hay)
        farm_hay(0, 0, full_size, full_size)


def farm_wood_to_target(target_wood):
    if target_wood <= num_items(Items.Wood):
        return
    clear()
    till_full_board()
    while num_items(Items.Wood) < target_wood:
        solo_farm(farm_bush_and_tree)
        farm_bush_and_tree(0, 0, full_size, full_size)


def farm_carrot_to_target(target_carrot):
    if target_carrot <= num_items(Items.Carrot):
        return
    clear()
    till_full_board()
    while num_items(Items.Carrot) < target_carrot:
        solo_farm(farm_carrot)
        farm_carrot(0, 0, full_size, full_size)


def farm_pumpkin_to_target(target_pumpkin):
    if target_pumpkin <= num_items(Items.Pumpkin):
        return
    clear()
    till_full_board()
    while num_items(Items.Pumpkin) < target_pumpkin:
        solo_farm(farm_pumpkin)
        farm_pumpkin(0, 0, full_size, full_size)


def farm_cactus_to_target(target_catus):
    if target_catus <= num_items(Items.Cactus):
        return
    clear()
    till_full_board()
    while num_items(Items.Cactus) < target_catus:
        solo_farm(farm_cactus)
        farm_cactus(0, 0, full_size, full_size)


def refill_power():
    if num_items(Items.Power) >= min_energy:
        return
    target_power = min_energy - num_items(Items.Power)
    needed_carrot = carrot_needed_more_for_sunflower(target_power)
    needed_wood = wood_needed_more_for_target_carrot(needed_carrot)
    needed_hay = hay_needed_more_for_target_carrot(needed_carrot)
    quick_print("Refilling power, needed carrot: " + str(needed_carrot) +
                ", needed wood: " + str(needed_wood) + ", needed hay: " + str(needed_hay))

    farm_hay_to_target(needed_hay)
    farm_wood_to_target(needed_wood)
    farm_carrot_to_target(needed_carrot)
    clear()
    till_full_board()
    solo_farm(farm_sunflower)


# till_full_board()
# while True:
#    continue
if SOLO_FARMING:
    refill_power()
    farm_hay_to_target(target_hay)
    refill_power()
    farm_wood_to_target(target_wood)
    refill_power()
    farm_carrot_to_target(target_carrot)
    refill_power()
    farm_pumpkin_to_target(target_pumpkin)
    refill_power()
    farm_cactus_to_target(target_catus)


spawn_drone(farm_sunflower, 0, 0, half_size, hexa_size)
spawn_drone(farm_carrot, half_size, 0, half_size, hexa_size)
spawn_drone(farm_bush_and_tree, 0, hexa_size, full_size, hexa_size)
spawn_drone(farm_bush_and_tree, 0, octa_size, full_size, hexa_size)
# spawn_drone(farm_bush_and_tree, 0, hexa_size, full_size, octa_size)
spawn_drone(farm_pumpkin, 0, hexa_size + octa_size,
            quad_size+1, quad_size)
spawn_drone(farm_cactus, quad_size+1, hexa_size +
            octa_size, quad_size+1, quad_size)
spawn_drone(farm_maze, 0, half_size-hexa_size,
            half_size+hexa_size, half_size+hexa_size)


apple_farm_width = half_size-hexa_size
apple_farm_height = half_size+quad_size+hexa_size
apple_farm_size = apple_farm_width * apple_farm_height
apple_pos = None

spawn_drone(farm_hay, half_size+hexa_size, octa_size +
            hexa_size, apple_farm_width, apple_farm_height)


def apple_pos_in_apple_farm(apple_pos):
    if apple_pos == None:
        return False
    x, y = apple_pos
    return x >= half_size+hexa_size and y >= octa_size+hexa_size


def become_dino():
    change_hat(Hats.Gray_Hat)
    change_hat(Hats.Dinosaur_Hat)


def goto_apple():
    global apple_pos
    if not apple_pos_in_apple_farm(apple_pos):
        apple_pos = None
        return False
    x, y = apple_pos
    if not go_to_xy(x, y):
        apple_pos = None
        return False
    return True


def farm_apple():
    while True:
        if can_harvest():
            harvest()
        global apple_pos
        if apple_pos == None:
            become_dino()
            apple_pos = measure()
            if not goto_apple():
                return

        if get_entity_type() == Entities.Apple:
            apple_pos = measure()
            if not goto_apple():
                return


def spawn_more_mazers():
    for i in range(max_drones()-num_drones()-1):
        spawn_drone(loop_solve_maze, 0, half_size-hexa_size,
                    half_size+hexa_size, half_size+hexa_size)


spawn_more_mazers()
go_to_xy(half_size+hexa_size, octa_size+hexa_size)

while True:
    spawn_more_mazers()
    farm_apple()
    # move_whole_area_do_action(
    #    apple_farm_width, apple_farm_height, farm_apple)


# move_whole_area_do_action(
#    apple_farm_width, apple_farm_height, farm_apple)
