nail_count = 256


def main():
    with open("quest08/data/input2.txt", "r") as file:
        numbers = [int(n) for n in file.read().strip().split(",")]

        num_knots = 0

        edges = list()
        for _ in range(len(numbers) - 1):
            a = numbers[_]
            b = numbers[_ + 1]

            if b > a:
                next = (a, b)
            else:
                next = (b, a)

            for e1 in edges:
                if do_edges_intersect(e1, next):
                    num_knots += 1

            edges.append(next)

        print(f"Total number of knots: {num_knots}")


def do_edges_intersect(e1, e2):
    # e1 splits the circle into two parts
    # if one point of e2 is in one half and the other point is in the other half, they intersect
    a, b = e1  # a < b
    c, d = e2  # c < d

    # If any of the points are the same, they don't intersect
    if a == c or b == d or b == c or a == d:
        return False

    c_side = a < c and c < b
    d_side = a < d and d < b

    # If c and d are on different sides of e1, they intersect
    return c_side != d_side


if __name__ == "__main__":
    main()
