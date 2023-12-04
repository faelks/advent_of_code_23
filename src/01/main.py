from pathlib import Path


def read_file(filename: str):
    """Read the provided filename and return a list of lines"""
    path = Path(__file__).with_name(filename)
    file = path.open("r")

    return [line.strip() for line in file]


def spelled_digit(input: str):
    """Return a digit if the string is a spelled out digit"""

    to_int = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    max_key_length = max(to_int, key=len)

    if len(input) > len(max_key_length):
        return None

    ltr = to_int.get(input, None)
    rtl = to_int.get(input[::-1], None)

    return ltr or rtl


def get_first_digit(input: str):
    """Return the first digit in the string"""
    for i, char in enumerate(input):
        if char.isnumeric():
            return char
        for j in range(i + 1):
            found_digit = spelled_digit(input[j : i + 1])
            if found_digit:
                return found_digit
    return None


def main():
    print("Advent of code 01")

    filename = "input.txt"
    lines = read_file(filename)

    sum = 0
    for line in lines:
        first = get_first_digit(line)
        last = get_first_digit(line[::-1])

        if not first and not last:
            raise Exception(f"Could not find numbers in line: {line}")

        sum += int(f"{first}{last}")

    print(f"Sum: {sum}")


if __name__ == "__main__":
    main()
