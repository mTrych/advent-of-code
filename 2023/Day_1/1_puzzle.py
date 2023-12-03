import re

SHORT = "1_puzzle_short_input.txt"
LONG = "1_puzzle_long_input.txt"


def main(input_file: str):
    result = 0
    with open(input_file, "r") as file:
        count = 0
        for line in file:
            count += 1
            # print(count)
            first = None
            last = None
            line = line.strip()
            for char in line:
                if re.match(r"\d+", char):
                    if not first:
                        first = char

                    last = char

            result += int(f"{first}{last}")

    print(result)


if __name__ == "__main__":
    main(SHORT)
    main(LONG)
