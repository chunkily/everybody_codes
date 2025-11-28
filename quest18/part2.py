import re

pattern_1 = r"Plant (\d+) with thickness (\d+)"
pattern_2 = r"- free branch with thickness (\d+)"
pattern_3 = r"- branch to Plant (\d+) with thickness (-?\d+)"
pattern_4 = r"^\d+"


def main():
    plants = dict()
    branches = dict()
    test_cases = list()
    with open("quest18/data/input2.txt", "r") as file:
        plant_id = None
        for line in file.readlines():
            if match := re.match(pattern_1, line):
                plant_id = int(match.group(1))
                plants[plant_id] = int(match.group(2))
                branches[plant_id] = []
            elif match := re.match(pattern_2, line):
                other_plant_id = 0
                branch_thickness = int(match.group(1))
                branches[plant_id].append((other_plant_id, branch_thickness))
            elif match := re.match(pattern_3, line):
                other_plant_id = int(match.group(1))
                branch_thickness = int(match.group(2))
                branches[plant_id].append((other_plant_id, branch_thickness))
            elif match := re.match(pattern_4, line):
                test_case = [int(x) for x in line.strip().split(" ")]

                test_cases.append(test_case)

    last_plant_id = plant_id

    answer = 0
    for test_case in test_cases:
        plant_energies = dict()
        plant_energies[0] = 1
        apply_test_case(plant_energies, test_case)

        answer += calculate_plant_energy(
            last_plant_id, plants, branches, plant_energies
        )

    print(answer)


def apply_test_case(plant_energies, test_case):
    for i, energy in enumerate(test_case):
        plant_energies[i + 1] = energy


def calculate_plant_energy(plant_id, all_plants, all_branches, plant_energies):
    if plant_id in plant_energies:
        return plant_energies[plant_id]

    branches = all_branches[plant_id]

    plant_energy = 0
    for other_plant_id, branch_thickness in branches:
        other_plant_energy = calculate_plant_energy(
            other_plant_id, all_plants, all_branches, plant_energies
        )
        plant_energy += other_plant_energy * branch_thickness

    thickness = all_plants[plant_id]
    if plant_energy < thickness:
        plant_energy = 0

    plant_energies[plant_id] = plant_energy

    return plant_energy


if __name__ == "__main__":
    main()
