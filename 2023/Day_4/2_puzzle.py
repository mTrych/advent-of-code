import re

SHORT = "puzzle_short_input.txt"
LONG = "puzzle_long_input.txt"


def main(input_file: str):
    result = 0
    with open(input_file, "r") as file:
        scratchcards = {}
        for line in file:
            line = line.strip()
            card, nums = line.split(":")
            card_id = int(re.sub(" +", ",", card).split(",")[1])
            if scratchcards.get(card_id):
                scratchcards[card_id] += 1

            else:
                scratchcards[card_id] = 1

            winning_nums, drawn_nums = nums.split(" | ")
            winning_nums = set(re.sub(" +", ",", winning_nums.strip()).split(","))
            drawn_nums = re.sub(" +", ",", drawn_nums.strip()).split(",")
            matched_nums_count = 0
            for drawn_num in drawn_nums:
                if drawn_num in winning_nums:
                    matched_nums_count += 1

            for i in range(card_id+1, card_id+matched_nums_count+1):
                multiplier = scratchcards[card_id]
                if scratchcards.get(i):
                    scratchcards[i] += 1 * multiplier

                else:
                    scratchcards[i] = 1 * multiplier

    for value in scratchcards.values():
        result += value

    print(result)


if __name__ == "__main__":
    main(SHORT)
    main(LONG)
