from pathlib import Path

import click


def process_file(input: Path) -> str:

    with input.open("r") as file:
        lines = file.readlines()

    max_length = max(len(line) for line in lines)
    border = "%" * (max_length + 1)

    result = border + "\n"
    for line in lines:
        result += f"%{line.strip()}%\n"
    result += border

    return result


def orient(input: str) -> str:

    rotations = {">": 0, "^": 1, "<": 2, "v": 3}
    rotation_count = next((rotations[char] for char in rotations if char in input), 0)
    for char in rotations:
        if char in input:
            input = input.replace(char, ">")
            break

    # print(f"Rotations required is {rotation_count}")

    if rotation_count == 0:
        return input

    lines = input.split("\n")
    n = len(lines)
    m = len(lines[0]) if n > 0 else 0

    rotated = [[""] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            if rotation_count == 1:
                rotated[j][n - 1 - i] = lines[i][j]
            elif rotation_count == 2:
                rotated[n - 1 - i][m - 1 - j] = lines[i][j]
            elif rotation_count == 3:
                rotated[m - 1 - j][i] = lines[i][j]

    rotated_string = "\n".join("".join(row) for row in rotated)
    return rotated_string


def breadcrumb(input: str) -> str:
    flat = list(input)
    i = flat.index(">")

    while flat[i] not in ["#", "%"]:
        flat[i] = "X"
        i += 1

    if flat[i] == "%":
        flat[i] = "!"
    elif flat[i] == "#":
        flat[i - 1] = "v"
    else:
        raise ValueError("Unexpected while loop termination.")

    return "".join(flat)


def guard_gallivant(input: Path) -> int:
    if not input.is_file():
        raise ValueError(f"The provided path {input} is not a file.")

    map = process_file(input)

    while "!" not in map:
        map = orient(map)
        map = breadcrumb(map)

    x_count = map.count("X")
    return x_count


def sneak_past(input: Path) -> int:
    if not input.is_file():
        raise ValueError(f"The provided path {input} is not a file.")

    map = process_file(input)

    loops = 0

    for i in range(len(map)):
        trial = process_file(input)
        trial = orient(trial)
        if trial[i] not in [">", "\n", "%", "#", "v", ">", "<"]:
            turn_count = 1

            trial = trial[:i] + "#" + trial[i + 1 :]

            while turn_count != 4 and "!" not in trial:
                try:
                    next_hash = trial.index("#", trial.index(">"))
                except ValueError:
                    # It escaped!
                    continue

                if "." not in trial[trial.index(">") : next_hash]:
                    turn_count += 1
                else:
                    turn_count = 1

                trial = breadcrumb(trial)
                trial = orient(trial)
                

        else:
            continue
        if "!" not in trial:
            loops += 1
    return loops


@click.command()
@click.argument("input_file", type=click.Path(exists=True, path_type=Path))
def main(input_file):
    result = guard_gallivant(input_file)
    print(f"Guard Gallivant Part 1: {result}")
    result = sneak_past(input_file)
    print(f"Guard Gallivant Part 2: {result}")


if __name__ == "__main__":
    main()
