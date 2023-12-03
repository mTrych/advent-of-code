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
INPUT_TXT = "eightwothree"
result = ""
i = 0
while i < len(INPUT_TXT):
    translated = False
    translated_window = 0
    for window_len in [3, 4, 5]:
        if i + window_len > len(INPUT_TXT):
            break

        tmp_txt = INPUT_TXT[i:i + window_len]
        if DIGITS_MAP.get(tmp_txt):
            result += DIGITS_MAP.get(tmp_txt)
            translated = True
            translated_window = window_len
            break

    if translated:
        i += 1
        continue

    result += INPUT_TXT[i]
    i += 1

print(result)
