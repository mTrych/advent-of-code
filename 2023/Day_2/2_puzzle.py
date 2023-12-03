
SHORT = "2_puzzle_short_input.txt"
LONG = "2_puzzle_long_input.txt"


def main(input_file: str):
    result = 0
    with open(input_file, "r") as file:
        for line in file:
            _, game_sets = line.strip().split(":")
            cubes_shown = game_sets.replace(";", ",").split(", ")
            cubes_max = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            for cubes in cubes_shown:
                count, color = cubes.strip().split(" ")
                count = int(count)
                if count > cubes_max.get(color):
                    cubes_max[color] = count

            values = cubes_max.values()
            multi_value = 1
            for value in values:
                multi_value *= value

            result += multi_value

    print(result)


if __name__ == "__main__":
    main(SHORT)
    main(LONG)
