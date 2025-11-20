def main():
    number_ranges = []
    with open("quest13/data/input2.txt", "r") as file:
        for line in file.readlines():
            start, end = line.split("-")
            number_ranges.append(range(int(start), int(end) + 1))

    dial = [1]
    right = True
    top_idx = 0
    for number_range in number_ranges:
        if right:
            dial.extend(number_range)
        else:
            for number in number_range:
                dial.insert(0, number)
            top_idx += len(number_range)
        right = not right

    answer_idx = (top_idx + 20252025) % len(dial)
    print(dial[answer_idx])


if __name__ == "__main__":
    main()
