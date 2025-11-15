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

    game_state = {
        "dragon": dragon_pos,
        "sheep": sheep_pos,
        "moves": list(),
        "debug": "",
    }

    dragon_win_count = 0
    game_states = [game_state]
    # visited = set()
    # Need to track number of ways to reach a state
    visited = dict()
    while game_states:
        next_states = []
        for game_state in game_states:
            for after_sheep in sheep_turn(game_state, hideouts, r_max, c_max):
                if after_sheep is None:
                    # Sheep wins
                    pass
                    # print("Sheep wins. Moves:" + " ".join(game_state["moves"]))
                else:
                    for after_dragon in dragon_turn(
                        after_sheep, hideouts, r_max, c_max
                    ):
                        if len(after_dragon["sheep"]) == 0:
                            # Dragon wins
                            dragon_win_count += 1
                            print(
                                f"Dragon win #{dragon_win_count}. Moves:"
                                + " ".join(after_dragon["moves"])
                            )
                        else:
                            k = state_key(after_dragon)

                            visited.add(state_key(after_dragon))
                            next_states.append(after_dragon)

        print("next states:", len(next_states))
        game_states = next_states

    print("Dragon win count:", dragon_win_count)


def sheep_turn(game_state, hideouts, r_max, c_max):
    has_valid_moves = False
    for sheep_pos in game_state["sheep"]:
        new_r = sheep_pos[0] + 1

        if new_r >= r_max:
            # Sheep wins
            yield None
            return

        new_pos = (new_r, sheep_pos[1])
        if new_pos != game_state["dragon"] or new_pos in hideouts:
            has_valid_moves = True
            move_id_str = move_id("S", new_pos)
            # next_sheep = game_state["sheep"] - {sheep_pos} + {new_pos}
            next_sheep = set(game_state["sheep"])
            next_sheep.remove(sheep_pos)
            next_sheep.add(new_pos)

            yield {
                "dragon": game_state["dragon"],
                "sheep": next_sheep,
                "moves": game_state["moves"] + [move_id_str],
            }

    if not has_valid_moves:
        # Sheep cannot move, skips turn
        yield {
            "dragon": game_state["dragon"],
            "sheep": game_state["sheep"],
            "moves": game_state["moves"] + ["S>SKIP"],
        }


def dragon_turn(game_state, hideouts, r_max, c_max):
    for dragon_pos in generate_moves(game_state["dragon"], r_max, c_max):
        if dragon_pos in game_state["sheep"] and dragon_pos not in hideouts:
            next_sheep = set(game_state["sheep"])
            next_sheep.remove(dragon_pos)
            next_state = {
                "dragon": dragon_pos,
                "sheep": next_sheep,
                "moves": game_state["moves"] + [move_id("D", dragon_pos)],
            }
            yield next_state
        else:
            yield {
                "dragon": dragon_pos,
                "sheep": game_state["sheep"],
                "moves": game_state["moves"] + [move_id("D", dragon_pos)],
            }


def move_id(player, pos):
    row, col = pos
    letter = chr(ord("A") + col)
    return f"{player}>{letter}{row + 1}"


def state_key(state) -> tuple:
    return (state["dragon"], *tuple(sorted(state["sheep"])))
    # return (len(state["moves"]), state["dragon"], *tuple(sorted(state["sheep"])))


def serialize_state(dragon, sheep) -> str:
    dragon_str = f"D:{dragon[0]},{dragon[1]}"
    sheep_str = " ".join(f"{s[0]},{s[1]}" for s in sorted(sheep))
    return f"{dragon_str}|{sheep_str}"


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
