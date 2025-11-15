def main():
    with open("quest10/data/input1.txt", "r") as file:
        lines = file.readlines()

        dragon_pos = None
        sheep_pos = set()

        r_max = len(lines)
        c_max = len(lines[0].strip())

        for c in range(c_max):
            for r in range(r_max):
                char = lines[r][c]

                if char == "D":
                    dragon_pos = (r, c)
                elif char == "S":
                    sheep_pos.add((r, c))

        in_range = set()
        in_range.add(dragon_pos)
        next_range = set()
        next_range.add(dragon_pos)
        for _ in range(4):
            current_range = next_range
            next_range = set()
            for pos in current_range:
                for new_pos in generate_moves(pos, r_max, c_max):
                    if new_pos not in in_range:
                        in_range.add(new_pos)
                        next_range.add(new_pos)

        caught_sheep = sheep_pos.intersection(in_range)
        print(f"Dragon can catch {len(caught_sheep)} sheep in 4 moves.")


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
