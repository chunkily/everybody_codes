import math

nail_count = 32


def main():
    with open("quest08/data/input1.txt", "r") as file:
        numbers = [int(n) for n in file.read().strip().split(",")]
        half = nail_count // 2

        sum = 0
        for _ in range(len(numbers) - 1):
            prev = numbers[_]
            target = numbers[_ + 1]

            if abs(target - prev) == half:
                sum += 1

        print(f"Total number of passes through center: {sum}")


if __name__ == "__main__":
    main()
