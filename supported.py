"""Dummy drone module for local testing."""


def clear():
    return None


def move(direction):
    return None


def tile():
    return None


def plant(id):
    return None


def harvest():
    return None


def abs(num):
    return None


def can_harvest():
    return None


def can_move():
    return None


def change_hat(hat):
    return None


def do_a_flip():
    return None


def get_companion():
    return None


def get_entity_type():
    return None


def get_ground_type():
    return None


def get_pos_x():
    return None


def get_pos_y():
    return None


def get_tick_count():
    return None


def get_time():
    return None


def get_water():
    return None


def get_world_size():
    return None


def has_finished():
    return None


def len(obj):
    return None


def list(obj):
    return None


def max(obj):
    return None


def max_drones():
    return None


def measure():
    return None


def min(obj):
    return None


def num_drones():
    return None


def num_items():
    return None


def num_unlocked():
    return None


def pet_the_piggy():
    return None


def print(obj):
    return None


def quick_print(obj):
    return None


def random():
    return None


def range(start, stop=None, step=None):
    return None


def set_execution_speed(speed):
    return None


def set_world_size(size):
    return None


def spawn_drone(x, *y):
    return None


def str(obj):
    return None


def swap(a, b):
    return None


def tap(x, y):
    return None


def till(x, y):
    return None


def use_item(id):
    return None


def wait_for(condition):
    return None


East = "right"
West = "left"
North = "up"
South = "down"


class Entities:
    Apple = "Apple"
    Bush = "Bush"
    Cactus = "Cactus"
    Carrot = "Carrot"
    Dead_Pumpkin = "Dead_Pumpkin"
    Dinosaur = "Dinosaur"
    Grass = "Grass"
    Hedge = "Hedge"
    Pumpkin = "Pumpkin"
    Sunflower = "Sunflower"
    Treasure = "Treasure"
    Tree = "Tree"


class Items:
    Hay = "Hay"
    Wood = "Wood"
    Carrot = "Carrot"
    Pumpkin = "Pumpkin"
    Cactus = "Cactus"
    Bone = "Bone"
    Weird_Substance = "Weird_Substance"
    Gold = "Gold"
    Water = "Water"
    Fertilizer = "Fertilizer"
    Power = "Power"


class Unlocks:
    Cactus = "Cactus"
    Carrots = "Carrots"
    Debug = "Debug"
    Debug_2 = "Debug_2"
    Dinosaurs = "Dinosaurs"
    Expand = "Expand"
    Expand_2 = "Expand_2"
    Fertilizer = "Fertilizer"
    Functions = "Functions"
    Grass = "Grass"
    Hats = "Hats"
    Lists = "Lists"
    Loops = "Loops"
    Mazes = "Mazes"
    Megafarm = "Megafarm"
    Operators = "Operators"
    Plant = "Plant"
    Polyculture = "Polyculture"
    Pumpkins = "Pumpkins"
    Senses = "Senses"
    Speed = "Speed"
    Sunflowers = "Sunflowers"
    Timing = "Timing"
    Trees = "Trees"
    Utilities = "Utilities"
    Variables = "Variables"
    Watering = "Watering"


class Hats:
    Gray_Hat = "Gray_Hat"
    Purple_Hat = "Purple_Hat"
    Green_Hat = "Green_Hat"
    Brown_Hat = "Brown_Hat"
    Dinosaur_Hat = "Dinosaur_Hat"


class Grounds:
    Soil = "Soil"
    Sand = "Sand"
    Grass = "Grass"
    Stone = "Stone"
    Water = "Water"
