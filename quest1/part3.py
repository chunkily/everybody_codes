def main():
    with open("quest1/data/input3.txt", "r") as file:
        names = file.readline().strip().split(",")
        file.readline()
        instructions = file.readline().strip().split(",")

        print(names, len(names))
        print(instructions)

        num_names = len(names)
        for instruction in instructions:
            is_right, number = parse_instruction(instruction)

            if is_right:
                next_pos = (+number) % num_names
            else:
                next_pos = (-number) % num_names

            temp = names[next_pos]
            names[next_pos] = names[0]
            names[0] = temp

        print("Name at top position:", names[0])


def parse_instruction(instruction):
    letter = instruction[0]
    number = int(instruction[1:])

    return letter == "R", number


if __name__ == "__main__":
    main()
