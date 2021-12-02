from typing import List
from day2_solution import Submarine


input: List[str] = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def test_set_course():
    answer: int = 900

    submarine = Submarine()
    submarine.set_course(input)

    assert (
        abs(submarine.get_horizontal_position() * submarine.get_vertical_position())
        == answer
    )
