from os import chdir

chdir("./2019/Day 3 - Crossed Wires/")


class Wire():
    def __init__(self, path, start_coordinate=(0, 0)):
        self.path = path.split(",")
        self.start_coordinate = start_coordinate
        self.traversed_coordinates = []
        self._path_to_coordinates()

    def _path_to_coordinates(self):
        start_coordinate = self.start_coordinate
        self.traversed_coordinates.append(start_coordinate)
        for step in self.path:
            direction = step[0]
            distance = int(step[1:])

            if direction == "U":
                for i in range(distance):
                    self.traversed_coordinates.append(
                        (start_coordinate[0], start_coordinate[1] + (i + 1)))
                start_coordinate = (
                    start_coordinate[0], start_coordinate[1] + distance)
            if direction == "D":
                for i in range(distance):
                    self.traversed_coordinates.append(
                        (start_coordinate[0], start_coordinate[1] - (i + 1)))
                start_coordinate = (
                    start_coordinate[0], start_coordinate[1] - distance)
            if direction == "R":
                for i in range(distance):
                    self.traversed_coordinates.append(
                        (start_coordinate[0] + (i + 1), start_coordinate[1]))
                start_coordinate = (
                    start_coordinate[0] + distance, start_coordinate[1])
            if direction == "L":
                for i in range(distance):
                    self.traversed_coordinates.append(
                        (start_coordinate[0] - (i + 1), start_coordinate[1]))
                start_coordinate = (
                    start_coordinate[0] - distance, start_coordinate[1])


with open("./input.txt", "r") as file:
    input = file.readlines()

wire_first = Wire(input[0])
wire_second = Wire(input[1])

intersections = set(
    wire_first.traversed_coordinates) & set(
        wire_second.traversed_coordinates)
intersections.remove((0, 0))
lmdi = min(set(map(lambda x: abs(x[0]) + abs(x[1]), intersections)))

fsi = min(set(map(
    lambda x:
    wire_first.traversed_coordinates.index(x) +
    wire_second.traversed_coordinates.index(x),
    intersections)))

print(f"Manhattan distance for nearest intersection: {lmdi}")
print(f"Manhattan distance for intersection with the fewest steps: {fsi}")
