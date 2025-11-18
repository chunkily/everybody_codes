def main():
    with open("quest11/data/input1.txt", "r") as file:
        lines = file.readlines()
        flock = [int(line.strip()) for line in lines]

        round_num = 0
        #print(flock, flock_checksum(flock))
        while phase_one(flock):
            round_num += 1
            if round_num == 10:
                print(round_num, flock, flock_checksum(flock))
            #print(round_num, flock, flock_checksum(flock))
        #print("End of phase one")
        while phase_two(flock):
            round_num += 1
            if round_num == 10:
                print(round_num, flock, flock_checksum(flock))
            #print(round_num, flock, flock_checksum(flock))
        #print("End of phase two")

def flock_checksum(flock):
    sum = 0
    for i in range(len(flock)):
        sum += flock[i] * (i + 1)
    return sum

def phase_one(flock):
    has_changed = False
    for i in range(len(flock) - 1):
        left = flock[i]
        right = flock[i + 1]
        if left > right:
            has_changed = True
            flock[i] -= 1
            flock[i + 1] += 1
    return has_changed

def phase_two(flock):
    has_changed = False
    for i in range(len(flock) - 1):
        left = flock[i]
        right = flock[i + 1]
        if left < right:
            has_changed = True
            flock[i] += 1
            flock[i + 1] -= 1
    return has_changed

if __name__ == "__main__":
    main()
