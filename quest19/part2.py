from collections import defaultdict


def main():
    openings = defaultdict(list)
    with open("quest19/data/input2.txt", "r") as file:
        for line in file.readlines():
            distance, height, size = map(int, line.split(","))
            openings[distance].append((height, size))

    # Sort openings at each distance by height for consistency
    for dist in openings:
        openings[dist].sort()

    max_distance = distance
    # print(openings)
    required_ascents = search(openings, max_distance, 0, 0, 0)
    print(f"Required wing flaps: {required_ascents}")


def can_pass(current, height, size):
    return current >= height and current < (height + size)


def can_pass_through_any(current, openings_at_position):
    for height, size in openings_at_position:
        if can_pass(current, height, size):
            return True
    return False


def search(openings, max_distance, position, current_height, required_ascents):
    next_distance = next_opening_distance(openings, position)
    if next_distance is None:
        return required_ascents  # No more openings

    distance_to_next = next_distance - position
    next_openings = openings[next_distance]

    actions = get_permissible_actions(distance_to_next, current_height, next_openings)
    print(f"position: {position} current_height: {current_height} actions: {actions}")

    for ascents, next_height in actions:
        next = search(
            openings,
            max_distance,
            next_distance,
            next_height,
            required_ascents + ascents,
        )
        if next is not None:
            return next
    return None


def next_opening_distance(openings, position):
    # Dictionary keys are iterated in insertion order (Python 3.7+)
    for dist in openings.keys():
        if dist > position:
            return dist


def get_permissible_actions(distance, current_height, openings_at_position):
    height_without_flaps = current_height - distance
    output = list()
    for ascents in range(distance + 1):
        # each ascent converts a downward move to upward so +2 height
        height_at_opening = height_without_flaps + 2 * ascents
        if can_pass_through_any(height_at_opening, openings_at_position):
            output.append((ascents, height_at_opening))
    return output


if __name__ == "__main__":
    main()
