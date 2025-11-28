from math import lcm


def main():
    with open("quest16/data/input3.txt", "r") as file:
        text = file.read()
        wall = [int(num) for num in text.split(",")]
        wall.insert(0, 0)

    wall_size = len(wall) - 1
    pattern = search(wall, 1, wall_size, tuple(), set())

    target = 202520252025000
    lo = 1
    hi = target

    while lo < hi:
        mid = (lo + hi) // 2
        blocks = number_of_blocks(pattern, mid)
        if blocks < target:
            lo = mid + 1
        else:
            hi = mid

    answer = lo
    if number_of_blocks(pattern, lo) > target:
        answer -= 1

    print(
        f"answer: {answer} number_of_blocks: {number_of_blocks(pattern, answer)} pattern: {pattern}"
    )


def search(wall, current, wall_size, partial, visited):
    if current == wall_size:
        return None
    partial = (*partial, current)
    if partial not in visited:
        visited.add(partial)
    else:
        return None

    wall_copy = wall.copy()

    for i in range(1, wall_size + 1):
        n = wall_copy[i]

        if i % current == 0:
            if n == 0:
                # current is not valid
                return None
            wall_copy[i] = n - 1

    if is_all_zeros(wall_copy):
        return partial

    for i in range(current + 1, wall_size):
        answer = search(wall_copy, i, wall_size, partial, visited)
        if answer is not None:
            return answer

    return None


def is_all_zeros(wall):
    for n in wall:
        if n != 0:
            return False
    return True


def number_of_blocks(pattern, wall_length):
    total = 0
    for p in pattern:
        total += wall_length // p
    return total


if __name__ == "__main__":
    main()
