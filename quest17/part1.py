def main():
    field = list()
    origin = None
    with open("quest17/data/input1.txt", "r") as file:
        for y, line in enumerate(file.readlines()):
            row = list()
            for x, char in enumerate(line.strip()):
                if char == "@":
                    row.append(0)
                    origin = (x, y)
                else:
                    row.append(int(char))
            field.append(row)
    max_y = len(field)
    max_x = len(field[0])

    total = 0
    radius = 10
    for y in range(max_y):
        for x in range(max_x):
            if is_destroyed(x, y, origin[0], origin[1], radius):
                total += field[y][x]
    print(f"answer: {total}")


def is_destroyed(xc, xy, xv, yv, r):
    return (xv - xc) * (xv - xc) + (yv - xy) * (yv - xy) <= r * r


if __name__ == "__main__":
    main()
