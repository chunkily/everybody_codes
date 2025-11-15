from collections import defaultdict


def main():
    with open("quest10/data/input3.txt", "r") as file:
        lines = file.readlines()

        dragon_pos = None
        sheep_pos = set()
        hideouts = set()

        r_max = len(lines)
        c_max = len(lines[0].strip())

        for c in range(c_max):
            for r in range(r_max):
                char = lines[r][c]

                if char == "D":
                    dragon_pos = (r, c)
                elif char == "S":
                    sheep_pos.add((r, c))
                elif char == "#":
                    hideouts.add((r, c))

        game_states = [(dragon_pos, tuple(sorted(sheep_pos)))]
        visited = defaultdict(list)
        visited[game_states[0]].append((None, None, None))

        while game_states:
            next_data = []
            for game_state in game_states:
                for after_sheep, sheep_move in sheep_turn(
                    game_state, hideouts, r_max, c_max
                ):
                    if after_sheep is None:
                        # Sheep wins
                        pass
                    else:
                        for after_dragon, dragon_move in dragon_turn(
                            after_sheep, hideouts, r_max, c_max
                        ):
                            next_data.append(
                                (after_dragon, sheep_move, dragon_move, game_state)
                            )

            game_states = []
            for state, sheep_move, dragon_move, parent in next_data:
                if state not in visited and len(state[1]) > 0:
                    game_states.append(state)

                visited[state].append((parent, sheep_move, dragon_move))
            print("States to explore:", len(game_states))

        # rebuild_winning_sequences(visited)
        count_winning_sequences(visited)


def rebuild_winning_sequences(visited):
    dragon_winning_sequences = []
    frontier = []

    dragon_win_states = [state for state in visited.keys() if len(state[1]) == 0]
    for state in dragon_win_states:
        frontier.append((state, ""))

    while frontier:
        current_key, sequence = frontier.pop()
        parents = visited[current_key]
        for parent_key, sheep_move, dragon_move in parents:
            if parent_key is None:
                # Reached root
                dragon_winning_sequences.append(sequence.strip())
            else:
                new_sequence = f"{sheep_move} {dragon_move} " + sequence
                frontier.append((parent_key, new_sequence))

    if len(dragon_winning_sequences) < 50:
        for seq in dragon_winning_sequences:
            print(seq)

    print("Number of winning sequences:", len(dragon_winning_sequences))


def count_winning_sequences(visited):
    count_ways = {}

    def count_ways_to_win(state_key):
        if state_key in count_ways:
            return count_ways[state_key]

        parents = visited[state_key]
        total_ways = 0
        for parent_key, sheep_move, dragon_move in parents:
            if parent_key is None:
                total_ways += 1
            else:
                total_ways += count_ways_to_win(parent_key)

        count_ways[state_key] = total_ways
        return total_ways

    total_dragon_winning_sequences = 0
    dragon_win_states = [state for state in visited.keys() if len(state[1]) == 0]
    for state in dragon_win_states:
        total_dragon_winning_sequences += count_ways_to_win(state)

    print("Number of winning sequences:", total_dragon_winning_sequences)


def sheep_turn(game_state, hideouts, r_max, c_max):
    has_valid_moves = False
    dragon = game_state[0]
    sheep = game_state[1]

    for sheep_pos in sheep:
        new_r = sheep_pos[0] + 1

        if new_r >= r_max:
            # Sheep wins
            yield None, None
            return

        new_pos = (new_r, sheep_pos[1])
        if new_pos != dragon or new_pos in hideouts:
            has_valid_moves = True

            next_sheep = set(sheep)
            next_sheep.remove(sheep_pos)
            next_sheep.add(new_pos)

            yield (dragon, tuple(sorted(next_sheep))), move_id("S", new_pos)

    if not has_valid_moves:
        # Sheep cannot move, skips turn
        yield (dragon, tuple(sorted(sheep))), "S>"


def dragon_turn(game_state, hideouts, r_max, c_max):
    dragon = game_state[0]
    sheep = game_state[1]

    for dragon_pos in generate_moves(dragon, r_max, c_max):
        if dragon_pos in sheep and dragon_pos not in hideouts:
            next_sheep = set(sheep)
            next_sheep.remove(dragon_pos)
            next_state = (dragon_pos, tuple(sorted(next_sheep)))
            yield next_state, move_id("D", dragon_pos)
        else:
            yield (dragon_pos, sheep), move_id("D", dragon_pos)


def move_id(player, pos):
    row, col = pos
    letter = chr(ord("A") + col)
    return f"{player}>{letter}{row + 1}"


def generate_moves(pos, r_max, c_max):
    r, c = pos
    if r - 2 >= 0 and c - 1 >= 0:
        yield (r - 2, c - 1)
    if r - 2 >= 0 and c + 1 < c_max:
        yield (r - 2, c + 1)
    if r - 1 >= 0 and c - 2 >= 0:
        yield (r - 1, c - 2)
    if r - 1 >= 0 and c + 2 < c_max:
        yield (r - 1, c + 2)
    if r + 1 < r_max and c - 2 >= 0:
        yield (r + 1, c - 2)
    if r + 1 < r_max and c + 2 < c_max:
        yield (r + 1, c + 2)
    if r + 2 < r_max and c - 1 >= 0:
        yield (r + 2, c - 1)
    if r + 2 < r_max and c + 1 < c_max:
        yield (r + 2, c + 1)


if __name__ == "__main__":
    main()
