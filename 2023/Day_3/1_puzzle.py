import re

SHORT = "puzzle_short_input.txt"
LONG = "puzzle_long_input.txt"


def main(input_file: str):
    result = 0
    symbols = {
        "previous": [],
        "current": []
    }
    numbers = {
        "previous": {},
        "current": {}
    }

    with open(input_file, "r") as file:
        for line in file:
            line = line.strip()
            translated_line = translate_line(line)
            numbers["current"] = translated_line[0]
            symbols["current"] = translated_line[1]
            # curr_nums_to_be_removed = []
            # for num_pos, num in numbers["current"].items():
            #     for sym_pos in symbols["current"]:
            #         if num_pos[0] == sym_pos[1] or num_pos[1] == sym_pos[0]:
            #             result += num
            #             curr_nums_to_be_removed.append(num_pos)
            result, curr_nums_to_be_removed = find_neighbours(numbers["current"], symbols["current"], result,
                                                              is_current=True)

            for num_pos in curr_nums_to_be_removed:
                del numbers["current"][num_pos]

            # for num_pos, num in numbers["current"].items():
            #     for sym_pos in symbols["previous"]:
            #         if num_pos[0] == sym_pos[1] or num_pos[1] == sym_pos[0]:
            #             result += num
            result, _ = find_neighbours(numbers["current"], symbols["previous"], result)

            # for num_pos, num in numbers["previous"].items():
            #     for sym_pos in symbols["current"]:
            #         if num_pos[0] == sym_pos[1] or num_pos[1] == sym_pos[0]:
            #             result += num
            result, _ = find_neighbours(numbers["previous"], symbols["current"], result)

            numbers["previous"] = numbers["current"]
            symbols["previous"] = symbols["current"]

    print(result)


def find_neighbours(numbers: dict, symbols: list, result: int, is_current: bool = False):
    curr_nums_to_be_removed = []
    for num_pos, num in numbers.items():
        for sym_pos in symbols:
            if num_pos[0] <= sym_pos[0] <= num_pos[1] or num_pos[0] <= sym_pos[1] <= num_pos[1]:
                result += num
                if is_current:
                    curr_nums_to_be_removed.append(num_pos)

    return result, curr_nums_to_be_removed


def translate_line(line: str):
    numbers = {}
    symbols = []
    matches = re.finditer(r"(\d+|[$#*+@%&\-=/]+)", line)
    for matched in matches:
        matched_txt = matched.group()
        matched_position = matched.span()
        if re.match(r"\d+", matched_txt):
            numbers[matched_position] = int(matched_txt)

        else:
            symbols.append(matched_position)

    return numbers, symbols


if __name__ == "__main__":
    main(SHORT)
    main(LONG)