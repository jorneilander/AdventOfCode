from typing import List, Tuple
from dataclasses import dataclass
import pathlib


@dataclass
class Step:
    direction: str
    distance: int


class Submarine:
    starting_position: Tuple[int, int] = (0, 0)
    position: Tuple[int, int] = (0, 0)
    path: List[Tuple[int, int]]
    aim: int = 0

    def get_position(self):
        return self.position

    def get_horizontal_position(self) -> int:
        return self.position[1]

    def get_vertical_position(self) -> int:
        return self.position[0]

    def set_course(self, input: List[str]) -> None:

        input_split: List[Step] = [
            Step(x.split(" ")[0], int(x.split(" ")[1])) for x in input
        ]
        for instruction in input_split:
            match instruction.direction:
              case "up":
                self.aim = self.aim + instruction.distance
              case "down":
                self.aim = self.aim - instruction.distance
              case "forward":
                self._move_horizontally(instruction.distance)
                self._move_vertically(instruction.distance * self.aim)

    def _move_horizontally(self, distance: int) -> None:
        new_position = (self.position[0] + distance, self.position[1])
        print(
            f"Moving horizontally from {self.position} to: {new_position} ({distance})"
        )
        self.position = new_position

    def _move_vertically(self, distance: int) -> None:
        new_position = (self.position[0], self.position[1] + distance)
        print(f"Moving vertically from {self.position} to: {new_position} ({distance})")
        self.position = new_position


if __name__ == "__main__":
    input_location = pathlib.Path(__file__).parent.resolve()

    with open(f"{input_location}/input.txt", "r") as file:
        input_raw: List[str] = file.readlines()
        input: List[str] = [x.replace("\n", "") for x in input_raw]

    submarine: Submarine = Submarine()
    submarine.set_course(input)

    # Answer part 1: 1480518
    # Answer part 2: 1282809906
    print(abs(submarine.get_horizontal_position() * submarine.get_vertical_position()))
