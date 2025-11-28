from collections import defaultdict
from itertools import combinations

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


def main():
    walls = list()
    current_position = (0, 0)
    points_of_interest = set(diagonals(current_position))
    current_direction = NORTH
    with open("quest15/data/input3.txt", "r") as file:
        instructions = file.read().strip().split(",")

        for instruction in instructions:
            turn_direction = instruction[0]
            length = int(instruction[1:])

            points_of_interest.add(
                get_corner_point(current_position, current_direction, turn_direction)
            )

            current_direction = turn(current_direction, turn_direction)
            current_position = wall_up(
                walls, current_position, current_direction, length
            )
        exit_position = current_position
    points_of_interest.update(
        diagonals(exit_position)
    )  # Include diagonals of exit position

    print("Number of points of interest:", len(points_of_interest))
    # 240 points of interest means n * (n-1) / 2 = 28,680 edges
    # distances = dict()
    connections = defaultdict(list)
    distances = dict()
    for point_a, point_b in combinations(points_of_interest, 2):
        if has_simple_path(walls, point_a, point_b):
            dist = manhattan_distance(point_a, point_b)
            distances[(point_a, point_b)] = dist
            distances[(point_b, point_a)] = dist
            connections[point_a].append(point_b)
            connections[point_b].append(point_a)

    for pos in diagonals((0, 0)):
        distances[((0, 0), pos)] = 2
        connections[(0, 0)].append(pos)

    for pos in diagonals(exit_position):
        distances[(pos, exit_position)] = 2
        connections[pos].append(exit_position)

    print("Number of simple connections:", len(distances))

    ans = path_find(distances, connections, (0, 0), exit_position)
    print(f"shortest path length: {ans}")
    # Note that solution may be incorrect in rare case where there is a direct path
    # between the start and end points! In such a case subtract 2 from the final answer.


def turn(current_direction, turn_direction):
    if turn_direction == "L":
        return (current_direction - 1) % 4
    elif turn_direction == "R":
        return (current_direction + 1) % 4
    else:
        raise ValueError("Invalid turn direction. Use 'L' or 'R'.")


# We can assume that the shortest path will go around corners only?
def get_corner_point(position, current_direction, turn_direction):
    x, y = position
    top_left = (x - 1, y + 1)
    top_right = (x + 1, y + 1)
    bottom_left = (x - 1, y - 1)
    bottom_right = (x + 1, y - 1)

    if current_direction == NORTH:
        if turn_direction == "L":
            #   X
            # -+
            #  |
            return top_right
        else:
            # X
            #  +-
            #  |
            return top_left
    elif current_direction == EAST:
        if turn_direction == "L":
            #  |
            # -+
            #   X
            return bottom_right
        else:
            #   X
            # -+
            #  |
            return top_right
    elif current_direction == SOUTH:
        if turn_direction == "L":
            #  |
            #  +-
            # X
            return bottom_left
        else:
            #  |
            # -+
            #   X
            return bottom_right
    elif current_direction == WEST:
        if turn_direction == "L":
            # X
            #  +-
            #  |
            return top_left
        else:
            #  |
            #  +-
            # X
            return bottom_left
    else:
        raise ValueError("Invalid direction")


def wall_up(walls, position, direction, length):
    x, y = position
    if direction == NORTH:
        y += length
    elif direction == EAST:
        x += length
    elif direction == SOUTH:
        y -= length
    elif direction == WEST:
        x -= length

    walls.append((position, (x, y)))

    return x, y


def has_simple_path(walls, point_a, point_b):
    # There is a simple path between point_a and point_b if the rectangle
    # defined by these two points does not intersect any walls. The shortest
    # distance between the two points will be the Manhattan distance.

    point_c = (point_a[0], point_b[1])
    point_d = (point_b[0], point_a[1])

    if wall_intersects(walls, point_a, point_c, point_b):
        return False
    if wall_intersects(walls, point_a, point_d, point_b):
        return False

    return True


def wall_intersects(walls, p1, p2, p3):
    for wall_start, wall_end in walls:
        if lines_intersect(p1, p2, wall_start, wall_end):
            return True
        if lines_intersect(p2, p3, wall_start, wall_end):
            return True
    return False


def orientation(a, b, c):
    val = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2


def lines_intersect(p1, p2, q1, q2):
    o1 = orientation(p1, p2, q1)
    o2 = orientation(p1, p2, q2)
    o3 = orientation(q1, q2, p1)
    o4 = orientation(q1, q2, p2)

    if o1 != o2 and o3 != o4:
        return True

    return False


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def diagonals(pos):
    x, y = pos
    return [
        (x + 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x - 1, y - 1),
    ]


def shortest_path(came_from, current, distances):
    distance = 0
    while current in came_from:
        next = came_from[current]
        distance += distances[next, current]
        current = next
    return distance


def path_find(distances, connections, start, goal):
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
            return shortest_path(came_from, current, distances)

        open_set.remove(current)
        for neighbour in connections[current]:
            tentative_g_score = g_score[current] + distances[(current, neighbour)]
            if tentative_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = g_score[neighbour] + heuristic_cost_estimate(
                    neighbour, goal
                )
                if neighbour not in open_set:
                    open_set.add(neighbour)

    raise ValueError("No path found")


def heuristic_cost_estimate(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == "__main__":
    main()
