def main():
    wall = [0] * 91

    total = 0
    with open("quest16/data/input1.txt", "r") as file:
        text = file.read()
        numbers = [int(num) for num in text.split(",")]

        for i in range(1, 90 + 1):
            for n in numbers:
                if i % n == 0:
                    wall[i] = wall[i] + 1
                    total += 1
        print(wall)
    print(total)


if __name__ == "__main__":
    main()
