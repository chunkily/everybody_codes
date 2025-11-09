def main():
    with open("quest05/data/input3.txt", "r") as file:
        sorted_swords = []
        for line in file.readlines():
            id_text, number_text = line.split(":")
            id = int(id_text)
            numbers = [int(x) for x in number_text.strip().split(",")]

            structure = construct_structure(numbers)
            insert_in_order(sorted_swords, id, structure)

        checksum = 0
        for i, sword in enumerate(sorted_swords):
            pos = i + 1
            id, structure = sword
            # print(f"{pos}: {id}")
            checksum += pos * int(id)

        print(f"Checksum: {checksum}")


def insert_in_order(sorted_list, new_id, new_structure):
    """Inserts a new_structure into the sorted_list maintaining order."""
    if not sorted_list:
        sorted_list.append((new_id, new_structure))
        return

    new_sword = (new_id, new_structure)
    for index, sword in enumerate(sorted_list):
        comparison = compare_swords(new_sword, sword)
        if comparison > 0:
            sorted_list.insert(index, new_sword)
            return

    sorted_list.append(new_sword)


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
        q = q + str(center)
    return int(q)


def get_quality_of_level(row):
    q = ""
    left, center, right = row
    if left is not None:
        q += str(left)
    q += str(center)
    if right is not None:
        q += str(right)
    return int(q)


def compare_swords(sword1, sword2):
    """Compares two sword qualities

    Returns:
        negative value if sword1 < sword2
        positive value if sword1 > sword2
    """
    id1, structure1 = sword1
    id2, structure2 = sword2

    q1 = get_quality(structure1)
    q2 = get_quality(structure2)
    if q1 < q2:
        return -1
    elif q1 > q2:
        return 1

    for level in range(min(len(structure1), len(structure2))):
        q1 = get_quality_of_level(structure1[level])
        q2 = get_quality_of_level(structure2[level])
        if q1 < q2:
            return -1
        elif q1 > q2:
            return 1

    if id1 < id2:
        return -1
    elif id1 > id2:
        return 1

    raise ValueError("Two identical swords encountered!")


if __name__ == "__main__":
    main()
