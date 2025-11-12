from collections import defaultdict


def main():
    valid_rules = defaultdict(list)

    with open("quest07/data/input1.txt", "r") as file:
        lines = file.readlines()
        names = lines[0].strip().split(",")

        for line in lines[2:]:
            left, right = line.split(">")
            valid_rules[left.strip()] = [
                target.strip() for target in right.strip().split(",")
            ]

        for name in names:
            if is_valid_name(name, valid_rules):
                print(f"{name} is valid")


def is_valid_name(name, rules):
    for i in range(len(name) - 1):
        left = name[i]
        right = name[i + 1]

        if right not in rules[left]:
            return False
    return True


if __name__ == "__main__":
    main()
