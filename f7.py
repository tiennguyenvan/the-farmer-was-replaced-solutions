import f0


def farm_maze():
    def spawn_maze_solver():
        if num_drones() < max_drones()-1:
            spawn_drone(solve_maze, True)

    def solve_maze(repeat=True):
        while True:
            if measure() == None and repeat:
                continue
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
            if not repeat:
                break

    f0.go_to(f0.HALF_SIZE, f0.HALF_SIZE, spawn_maze_solver)
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, f0.FULL_SIZE * 2 **
             (num_unlocked(Unlocks.Mazes) - 1))
    solve_maze(False)


if __name__ == "__main__":
    while True:
        farm_maze()
