def main():
    with open("quest03/data/input1.txt", "r") as file:
        sizes = [int(x) for x in file.read().split(",")]

    sizes.sort(reverse=True)

    sum = 0
    current = sizes[0] + 1
    for size in sizes:
        if size < current:
            sum += size
            current = size

    print(sum)


if __name__ == "__main__":
    main()
