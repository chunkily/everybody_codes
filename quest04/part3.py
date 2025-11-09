def main():
    teeth_pairs = []
    with open("quest04/data/input3.txt", "r") as file:
        lines = file.readlines()
        teeth_pairs.append((1, int(lines[0].strip())))
        for line in lines[1:-1]:
            a, b = map(int, line.strip().split("|"))
            teeth_pairs.append((a, b))
        teeth_pairs.append((int(lines[-1].strip()), 1))

    print(teeth_pairs)

    all_ratio = 1.0
    prev_right = 1
    for pair in teeth_pairs:
        left, right = pair
        ratio = prev_right / left
        all_ratio *= ratio
        prev_right = right

    print(f"Full rotations on last gear: {int(all_ratio * 100)}")


if __name__ == "__main__":
    main()
