DESCEND = "↓"
ASCEND = "↑"


def main():
    openings = dict()
    with open("quest19/data/input1.txt", "r") as file:
        for line in file.readlines():
            distance, height, size = map(int, line.split(","))
            openings[distance] = (height, size)
    max_distance = distance
    path = search(openings, max_distance, 0, 0, [])
    print("".join(path))
    required_ascents = path.count(ASCEND)
    print(f"Required wing flaps: {required_ascents}")


def can_pass(current, height, size):
    return current >= height and current < (height + size)


def search(openings, max_distance, position, current_height, path):
    if position > max_distance:
        return path
    if position in openings:
        height, size = openings[position]
        if not can_pass(current_height, height, size):
            return False

    can_descend_here = search(
        openings, max_distance, position + 1, current_height - 1, path + [DESCEND]
    )
    if can_descend_here:
        return can_descend_here
    return search(
        openings, max_distance, position + 1, current_height + 1, path + [ASCEND]
    )


if __name__ == "__main__":
    main()
