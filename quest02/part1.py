import re


def main():
    with open("quest02/data/input1.txt", "r") as file:
        text = file.read().strip()
        # A=[25,9]
        pattern = r"A=\[(\d+),(\d+)\]"
        match = re.search(pattern, text)
        if match:
            xa = int(match.group(1))
            ya = int(match.group(2))
            print(f"x={xa}, y={ya}")
        else:
            print("No match found.")
            return

    x = 0
    y = 0
    for _ in range(3):
        x, y = cycle(x, y, xa, ya)
        print(f"x={x}, y={y}")

    print(f"Final result: [{x},{y}]")


def multiply(x1, y1, x2, y2):
    return x1 * x2 - y1 * y2, x1 * y2 + y1 * x2


def divide(x1, y1, x2, y2):
    return x1 // x2, y1 // y2


def add(x1, y1, x2, y2):
    return x1 + x2, y1 + y2


def cycle(x, y, xa, ya):
    x, y = multiply(x, y, x, y)

    x, y = divide(x, y, 10, 10)

    x, y = add(x, y, xa, ya)

    return x, y


if __name__ == "__main__":
    main()
