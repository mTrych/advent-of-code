import re

SHORT = "puzzle_short_input.txt"
LONG = "puzzle_long_input.txt"


class Number:
    line: int
    position: tuple
    value: int

    def __init__(self, line: int, position: tuple, value: int):
        self.line = line
        self.position = position
        self.value = value

    def __repr__(self):
        return f"{self.value} at {self.position} at line {self.line}"

    def __str__(self):
        return f"{self.value} at {self.position} at line {self.line}"

    def __eq__(self, other):
        return (self.value, self.position, self.line) == (other.value, other.position, other.line)


class Star:
    line: int
    position: tuple
    value: str

    def __init__(self, line: int = -1, position: tuple = (-1, -1)):
        self.line = line
        self.position = position
        self.value = "*"

    def __repr__(self):
        return f"{self.value} at {self.position} at line {self.line}"

    def __str__(self):
        return f"{self.value} at {self.position} at line {self.line}"

    def __eq__(self, other):
        return (self.value, ) == (other.value, )


def main(input_file: str):
    result = 0
    gears = {}
    with open(input_file, "r") as file:
        file = file.readlines()
        for i in range(1, len(file)-1):
            window = file[i-1:i+2]
            for line in window:
                if "*" in line:
                    translated_window = translate_window(window, i-1)
                    stars_positions = []
                    for translated_line in translated_window:
                        for element in translated_line:
                            if isinstance(element, Star):
                                stars_positions.append(element)

                    for star_position in stars_positions:
                        matched_elements = []
                        for translated_line in translated_window:
                            for element in translated_line:
                                if not isinstance(element, Star):
                                    if abs(element.line - star_position.line) <= 1:
                                        if element.position[0] <= star_position.position[0] <= element.position[1] or element.position[0] <= star_position.position[1] <= element.position[1]:
                                            if element not in matched_elements:
                                                matched_elements.append(element)

                        if len(matched_elements) == 2:
                            # print(matched_elements)
                            gear_key = ""
                            for element in matched_elements:
                                gear_key += str(element)
                            gear_key += str(star_position)
                            if gear_key not in gears:
                                first, second = matched_elements
                                gears[gear_key] = first.value * second.value

                    break

    for value in gears.values():
        result += value

    print(result)


def find_neighbours(numbers: dict, symbols: dict, result: int, is_current: bool = False):
    nums_to_be_removed = []
    for num_pos, num in numbers.items():
        for sym_pos in symbols:
            if num_pos[0] <= sym_pos[0] <= num_pos[1] or num_pos[0] <= sym_pos[1] <= num_pos[1]:
                result += num
                if is_current:
                    nums_to_be_removed.append(num_pos)

    return result, nums_to_be_removed


def translate_window(lines: list, window_line: int):
    translated = []
    for line in lines:
        line = line.strip()
        matches = re.finditer(r"(\d+|[*]+)", line)
        translated_line = []
        for matched in matches:
            matched_txt = matched.group()
            matched_position = matched.span()
            if re.match(r"\d+", matched_txt):
                translated_line.append(Number(window_line, matched_position, int(matched_txt)))

            else:
                translated_line.append(Star(window_line, matched_position))

        window_line += 1
        translated.append(translated_line)

    return translated


if __name__ == "__main__":
    main(SHORT)
    main(LONG)