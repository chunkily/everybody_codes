def main():
    with open("quest12/data/input1.txt", "r") as file:
        barrels = []
        for line in file.readlines():
            row = []
            for char in line.strip():
                row.append(int(char))
            barrels.append(row)
    max_y = len(barrels)
    max_x = len(barrels[0])

    exploded = set()
    exploded.add((0, 0))
    frontier = [(0, 0)]

    while frontier:
        x, y = frontier.pop()
        for nx, ny in chain(barrels, x, y, max_x, max_y):
            if (nx, ny) not in exploded:
                exploded.add((nx, ny))
                frontier.append((nx, ny))

    print(len(exploded))


def chain(barrels, x, y, max_x, max_y):
    current = barrels[y][x]

    if x > 0 and barrels[y][x - 1] <= current:
        yield x - 1, y
    if x < max_x - 1 and barrels[y][x + 1] <= current:
        yield x + 1, y
    if y > 0 and barrels[y - 1][x] <= current:
        yield x, y - 1
    if y < max_y - 1 and barrels[y + 1][x] <= current:
        yield x, y + 1


if __name__ == "__main__":
    main()
