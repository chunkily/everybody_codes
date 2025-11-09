def main():
    with open("quest04/data/input1.txt", "r") as file:
        teeth = [int(x) for x in file.readlines()]
        print(teeth)

    all_ratio = 1.0
    prev = teeth[0]
    for tooth in teeth:
        ratio = prev / tooth
        all_ratio *= ratio
        # print(f"tooth: {tooth}, prev: {prev}, ratio: {ratio}, all_ratio: {all_ratio}")
        prev = tooth

    print(f"Full rotations on last gear: {int(all_ratio * 2025)}")


if __name__ == "__main__":
    main()
