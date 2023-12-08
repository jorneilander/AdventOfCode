import pathlib
import sys
from loguru import logger

logger.remove()
logger.add(sys.stderr, level="INFO")

location = pathlib.Path = pathlib.Path(__file__).parent.resolve()

with open(f"{location}/input.txt", "r") as file:
    input: list[str] = file.readlines()
input_sanitized: list[str] = [x.replace("\n", "") for x in input]

logger.debug(input_sanitized)

integer_map = {
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


def get_first_number(
    input: str, reverse_input_enabled: bool = False, string_search_enabled: bool = True
) -> int:
    """Searches string for the first numeric value

    Args:
        input (str): Input string to process
        reverse_input_enabled (bool, optional): Reverse input string. Defaults to False.
        string_search_enabled (bool, optional): Search for numeric values as strings (e.g., 1 = one). Defaults to True.

    Returns:
        int: First numeric value found
    """

    integer_strings = [x for x in integer_map.keys()]
    if reverse_input_enabled:
        input = input[::-1]
        integer_strings = [x[::-1] for x in integer_map.keys()]

    for index, character in enumerate(input):
        if character.isdigit():
            return int(character)
        elif string_search_enabled:
            for integer_string in integer_strings:
                if input[index : (index + len(integer_string))] == integer_string:
                    if reverse_input_enabled:
                        return int(integer_map[integer_string[::-1]])
                    else:
                        return int(integer_map[integer_string])


# Part one
calibration_values = []
for input in input_sanitized:
    calibration_value = (
        f"{get_first_number(input, False, False)}{get_first_number(input, True, False)}"
    )
    logger.debug(f"{input}: {calibration_value}")
    calibration_values.append(int(calibration_value))

logger.info(f"Sum - Part 1: {sum(calibration_values)}")

# Part two
calibration_values = []
for input in input_sanitized:
    calibration_value = f"{get_first_number(input)}{get_first_number(input, True)}"
    logger.debug(f"{input}: {calibration_value}")
    calibration_values.append(int(calibration_value))

logger.info(f"Sum - Part 2: {sum(calibration_values)}")
