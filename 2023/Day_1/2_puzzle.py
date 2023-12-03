import re

SHORT = "2_puzzle_short_input.txt"
LONG = "1_puzzle_long_input.txt"
DIGITS_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def main(input_file: str):
    result = 0
    with open(input_file, "r") as file:
        for line in file:
            first = None
            last = None
            line = line.strip()
            line = translate_words_to_digits(line)
            for char in line:
                if re.match(r"\d+", char):
                    if not first:
                        first = char

                    last = char

            # print(f"{first}{last}")
            # print()
            result += int(f"{first}{last}")

    print(result)


def translate_words_to_digits(line: str):
    result = ""
    i = 0
    while i < len(line):
        for window_len in [3, 4, 5]:
            if i + window_len > len(line):
                break

            tmp_txt = line[i:i + window_len]
            if DIGITS_MAP.get(tmp_txt):
                result += DIGITS_MAP.get(tmp_txt)
                break

        result += line[i]
        i += 1

    return result


if __name__ == "__main__":
    main(SHORT)
    main(LONG)
