NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


def main():
    walls = set()
    current_position = (0, 0)
    current_direction = NORTH
    with open("quest15/data/input1.txt", "r") as file:
        instructions = file.read().strip().split(",")

        for instruction in instructions:
            turn_direction = instruction[0]
            length = int(instruction[1:])

            current_direction = turn(current_direction, turn_direction)
            current_position = wall_up(
                walls, current_position, current_direction, length
            )

    visualize_walls(walls)

    ans = shortest_path(walls, (0, 0), current_position)
    print(f"shortest path length: {ans}")


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


def shortest_path(walls, start, end):
    # Using floodfill method to get the length of shortest path from start to end.
    path_length = 0

    visited = set()
    frontier = set()
    frontier.add(start)
    while frontier:
        path_length += 1
        next = set()
        for x, y in frontier:
            neighbours = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
            for neighbour in neighbours:
                if neighbour == end:
                    return path_length
                if (
                    neighbour not in next
                    and neighbour not in visited
                    and neighbour not in walls
                ):
                    next.add(neighbour)
        frontier = next


if __name__ == "__main__":
    main()
