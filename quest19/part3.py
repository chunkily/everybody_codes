from collections import defaultdict
import heapq


def main():
    openings = defaultdict(list)
    with open("quest19/data/input3.txt", "r") as file:
        for line in file.readlines():
            distance, height, size = map(int, line.split(","))
            openings[distance].append((height, size))

    # Sort openings at each distance by height for consistency
    for dist in openings:
        openings[dist].sort()

    required_ascents = search(openings)
    print(f"Required wing flaps: {required_ascents}")


def search(openings):
    distances = list(openings.keys())
    heap = [(0, -1, 0)]  # (cost, idx, height)
    best = {}  # (idx, height) -> best cost seen

    target_idx = len(distances) - 1

    while heap:
        cost, idx, height = heapq.heappop(heap)
        key = (idx, height)

        # Skip if we've already found a better path to this state
        if best.get(key, float("inf")) <= cost:
            continue

        best[key] = cost

        next_idx = idx + 1
        if next_idx > target_idx:
            return cost  # Reached the end

        distance = distances[idx] if idx >= 0 else 0
        next_distance = distances[next_idx]

        gap = next_distance - distance
        next_openings = openings[next_distance]

        actions = get_permissible_actions(gap, height, next_openings)

        for ascents, next_height in actions:
            next_cost = cost + ascents
            next_key = (next_idx, next_height)

            if best.get(next_key, float("inf")) <= next_cost:
                continue
            heapq.heappush(heap, (next_cost, next_idx, next_height))
    # No valid path found
    return None


def get_permissible_actions(gap, height, openings_at_idx):
    height_without_flaps = height - gap
    output = list()
    for oh, sz in openings_at_idx:
        min_a = max(0, (oh - height_without_flaps + 1) // 2)
        max_a = min(gap, (oh + sz - 1 - height_without_flaps) // 2)
        if min_a <= max_a:
            for a in range(min_a, max_a + 1):
                output.append((a, height_without_flaps + 2 * a))
    return output


if __name__ == "__main__":
    main()
