def main():
    # r ->
    # q \
    triangles = dict()
    with open("quest20/data/input1.txt", "r") as file:
        for q, line in enumerate(file.readlines()):
            for r, char in enumerate(line.strip()):
                if char in ("T", "#"):
                    triangles[(q, r)] = char == "T"
                    symbol = "▲" if is_upward(q, r) else "▼"
                    print(f"{symbol} {char} {q} {r}", end=" ")
            print()

    pairs = set()
    for (q, r), is_trampoline in triangles.items():
        if is_trampoline:
            neighbours = get_edge_neighbors(q, r)
            for neighbour in neighbours:
                if triangles.get(neighbour, False):
                    pair = tuple(sorted([(q, r), neighbour]))
                    pairs.add(pair)

    print(f"Number of pairs of adjacent trampolines: {len(pairs)}")


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


if __name__ == "__main__":
    main()
