def main():
    field = list()
    origin = None
    with open("quest17/data/input2.txt", "r") as file:
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

    highest_destruction = 0
    highest_radius = 0

    for radius in range(1, max(max_x, max_y)):
        destruction = 0
        for y in range(max_y):
            for x in range(max_x):
                if is_destroyed(x, y, origin[0], origin[1], radius):
                    destruction += field[y][x]
                    field[y][x] = 0  # Prevent double counting in larger radii
        if destruction > highest_destruction:
            highest_destruction = destruction
            highest_radius = radius

    print(
        f"answer: {highest_radius * highest_destruction} = {highest_radius} * {highest_destruction}"
    )


def is_destroyed(xc, yc, xv, yv, r):
    return (xv - xc) * (xv - xc) + (yv - yc) * (yv - yc) <= r * r


if __name__ == "__main__":
    main()
