import re

REPEAT_COUNT = 1000
DIST = 1000


def main():
    sum = 0
    with open("quest06/data/input3.txt", "r") as file:
        text = file.read().strip()

        repeated = text * REPEAT_COUNT

        for i, letter in enumerate(repeated):
            sum += count_mentors(repeated, letter, i)

    print(sum)


def is_uppercase(letter):
    return re.match(r"[A-Z]", letter) is not None


def count_mentors(full_text, letter, current_index):
    if is_uppercase(letter):
        return 0

    left = max(current_index - DIST, 0)
    right = min(current_index + DIST + 1, len(full_text))

    mentor = letter.upper()

    count = 0
    for i in range(left, right):
        if full_text[i] == mentor:
            count += 1

    # print(f"letter: {letter}, index: {current_index}, count: {count}")
    return count


if __name__ == "__main__":
    main()
