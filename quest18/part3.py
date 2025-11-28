import re

pattern_1 = r"Plant (\d+) with thickness (\d+)"
pattern_2 = r"- free branch with thickness 1"
pattern_3 = r"- branch to Plant (\d+) with thickness (-?\d+)"
pattern_4 = r"^\d+"


def main():
    plants = dict()
    branches = dict()
    test_cases = set()
    free_branch_plant_ids = set()

    with open("quest18/data/input3.txt", "r") as file:
        plant_id = None
        for line in file.readlines():
            if match := re.match(pattern_1, line):
                plant_id = int(match.group(1))
                plants[plant_id] = int(match.group(2))
                branches[plant_id] = []
            elif match := re.match(pattern_2, line):
                other_plant_id = 0
                branch_thickness = 1
                branches[plant_id].append((other_plant_id, branch_thickness))
                free_branch_plant_ids.add(plant_id)
            elif match := re.match(pattern_3, line):
                other_plant_id = int(match.group(1))
                branch_thickness = int(match.group(2))
                branches[plant_id].append((other_plant_id, branch_thickness))
            elif match := re.match(pattern_4, line):
                test_case = parse_test_case(line)

                test_cases.add(test_case)

    last_plant_id = plant_id

    test_results = dict()

    for test_case in test_cases:
        plant_energies = dict()
        plant_energies[0] = 1
        apply_test_case(plant_energies, test_case)

        result = calculate_plant_energy(last_plant_id, plants, branches, plant_energies)
        if result > 0:
            test_results[test_case] = result

    # Best initial guess from test case with highest result
    initial_guess = max(test_results, key=test_results.get)

    max_result = get_max_energy(
        last_plant_id, plants, branches, free_branch_plant_ids, initial_guess
    )
    print("Maximum possible energy:", max_result)
    answer = 0
    for test_case, result in test_results.items():
        # print(f"Test case {test_case}: {result}")
        difference = max_result - result
        answer += difference

    print("Sum of differences:", answer)


def parse_test_case(line):
    s = line.strip().replace(" ", "")

    return tuple(int(x) for x in s)


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


# Maybe a greedy gradient descent approach could work?
def get_max_energy(
    plant_id, all_plants, all_branches, free_branch_plant_ids, initial_guess
):
    free_branch_count = len(free_branch_plant_ids)
    test_case = initial_guess

    plant_energies = dict()
    plant_energies[0] = 1
    apply_test_case(plant_energies, test_case)

    result = calculate_plant_energy(plant_id, all_plants, all_branches, plant_energies)

    improved = True
    while improved:
        improved = False
        for i in range(free_branch_count):
            new_test_case = bit_toggle(test_case, i)

            plant_energies = dict()
            plant_energies[0] = 1
            apply_test_case(plant_energies, new_test_case)

            new_result = calculate_plant_energy(
                plant_id, all_plants, all_branches, plant_energies
            )

            if new_result > result:
                test_case = new_test_case
                result = new_result
                print(f"New max energy: {result} with test case {test_case}")
                improved = True

    return result


def bit_toggle(test_case, index):
    lst = list(test_case)
    lst[index] = 1 - lst[index]
    return tuple(lst)


if __name__ == "__main__":
    main()
