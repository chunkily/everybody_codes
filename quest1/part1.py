def main():
    with open("quest1/data/input1.txt", "r") as file:
        names = file.readline().strip().split(",")
        file.readline()
        instructions = file.readline().strip().split(",")

        print(names)
        print(instructions)

        pos = 0
        num_names = len(names)
        for instruction in instructions:
            is_right, number = parse_instruction(instruction)

            if is_right:
                next_pos = pos + number
                if next_pos >= num_names:
                    next_pos = num_names - 1
                print(f"Moved right {number} from {pos} to position {next_pos}")
            else:
                next_pos = pos - number

                if next_pos < 0:
                    next_pos = 0
                print(f"Moved left {number} from {pos} to position {next_pos}")
            pos = next_pos

        print("Final position:", pos)
        print("Name at final position:", names[pos])


def parse_instruction(instruction):
    letter = instruction[0]
    number = int(instruction[1:])

    return letter == "R", number


if __name__ == "__main__":
    main()
