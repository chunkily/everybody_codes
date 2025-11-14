from itertools import combinations, permutations


def main():
    with open("quest09/data/input3.txt", "r") as file:
        sequences = dict()
        for line in file.readlines():
            id, dna = line.strip().split(":")
            sequences[int(id)] = dna

        branches = list()
        for group_of_three in combinations(range(1, len(sequences) + 1), 3):
            for child_id, parent1_id, parent2_id in iter_group(group_of_three):
                seq1 = sequences[child_id]
                seq2 = sequences[parent1_id]
                seq3 = sequences[parent2_id]

                if are_parents(seq1, seq2, seq3):
                    branches.append((child_id, parent1_id, parent2_id))
                    # print(f"{child_id} is child of {parent1_id} and {parent2_id}")

        largest_scale_sum = 0
        unvisited = set(sequences.keys())
        while unvisited:
            next = unvisited.pop()
            frontier = set()
            frontier.add(next)
            family = set()
            family.add(next)

            while frontier:
                current = frontier.pop()
                for child, parent1, parent2 in branches:
                    if parent1 == current or parent2 == current:
                        if child not in family:
                            family.add(child)
                            frontier.add(child)
                    elif child == current:
                        if parent1 not in family:
                            family.add(parent1)
                            frontier.add(parent1)
                        if parent2 not in family:
                            family.add(parent2)
                            frontier.add(parent2)
            print(f"Found family of size {sum(family)}: {family}")

            largest_scale_sum = max(largest_scale_sum, sum(family))
            unvisited.difference_update(family)

        print(f"Largest family tree: {largest_scale_sum}")


def iter_group(group):
    yield group[0], group[1], group[2]
    yield group[1], group[0], group[2]
    yield group[2], group[0], group[1]


def are_parents(child, parent1, parent2):
    for i in range(len(child)):
        if child[i] != parent1[i] and child[i] != parent2[i]:
            return False
    return True


if __name__ == "__main__":
    main()
