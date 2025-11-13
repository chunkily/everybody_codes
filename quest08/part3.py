nail_count = 256


def main():
    with open("quest08/data/input3.txt", "r") as file:
        numbers = [int(n) for n in file.read().strip().split(",")]

        edges = list()
        for _ in range(len(numbers) - 1):
            a = numbers[_]
            b = numbers[_ + 1]

            if b > a:
                next = (a, b)
            else:
                next = (b, a)

            edges.append(next)

        most_intersects = 0
        for a in range(nail_count):
            for b in range(a + 1, nail_count):
                edge = (a + 1, b + 1)
                num_intersects = 0
                for e in edges:
                    if do_edges_intersect(e, edge) or e == edge:
                        num_intersects += 1
                if num_intersects > most_intersects:
                    most_intersects = num_intersects

        print(f"Maximum possible threads cut: {most_intersects}")


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
