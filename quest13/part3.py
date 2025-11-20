def main():
    number_ranges = []
    with open("quest13/data/input3.txt", "r") as file:
        for line in file.readlines():
            start, end = map(int, (x for x in line.split("-")))
            number_ranges.append((start, end - start + 1))

    dial = [(1, 1, True)]
    dial_left = []
    right = True
    dial_length = 1
    for start, length in number_ranges:
        if right:
            dial.append((start, length, right))
            dial_length += length
        else:
            dial_left.insert(0, (start, length, right))
            dial_length += length
        right = not right
    dial = dial + dial_left

    get_answer(dial, dial_length)


def get_answer(dial, dial_length):
    offset = 202520252025 % dial_length
    target_start = 1
    target_length = 1
    target_right = True
    target_idx = 0
    while offset >= target_length:
        offset -= target_length
        target_idx += 1
        target_start, target_length, target_right = dial[target_idx]

    if target_right:
        answer = target_start + offset
    else:
        answer = target_start + target_length - offset - 1
    print(answer)


if __name__ == "__main__":
    main()
