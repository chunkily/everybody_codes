def main():
    with open("quest05/data/input1.txt", "r") as file:
        text = file.read()

        id, number_text = text.split(":")
        numbers = [int(x) for x in number_text.strip().split(",")]

    fishbone = [(None, numbers.pop(0), None)]

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

    print_structure(fishbone)


def print_structure(structure):
    q = ""
    for left, center, right in structure:
        print(f"{left} - {center} - {right}")
        q = q + str(center)
    print(f"Quality: {q}")


if __name__ == "__main__":
    main()
