def main():
    with open("quest10/data/input2.txt", "r") as file:
        lines = file.readlines()

        dragon_pos = set()
        sheep_pos = set()
        hideouts = set()

        r_max = len(lines)
        c_max = len(lines[0].strip())

        for c in range(c_max):
            for r in range(r_max):
                char = lines[r][c]

                if char == "D":
                    dragon_pos.add((r, c))
                elif char == "S":
                    sheep_pos.add((r, c))
                elif char == "#":
                    hideouts.add((r, c))

    eaten_count = 0
    for turn in range(20):
        dragon_pos = generate_next_dragon(dragon_pos, r_max, c_max)
        in_range = dragon_pos - hideouts

        eaten_sheep = sheep_pos & in_range
        eaten_count += len(eaten_sheep)
        sheep_pos -= eaten_sheep

        sheep_pos = generate_next_sheep(sheep_pos, r_max, c_max)

        eaten_sheep = sheep_pos & in_range
        eaten_count += len(eaten_sheep)
        sheep_pos -= eaten_sheep

    print(f"Total eaten sheep: {eaten_count}")


def generate_next_dragon(current, r_max, c_max):
    next = set()
    for pos in current:
        for new_pos in generate_moves(pos, r_max, c_max):
            next.add(new_pos)
    return next


def generate_next_sheep(current, r_max, c_max):
    next = set()
    for r, c in current:
        if r < r_max - 1:
            next.add((r + 1, c))
    return next


def generate_moves(pos, r_max, c_max):
    r, c = pos
    if r - 2 >= 0 and c - 1 >= 0:
        yield (r - 2, c - 1)
    if r - 2 >= 0 and c + 1 < c_max:
        yield (r - 2, c + 1)
    if r - 1 >= 0 and c - 2 >= 0:
        yield (r - 1, c - 2)
    if r - 1 >= 0 and c + 2 < c_max:
        yield (r - 1, c + 2)
    if r + 1 < r_max and c - 2 >= 0:
        yield (r + 1, c - 2)
    if r + 1 < r_max and c + 2 < c_max:
        yield (r + 1, c + 2)
    if r + 2 < r_max and c - 1 >= 0:
        yield (r + 2, c - 1)
    if r + 2 < r_max and c + 1 < c_max:
        yield (r + 2, c + 1)


if __name__ == "__main__":
    main()
