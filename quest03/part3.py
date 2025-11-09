from collections import defaultdict


def main():
    with open("quest03/data/input3.txt", "r") as file:
        sizes = [int(x) for x in file.read().split(",")]

    # answer is largest count of duplicate values
    d = defaultdict(int)
    for size in sizes:
        d[size] += 1

    max_count = max(d.values())
    print(f"Minimum number of sets: {max_count}")


if __name__ == "__main__":
    main()
