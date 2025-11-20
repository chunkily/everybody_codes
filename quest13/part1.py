def main():
    with open("quest13/data/input1.txt", "r") as file:
        numbers = [int(line.strip()) for line in file.readlines()]

    dial = [1]
    right = True
    top_idx = 0
    for number in numbers:
        if right:
            dial.append(number)
        else:
            dial.insert(0, number)
            top_idx += 1
        right = not right

    answer_idx = (top_idx + 2025) % len(dial)
    print(dial[answer_idx])


if __name__ == "__main__":
    main()
