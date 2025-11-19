def main():
    exploded = set()
    unexploded = set()
    with open("quest12/data/input3.txt", "r") as file:
        barrels = []
        for i, line in enumerate(file.readlines()):
            row = []
            for j, char in enumerate(line.strip()):
                row.append(int(char))
                unexploded.add((j, i))
            barrels.append(row)
    max_y = len(barrels)
    max_x = len(barrels[0])

    for i in range(3):
        best_exploded = set()
        best_exploded_count = 0
        best_position = None

        for position in unexploded:
            test_exploded = calculate_explosions(barrels, max_x, max_y, position)
            if len(test_exploded) > best_exploded_count:
                best_exploded_count = len(test_exploded)
                best_exploded = test_exploded
                best_position = position
        print(
            f"#{i+1} fireball at {best_position} with size {barrels[best_position[1]][best_position[0]]} explodes {best_exploded_count} barrels"
        )
        exploded |= best_exploded
        unexploded -= best_exploded
        for x, y in best_exploded:
            barrels[y][x] = 0

    print(len(exploded))


def chain(barrels, x, y, max_x, max_y):
    current = barrels[y][x]

    if x > 0 and barrels[y][x - 1] <= current and barrels[y][x - 1] > 0:
        yield x - 1, y
    if x < max_x - 1 and barrels[y][x + 1] <= current and barrels[y][x + 1] > 0:
        yield x + 1, y
    if y > 0 and barrels[y - 1][x] <= current and barrels[y - 1][x] > 0:
        yield x, y - 1
    if y < max_y - 1 and barrels[y + 1][x] <= current and barrels[y + 1][x] > 0:
        yield x, y + 1


def calculate_explosions(barrels, max_x, max_y, initial):
    exploded = set()
    exploded.add(initial)
    frontier = [initial]

    # print(f"Testing from {initial}")
    while frontier:
        x, y = frontier.pop()
        for nx, ny in chain(barrels, x, y, max_x, max_y):
            if (nx, ny) not in exploded:
                exploded.add((nx, ny))
                frontier.append((nx, ny))
    # print(f"  Exploded {len(exploded)} barrels")

    return exploded


if __name__ == "__main__":
    main()
