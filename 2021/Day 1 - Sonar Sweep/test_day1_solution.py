from typing import List
from day1_solution import get_increments, get_sliding_window_increments

input: List[str] = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_increments():
    answer: int = 7

    assert get_increments(input) == answer


def test_sliding_window_increments():
    answer: int = 5

    assert get_sliding_window_increments(input) == answer
