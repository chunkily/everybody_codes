def main():
    with open("quest03/data/input2.txt", "r") as file:
        sizes = [int(x) for x in file.read().split(",")]

    sizes.sort()

    sum = 0
    current = sizes[0] - 1
    count = 0
    for size in sizes:
        if size > current:
            sum += size
            current = size
            count += 1

            if count == 20:
                print(
                    f"smallest possible set of 20 crates for this list of crates: {sum}"
                )
                return

    print(
        f"Unexpectedly found less than 20 unique sizes. {count} unique sizes found with sum {sum}."
    )


if __name__ == "__main__":
    main()
