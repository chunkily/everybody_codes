from collections import defaultdict

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


def main():
    walls = set()
    current_position = (0, 0)
    current_direction = NORTH
    with open("quest15/data/input2.txt", "r") as file:
        instructions = file.read().strip().split(",")

        for instruction in instructions:
            turn_direction = instruction[0]
            length = int(instruction[1:])

            current_direction = turn(current_direction, turn_direction)
            current_position = wall_up(
                walls, current_position, current_direction, length
            )
    walls.remove(current_position)

    ans = path_find(walls, (0, 0), current_position)
    print(f"shortest path length: {len(ans) - 1}")


def visualize_walls(walls):
    if not walls:
        print("No walls to display.")
        return

    min_x = min(x for x, y in walls)
    max_x = max(x for x, y in walls)
    min_y = min(y for x, y in walls)
    max_y = max(y for x, y in walls)

    for y in range(max_y, min_y - 1, -1):
        row = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in walls:
                row += "#"
            else:
                row += "."
        print(row)


def turn(current_direction, turn_direction):
    if turn_direction == "L":
        return (current_direction - 1) % 4
    elif turn_direction == "R":
        return (current_direction + 1) % 4
    else:
        raise ValueError("Invalid turn direction. Use 'L' or 'R'.")


def wall_up(walls, position, direction, length):
    x, y = position

    for i in range(length):
        if direction == NORTH:
            y += 1
        elif direction == EAST:
            x += 1
        elif direction == SOUTH:
            y -= 1
        elif direction == WEST:
            x -= 1
        walls.add((x, y))

    return x, y


def reconstruct_path(came_from, current):
    total_path = list()
    total_path.append(current)
    while current in came_from:
        current = came_from[current]
        total_path.insert(0, current)
    return total_path


def path_find(walls, start, goal):
    open_set = set()
    open_set.add(start)

    came_from = dict()

    g_score = defaultdict(lambda: float("inf"))
    g_score[start] = 0

    f_score = defaultdict(lambda: float("inf"))
    f_score[start] = heuristic_cost_estimate(start, goal)

    while open_set:
        current = min(open_set, key=lambda pos: f_score[pos])
        if current == goal:
            return reconstruct_path(came_from, current)

        open_set.remove(current)
        for neighbour in adjacent(current, walls):
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = g_score[neighbour] + heuristic_cost_estimate(
                    neighbour, goal
                )
                if neighbour not in open_set:
                    open_set.add(neighbour)

    raise ValueError("No path found")


def adjacent(pos, walls):
    x, y = pos
    neighbours = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
    for neighbour in neighbours:
        if neighbour not in walls:
            yield neighbour


def heuristic_cost_estimate(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == "__main__":
    main()
