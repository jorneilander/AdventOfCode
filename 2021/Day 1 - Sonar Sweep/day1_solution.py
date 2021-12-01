from os import chdir
from typing import List


def get_increments(input: List[int]) -> int:
    increments: int = 0

    for x in range(len(input)):
        if x > 0:
            if input[x] > input[x - 1]:
                increments = increments + 1

    return increments


def get_sliding_window_increments(input: List[int]) -> int:
    increments: int = 0
    sliding_windows: List[tuple[int, int, int]] = [
        (input[x], input[x + 1], input[x + 2]) for x in range(len(input) - 2)
    ]

    sliding_windows_sums: List[int] = [
        sum(sliding_window) for sliding_window in sliding_windows
    ]

    for x in range(len(sliding_windows_sums)):
        if x > 0:
            if sliding_windows_sums[x] > sliding_windows_sums[x - 1]:
                increments = increments + 1

    return increments


chdir("./2021/Day 1 - Sonar Sweep")

with open("./input.txt", "r") as file:
    input: List[str] = file.readlines()

input_sanitized: List[int] = [int(x.replace("\n", "")) for x in input]


# Answer day 1 - part 1
increments: int = get_increments(input_sanitized)
print(f"Amount of increments: {increments}")

# Answer day 1 - part 2
increments_sliding_window: int = get_sliding_window_increments(input_sanitized)
print(f"Increments in sliding window: {increments_sliding_window}")
