from collections import defaultdict
import re


def main():
    sum = 0
    with open("quest06/data/input1.txt", "r") as file:
        text = file.read().strip()

        a_only = [a for a in text if a in "Aa"]

        mentor_count = defaultdict(int)

        for letter in a_only:
            if is_uppercase(letter):
                mentor_count[letter] += 1
            else:
                sum += mentor_count[letter.upper()]

    print(sum)


def is_uppercase(letter):
    return re.match(r"[A-Z]", letter) is not None


if __name__ == "__main__":
    main()
