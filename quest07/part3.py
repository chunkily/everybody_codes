from collections import defaultdict


def main():
    valid_rules = defaultdict(list)

    with open("quest07/data/input3.txt", "r") as file:
        lines = file.readlines()
        names = lines[0].strip().split(",")

        for line in lines[2:]:
            left, right = line.split(">")
            valid_rules[left.strip()] = [
                target.strip() for target in right.strip().split(",")
            ]

        all_names = set()
        for prefix in names:
            if is_valid_name(prefix, valid_rules):
                add_unique_names(all_names, prefix, valid_rules)

        sum = 0
        for name in all_names:
            if len(name) >= 7:
                sum += 1

        print(f"Total unique names from all valid prefixes: {sum}")


def is_valid_name(name, rules):
    for i in range(len(name) - 1):
        left = name[i]
        right = name[i + 1]

        if right not in rules[left]:
            return False
    return True


def add_unique_names(all_names, prefix, rules):
    frontier = [prefix]

    while frontier:
        next = frontier.pop()

        if len(next) < 11:
            for right in rules[next[-1]]:
                new_name = next + right
                if new_name not in all_names:
                    all_names.add(new_name)
                    frontier.append(new_name)


if __name__ == "__main__":
    main()
