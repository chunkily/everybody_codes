def main():
    with open("quest09/data/input1.txt", "r") as file:
        sequences = dict()
        for line in file.readlines():
            id, dna = line.strip().split(":")
            sequences[int(id)] = dna

        sim13 = similarity_score(sequences[1], sequences[3])
        sim23 = similarity_score(sequences[2], sequences[3])

        print(f"Degree of similarity: {sim13} * {sim23} = {sim13 * sim23}")


def similarity_score(seq1, seq2):
    sum = 0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            sum += 1

    return sum


if __name__ == "__main__":
    main()
