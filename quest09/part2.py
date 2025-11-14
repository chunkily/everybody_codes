from itertools import combinations, permutations


def main():
    with open("quest09/data/input2.txt", "r") as file:
        sequences = dict()
        for line in file.readlines():
            id, dna = line.strip().split(":")
            sequences[int(id)] = dna

        sum = 0
        for group_of_three in combinations(range(1, len(sequences) + 1), 3):
            for child_id, parent1_id, parent2_id in iter_group(group_of_three):
                seq1 = sequences[child_id]
                seq2 = sequences[parent1_id]
                seq3 = sequences[parent2_id]

                if are_parents(seq1, seq2, seq3):
                    sim13 = similarity_score(seq1, seq3)
                    sim12 = similarity_score(seq1, seq2)
                    sum += sim13 * sim12
                    # print(
                    #     f"{child_id} is child of {parent1_id} and {parent2_id}: {sim13} * {sim12} = {sim13 * sim12}"
                    # )

        print(f"Total degree of similarity: {sum}")


def iter_group(group):
    yield group[0], group[1], group[2]
    yield group[1], group[0], group[2]
    yield group[2], group[0], group[1]


def are_parents(child, parent1, parent2):
    for i in range(len(child)):
        if child[i] != parent1[i] and child[i] != parent2[i]:
            return False
    return True


def similarity_score(seq1, seq2):
    sum = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            sum += 1

    return sum


if __name__ == "__main__":
    main()
