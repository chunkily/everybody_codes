def main():
    with open("quest01/data/input2.txt", "r") as file:
        names = file.readline().strip().split(",")
        file.readline()
        instructions = file.readline().strip().split(",")

        print(names, len(names))
        print(instructions)

        pos = 0
        num_names = len(names)
        for instruction in instructions:
            is_right, number = parse_instruction(instruction)

            if is_right:
                next_pos = (pos + number) % num_names
                print(f"Moved right {number} from {pos} to position {next_pos}")
            else:
                next_pos = (pos - number) % num_names
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
