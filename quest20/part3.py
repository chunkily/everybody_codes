from collections import deque


def main():
    # r ->
    # q \
    triangles = dict()
    start = None
    end = None

    with open("quest20/data/input3.txt", "r") as file:
        for q, line in enumerate(file.readlines()):
            for r, char in enumerate(line.strip()):
                if char != ".":
                    triangles[(q, r)] = char
                    if char == "S":
                        start = (q, r)
                    elif char == "E":
                        end = (q, r)

    rotating_map = dict()
    rotating_map[0] = triangles

    max_r = max(r for (q, r) in triangles.keys())

    # visualize_path(triangles)

    # Generate all 3 rotations
    ends = [end]
    for i in range(2):
        new_triangles = dict()
        for (q, r), char in triangles.items():
            new_coordinates = rotate_clockwise(q, r, max_r)
            new_triangles[new_coordinates] = char
            if char == "E":
                ends.append(new_coordinates)
        triangles = new_triangles
        rotating_map[i + 1] = triangles
        # visualize_path(triangles)

    path = path_find(start, ends, rotating_map)
    if path is None:
        print("No path found.")
    else:
        print(f"Path found with {len(path)-1} moves:")
        # for rotation, coord in path:
        #     visualize_path(rotating_map[rotation], [coord])


def rotate_clockwise(q, r, max_r):
    """
    Rotates the coordinates of the triangle at (q, r) clockwise 120 degrees.
    """
    q2 = (r - q) // 2
    r2 = max_r - r + q2 - q
    return (q2, r2)


def is_upward(q, r):
    return (q + r) % 2 == 1


def get_edge_neighbors(q, r):
    """Returns the 3 triangles that share an edge."""
    if is_upward(q, r):
        top_left = (q, r - 1)
        top_right = (q, r + 1)
        bottom = (q + 1, r)
        return [top_left, top_right, bottom]
    else:
        bottom_left = (q, r - 1)
        bottom_right = (q, r + 1)
        top = (q - 1, r)
        return [bottom_left, bottom_right, top]


def path_find(start, ends, rotating_map):
    """Finds a path from start to end using BFS."""
    initial = (0, start)

    queue = deque([initial])
    visited = set()
    visited.add(initial)
    parent = {initial: None}

    while queue:
        rotation, current = queue.popleft()
        if current == ends[rotation]:
            # Reconstruct path
            path = []
            step = (rotation, current)
            while step is not None:
                path.append(step)
                step = parent.get(step)
            path.reverse()

            return path

        next_rotation = (rotation + 1) % 3  # Rotate for next move
        triangles = rotating_map[next_rotation]

        neighbours = []
        for adjacent_coord in get_edge_neighbors(*current):
            if triangles.get(adjacent_coord, "#") != "#":
                neighbours.append((next_rotation, adjacent_coord))
        if triangles.get(current, "#") != "#":
            neighbours.append((next_rotation, current))  # Allow staying in place

        for neighbour in neighbours:
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = (rotation, current)
                queue.append(neighbour)

    return


def visualize_path(triangles, path=None):
    min_q = min(q for (q, r) in triangles.keys())
    max_q = max(q for (q, r) in triangles.keys())
    min_r = min(r for (q, r) in triangles.keys())
    max_r = max(r for (q, r) in triangles.keys())

    path_set = set(path) if path is not None else set()

    for q in range(min_q, max_q + 1):
        line = ""
        for r in range(min_r, max_r + 1):
            if (q, r) in path_set:
                line += "*"
            elif (q, r) in triangles:
                line += triangles[(q, r)]
            else:
                line += "."
        print(line)


if __name__ == "__main__":
    main()
