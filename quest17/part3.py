from collections import defaultdict


def main():
    field = list()
    origin = None
    start = None
    with open("quest17/data/input3.txt", "r") as file:
        for y, line in enumerate(file.readlines()):
            row = list()
            for x, char in enumerate(line.strip()):
                if char == "@":
                    row.append(0)
                    origin = (x, y)
                elif char == "S":
                    row.append(0)
                    start = (x, y)
                else:
                    row.append(int(char))
            field.append(row)
    max_y = len(field)
    max_x = len(field[0])

    for radius in range(1, max(max_x, max_y) // 2):
        time = (radius + 1) * 30
        for y in range(max_y):
            for x in range(max_x):
                if is_destroyed(x, y, origin[0], origin[1], radius):
                    field[y][x] = 0

        print(f"Searching with radius {radius}")
        min_cost = min_enclosing_wall_cost(field, origin, max_x, max_y, start, time)
        if min_cost <= time:
            answer = radius * min_cost
            print(f"answer: {answer} = {radius} * {min_cost}")
            return


def is_destroyed(xc, yc, xv, yv, r):
    return (xv - xc) * (xv - xc) + (yv - yc) * (yv - yc) <= r * r


def min_enclosing_wall_cost(field, origin, max_x, max_y, start, budget):
    # ASSUMPTIONS:
    # 1. lava origin is in the center
    # 2. start point is located in same column, above the origin
    # 3. the path has to go through one of the bottom points
    origin_x, origin_y = origin
    left_points = set()
    right_points = set()
    bottom_points = set()

    for x in range(origin_x, 0, -1):
        p = (x, origin_y)
        if field[p[1]][p[0]] != 0:
            left_points.add(p)
    for x in range(origin_x + 1, max_x):
        p = (x, origin_y)
        if field[p[1]][p[0]] != 0:
            right_points.add(p)
    for y in range(origin_y + 1, max_y):
        p = (origin_x, y)
        if field[p[1]][p[0]] != 0:
            bottom_points.add(p)

    walls = set()
    for x in range(max_x):
        for y in range(max_y):
            if field[y][x] == 0:
                walls.add((x, y))
    walls.remove(start)

    has_loop_under_budget = False
    min_cost = budget

    for bp in bottom_points:
        total_cost = 0

        left_walls = walls | right_points
        p1 = path_find(start, bp, field, max_x, max_y, left_walls)
        total_cost += compute_path_cost(p1, field)
        if total_cost >= min_cost:
            continue

        right_walls = walls | left_points
        p2 = path_find(bp, start, field, max_x, max_y, right_walls)

        # Avoid duplicating cost of connecting node
        total_cost += compute_path_cost(p2[1:], field)

        if total_cost < min_cost:
            print(f"    loop via {bp} with cost {total_cost}")
            # loop_nodes = p1 + p2[1:]
            # visualize(field, loop_nodes)
            min_cost = total_cost
            has_loop_under_budget = True

    if not has_loop_under_budget:
        return float("inf")
    return min_cost


def compute_path_cost(path, field):
    return sum(field[y][x] for (x, y) in path)


def adjacent(xy, max_x, max_y):
    x, y = xy

    if x > 0:
        yield x - 1, y
    if y > 0:
        yield x, y - 1
    if x < max_x - 1:
        yield x + 1, y
    if y < max_y - 1:
        yield x, y + 1


def path_find(start, goal, field, max_x, max_y, walls):
    def heuristic_cost_estimate(a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

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
            # rebuild path: include start .. goal
            total_path = [current]
            while current in came_from:
                current = came_from[current]
                total_path.insert(0, current)
            return total_path

        open_set.remove(current)
        neighbours = [n for n in adjacent(current, max_x, max_y) if n not in walls]
        for neighbour in neighbours:
            tentative_g_score = g_score[current] + field[neighbour[1]][neighbour[0]]
            if tentative_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = g_score[neighbour] + heuristic_cost_estimate(
                    neighbour, goal
                )
                if neighbour not in open_set:
                    open_set.add(neighbour)

    raise ValueError("No path found")


def visualize(field, path=list()):
    path_set = set(path)
    for y, row in enumerate(field):
        line = ""
        for x, val in enumerate(row):
            if (x, y) in path_set:
                line += "_"
            elif val == 0:
                line += "."
            else:
                line += str(val)
        print(line)


if __name__ == "__main__":
    main()
