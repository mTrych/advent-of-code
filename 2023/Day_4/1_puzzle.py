import re

SHORT = "puzzle_short_input.txt"
LONG = "puzzle_long_input.txt"


def main(input_file: str):
    result = 0
    with open(input_file, "r") as file:
        for line in file:
            line = line.strip()
            winning_nums, drawn_nums = line.split(":")[1].split(" | ")
            winning_nums = set(re.sub(" +", ",", winning_nums.strip()).split(","))
            drawn_nums = re.sub(" +", ",", drawn_nums.strip()).split(",")
            drawn_power = -1
            for drawn_num in drawn_nums:
                if drawn_num in winning_nums:
                    drawn_power += 1

            if drawn_power != -1:
                result += 2**drawn_power

    print(result)


if __name__ == "__main__":
    main(SHORT)
    main(LONG)
