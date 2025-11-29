from collections import deque


def main():
    # r ->
    # q \
    triangles = dict()
    start = None
    end = None

    with open("quest20/data/input2.txt", "r") as file:
        for q, line in enumerate(file.readlines()):
            for r, char in enumerate(line.strip()):
                if char != ".":
                    triangles[(q, r)] = char
                    if char == "S":
                        start = (q, r)
                    elif char == "E":
                        end = (q, r)

    # print(start, end)
    path = path_find(start, end, triangles)
    if path is None:
        print("No path found from S to E.")
        return

    # visualize_path(triangles, path)

    print(f"Path from S to E takes {len(path) - 1} steps")


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


def path_find(start, end, triangles):
    """Finds a path from start to end using BFS."""

    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}

    while queue:
        # print("Queue size:", len(queue))
        # if len(queue) > 1000:
        #     print("Too many nodes to explore, aborting.")
        #     return None
        current = queue.popleft()
        if current == end:
            break

        for neighbor in get_edge_neighbors(*current):
            if triangles.get(neighbor, "#") != "#" and neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    # Reconstruct path
    path = []
    step = end
    while step is not None:
        path.append(step)
        step = parent.get(step)
    path.reverse()

    return path if path[0] == start else None


def visualize_path(triangles, path):
    min_q = min(q for (q, r) in triangles.keys())
    max_q = max(q for (q, r) in triangles.keys())
    min_r = min(r for (q, r) in triangles.keys())
    max_r = max(r for (q, r) in triangles.keys())

    path_set = set(path)

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
