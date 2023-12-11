from pathlib import Path


def read_file(filename: str):
    """Read the provided filename and return a list of lines"""
    path = Path(__file__).with_name(filename)
    file = path.open("r")

    return [line.strip() for line in file]


def main():
    print("Advent of code XX")


if __name__ == "__main__":
    main()
