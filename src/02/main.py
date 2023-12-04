from pathlib import Path


def read_file(filename: str):
    """Read the provided filename and return a list of lines"""
    path = Path(__file__).with_name(filename)
    file = path.open("r")

    return [line.strip() for line in file]


def parse_line(line: str):
    """Parse a line and return a tuple with game id and rgb counts
    Example Line: Game 1: 1 green, 2 red, 6 blue; 4 red, 1 green, 3 blue; 7 blue, 5 green; 6 blue, 2 red, 1 green
    Example Output: (1, {"red": [2, 4], "green": [1, 5], "blue": [6, 3, 7, 6]})
    """

    [game_with_id, all_games] = line.split(":")
    game_id = int(game_with_id.split(" ")[1])
    games = [game.strip() for game in all_games.split(";")]

    rgb = {
        "red": [],
        "green": [],
        "blue": [],
    }
    for game in games:
        for color_count in [v.strip() for v in game.split(",")]:
            count = int(color_count.split(" ")[0])

            if "red" in color_count:
                rgb["red"].append(count)
            elif "green" in color_count:
                rgb["green"].append(count)
            elif "blue" in color_count:
                rgb["blue"].append(count)

    return (game_id, rgb)


def find_min_config(rgb: dict):
    """Find the minimum configuration for the game to be possible"""

    return {
        "red": max(rgb["red"]),
        "green": max(rgb["green"]),
        "blue": max(rgb["blue"]),
    }


def game_is_possible(rgb: dict, config: dict):
    """Return a boolean whether the game is possible for the configuration"""

    for color, counts in rgb.items():
        impossible = any(c > config[color] for c in counts)
        if impossible:
            return False

    return True


def main():
    print("Advent of code 02")

    filename = "input.txt"
    lines = read_file(filename)

    config = {"red": 12, "blue": 14, "green": 13}

    sum = 0
    power_sum = 0
    for line in lines:
        (game_id, rgb) = parse_line(line)
        if game_is_possible(rgb, config):
            sum += game_id

        min_config = find_min_config(rgb)
        power_sum += min_config["red"] * min_config["green"] * min_config["blue"]

    print(f"Sum of possible game ids: {sum}")
    print(f"Sum of min possible config powers (r*b*g): {power_sum}")


if __name__ == "__main__":
    main()
