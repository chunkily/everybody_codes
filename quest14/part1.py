def main():
    floor = []
    with open("quest14/data/input1.txt", "r") as file:
        for line in file.readlines():
            row = [c == "#" for c in line.strip()]
            floor.append(row)
    max_row = len(floor)
    max_col = len(floor[0])

    sum_active = 0
    for _ in range(10):
        floor = next_floor(floor, max_row, max_col)
        sum_active += count_active(floor)
        print_floor(floor)

    print("Sum of active cells over 10 iterations:", sum_active)


def count_active(floor):
    return sum(cell for row in floor for cell in row)


def print_floor(floor):
    for row in floor:
        print("".join("#" if cell else "." for cell in row))
    print()


def next_floor(floor, max_row, max_col):
    new_floor = []
    for r in range(max_row):
        new_row = []
        for c in range(max_col):
            new_state = next_state(floor, r, c, max_row, max_col)
            new_row.append(new_state)
        new_floor.append(new_row)
    return new_floor


def next_state(floor, row, col, max_row, max_col):
    current = floor[row][col]

    num_active_diagonal = 0
    if row > 0 and col > 0 and floor[row - 1][col - 1]:
        num_active_diagonal += 1
    if row > 0 and col < max_col - 1 and floor[row - 1][col + 1]:
        num_active_diagonal += 1
    if row < max_row - 1 and col > 0 and floor[row + 1][col - 1]:
        num_active_diagonal += 1
    if row < max_row - 1 and col < max_col - 1 and floor[row + 1][col + 1]:
        num_active_diagonal += 1

    is_odd = num_active_diagonal % 2 == 1

    if current:
        return is_odd
    else:
        return not is_odd


if __name__ == "__main__":
    main()
