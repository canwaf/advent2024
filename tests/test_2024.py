import sys
from pathlib import Path

import pytest

# Set the source directory to be one level up from the tests directory
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Import the function to be tested Day 6
from day6_solution import breadcrumb, guard_gallivant, orient, process_file, sneak_past


def test_2024_day6_part1():
    # Define the input file path
    input_file = Path(__file__).resolve().parent / "fixtures" / "2024_day6_input.txt"

    # Define the expected output
    expected_output = 41

    # Call the function and assert the result
    result = guard_gallivant(input_file)
    assert result == expected_output


def test_2024_day6_process_file():
    # Define the input file path
    input_file = Path(__file__).resolve().parent / "fixtures" / "2024_day6_input.txt"

    expected_output = """%%%%%%%%%%%%
%....#.....%
%.........#%
%..........%
%..#.......%
%.......#..%
%..........%
%.#..^.....%
%........#.%
%#.........%
%......#...%
%%%%%%%%%%%%"""

    result = process_file(input_file)
    assert result == expected_output


def test_2024_day6_orient():
    result = orient(
        """..v
#..
..#"""
    )

    assert (
        result
        == """>.#
...
.#."""
    )


def test_2024_day6_breadcrumb():
    result = breadcrumb("...>.....#")

    assert result == "...XXXXXv#"


def test_2024_day6_part2():
    # Define the input file path
    input_file = Path(__file__).resolve().parent / "fixtures" / "2024_day6_input.txt"

    # Define the expected output
    expected_output = 6

    # Call the function and assert the result
    result = sneak_past(input_file)
    assert result == expected_output


if __name__ == "__main__":
    pytest.main()
