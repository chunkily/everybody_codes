import re


def main():
    with open("quest02/data/input3.txt", "r") as file:
        text = file.read().strip()
        pattern = r"A=\[(-?\d+),(-?\d+)\]"
        match = re.search(pattern, text)
        if match:
            x_input = int(match.group(1))
            y_input = int(match.group(2))
            print(f"x_input={x_input}, y_input={y_input}")
        else:
            print("No match found.")
            return

    count = 0

    for y in range(y_input, y_input + 1001):
        for x in range(x_input, x_input + 1001):
            if engrave(x, y):
                count += 1

    print(f"Final count: {count}")


def multiply(x1, y1, x2, y2):
    return (x1 * x2) - (y1 * y2), (x1 * y2) + (y1 * x2)


def divide(x1, y1, x2, y2):
    return int(x1 / x2), int(y1 / y2)


def add(x1, y1, x2, y2):
    return x1 + x2, y1 + y2


def cycle(x, y, xa, ya):
    x, y = multiply(x, y, x, y)

    x, y = divide(x, y, 100000, 100000)

    x, y = add(x, y, xa, ya)

    return x, y


def engrave(xa, ya):
    x = 0
    y = 0

    for _ in range(100):
        x, y = cycle(x, y, xa, ya)

        if x > 1000000 or x < -1000000 or y > 1000000 or y < -1000000:
            # print(_, x, y)
            return False

    # print(x, y)
    return True


if __name__ == "__main__":
    main()
    # engrave(35630, -64880)
    # engrave(35630, -64870)
    # engrave(35640, -64860)
    # engrave(36230, -64270)
    # engrave(36250, -64270)

    # print(engrave(35460, -64910))
    # print(engrave(35470, -64910))
    # print(engrave(35480, -64910))
    # print(engrave(35680, -64850))
    # print(engrave(35630, -64830))
