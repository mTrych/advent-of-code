SHORT = "1_puzzle_short_input.txt"
LONG = "1_puzzle_long_input.txt"
LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def main(input_file: str):
    result = 0
    with open(input_file, "r") as file:
        for line in file:
            game, game_sets = line.strip().split(":")
            game_id = int(game.split(" ")[1])
            cubes_shown = game_sets.replace(";", ",").split(", ")
            is_valid = True
            for cubes in cubes_shown:
                count, color = cubes.strip().split(" ")
                if int(count) > LIMITS.get(color):
                    is_valid = False
                    break

            if not is_valid:
                continue

            result += game_id

    print(result)


if __name__ == "__main__":
    main(SHORT)
    main(LONG)
