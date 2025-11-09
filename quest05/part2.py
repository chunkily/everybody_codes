def main():
    with open("quest05/data/input2.txt", "r") as file:
        min_quality = None
        max_quality = None
        for line in file.readlines():
            id, number_text = line.split(":")
            numbers = [int(x) for x in number_text.strip().split(",")]

            structure = construct_structure(numbers)
            quality = get_quality(structure)
            # print(f"{id}: {quality}")
            if min_quality is None or quality < min_quality:
                min_quality = quality
            if max_quality is None or quality > max_quality:
                max_quality = quality

        print(
            f"Difference between max and min quality: {max_quality} - {min_quality} = {max_quality - min_quality}"
        )


def construct_structure(numbers):
    fishbone = [(None, numbers.pop(0), None)]

    # Theres a more efficient approach where we store the left hole and right hole
    # positions for each row, but this is simpler to implement for now :))
    for number in numbers:
        unfilled = True
        row = 0
        while unfilled:
            left, center, right = fishbone[row]
            if left is None and number < center:
                fishbone[row] = (number, center, right)
                unfilled = False
            elif right is None and number > center:
                fishbone[row] = (left, center, number)
                unfilled = False
            else:
                row += 1
                if row >= len(fishbone):
                    fishbone.append((None, number, None))
                    unfilled = False
    return fishbone


def get_quality(structure):
    q = ""
    for left, center, right in structure:
        # print(f"{left} - {center} - {right}")
        q = q + str(center)
    # print(f"Quality: {q}")
    return int(q)


if __name__ == "__main__":
    main()
