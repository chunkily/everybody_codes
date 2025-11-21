def main():
    pattern = []
    with open("quest14/data/input3.txt", "r") as file:
        for line in file.readlines():
            row = [c == "#" for c in line.strip()]
            pattern.append(row)
    pattern_size = len(pattern)
    if len(pattern[0]) != pattern_size:
        raise ValueError("Pattern must be square")

    max_row = 34
    max_col = 34

    # Pattern should match in the center
    pattern_idx = (max_row - pattern_size) // 2

    floor = [[False for _ in range(max_col)] for _ in range(max_row)]

    # Assume pattern is symmetric, only need to match a quarter
    match_size = pattern_size // 2
    first_match_key = None
    matches = []
    for i in range(1_000_000_000):
        floor = next_floor(floor, max_row, max_col)
        if match_pattern(floor, pattern, pattern_idx, match_size):
            # print_floor(floor)
            print(f"Pattern matched at iteration {i + 1}")
            matches.append((i + 1, count_active(floor)))
            state_key_str = state_key(floor)
            if first_match_key is None:
                first_match_key = state_key_str
            elif state_key_str == first_match_key:
                print("Pattern repetition detected, stopping search.")
                break

    get_answer(matches)


def count_active(floor):
    return sum(cell for row in floor for cell in row)


def get_answer(matches):
    total_iterations = 1_000_000_000
    # total_iterations = 10_000
    cycle_diffs = []
    active_counts = []
    for i in range(0, len(matches) - 1):
        cycle_diff = matches[i + 1][0] - matches[i][0]
        cycle_diffs.append(cycle_diff)
        active_counts.append(matches[i + 1][1])

    cycle_idx = 0
    answer = matches[0][1]
    current = matches[0][0]
    # print(f"Cycle {current}: +{answer}")
    while current + cycle_diffs[cycle_idx] < total_iterations:
        answer += active_counts[cycle_idx]
        current += cycle_diffs[cycle_idx]
        # print(f"Cycle {current}: +{active_counts[cycle_idx]}")
        cycle_idx = (cycle_idx + 1) % len(cycle_diffs)

    print("Answer:", answer)


def match_pattern(floor, pattern, pattern_idx, match_size):
    for r in range(match_size):
        for c in range(match_size):
            floor_r = pattern_idx + r
            floor_c = pattern_idx + c
            if floor[floor_r][floor_c] != pattern[r][c]:
                return False
    return True


def print_floor(floor):
    for row in floor:
        print("".join("#" if cell else "." for cell in row))
    print()


def state_key(floor):
    return "".join("".join("1" if cell else "0" for cell in row) for row in floor)


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
