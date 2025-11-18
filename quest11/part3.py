def main():
    with open("quest11/data/input3.txt", "r") as file:
        lines = file.readlines()
        flock = [int(line.strip()) for line in lines]
        # print(slow_solution(flock))
        print(fast_solution(flock))


def fast_solution(flock):
    flock = flock.copy()
    # if flock is not sorted, abort
    is_sorted = all(flock[i] <= flock[i + 1] for i in range(len(flock) - 1))
    if not is_sorted:
        raise ValueError("Flock must be sorted for fast solution")

    return fast_phase2_solution(flock)


def fast_phase2_solution(flock):
    n = len(flock)
    total = sum(flock)
    avg = total // n

    total = 0
    for i in range(n):
        total += abs(flock[i] - avg)

    return total // 2


def slow_solution(flock):
    flock = flock.copy()
    phase_one_round_num = 0
    while phase_one(flock):
        phase_one_round_num += 1
    print("Phase one:", phase_one_round_num, flock)
    phase_two_round_num = 0
    while phase_two(flock):
        phase_two_round_num += 1
    print("Phase two:", phase_two_round_num, flock)
    return phase_one_round_num + phase_two_round_num


def phase_one(flock):
    has_changed = False
    for i in range(len(flock) - 1):
        left = flock[i]
        right = flock[i + 1]
        if left > right:
            has_changed = True
            flock[i] -= 1
            flock[i + 1] += 1
    return has_changed


def phase_two(flock):
    has_changed = False
    for i in range(len(flock) - 1):
        left = flock[i]
        right = flock[i + 1]
        if left < right:
            has_changed = True
            flock[i] += 1
            flock[i + 1] -= 1
    return has_changed


if __name__ == "__main__":
    main()
