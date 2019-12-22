from os import chdir
from collections import namedtuple

chdir("./2019/Day 10 - Monitoring Station/")

Asteroid = namedtuple("Asteroid", ["x", "y"])


class Map():
    def __init__(self, input: list):
        self.input = reversed(input)
        for x in self.input:
            print(x)
        self.height = len(input)
        self.width = len(input[0])
        self.max_x = self.width - 1
        self.max_y = self.height - 1
        self.asteroids = [Asteroid(x, y) for y in range(self.height) for x in range(self.width) if input[y][x] == "#"]
        self.potential_stations = [MonitoringStation(self, asteroid.x, asteroid.y) for asteroid in self.asteroids]

    def __repr__(self):
        return " ".join([f"{x[0],x[1]}" for x in self.asteroids])


class MonitoringStation():
    def __init__(self, map: Map, x: int, y: int):
        self.map = map
        self.x = x
        self.y = y
        self.seen_coords = [(x, y) for x in range(self.map.width) for y in range(self.map.height)]
        self.seen_asteroids: list[Asteroid] = self.map.asteroids.copy()
        self._calc_diff()

    def _calc_diff(self):
        # We can't see ourselves
        self.seen_coords.remove((self.x, self.y))
        self.seen_asteroids.remove((self.x, self.y))
        for asteroid in self.seen_asteroids:
            x_diff = asteroid.x - self.x
            y_diff = asteroid.y - self.y
            self._remove_hidden_coords(asteroid, x_diff, y_diff)

    def _remove_hidden_coords(self, start: Asteroid, x_step: int, y_step: int):
        print(f"I'm: {(self.x, self.y)}, Asteroid: {start}, x_step: {x_step}, y_step: {y_step}")
        x_pos = start.x
        y_pos = start.y
        # First the easy scenario's
        if y_step == 0:  # we stay on the x-axis
            if x_step < 0:  # we are to the left of our current position
                x_pos = x_pos - 1

                while x_pos >= 0:
                    print(f"Removing {(x_pos,y_pos)}")
                    if (x_pos, y_pos) in self.seen_coords:
                        self.seen_coords.remove((x_pos, y_pos))
                    x_pos = x_pos - 1
            else:  # we are to the right of our current position
                x_pos = x_pos + 1

                while x_pos < self.map.width:
                    print(f"Removing {(x_pos,y_pos)}")
                    if (x_pos, y_pos) in self.seen_coords:
                        self.seen_coords.remove((x_pos, y_pos))
                    x_pos = x_pos + 1

        elif x_step == 0:
            if y_step < 0:  # we are to the bottom of our current position
                y_pos = y_pos - 1

                while y_pos >= 0:
                    print(f"Removing {(x_pos,y_pos)}")
                    if (x_pos, y_pos) in self.seen_coords:
                        self.seen_coords.remove((x_pos, y_pos))
                    y_pos = y_pos - 1
            else:  # we are to the bottom of our current position
                y_pos = y_pos + 1

                while y_pos < self.map.height:
                    print(f"Removing {(x_pos,y_pos)}")
                    if (x_pos, y_pos) in self.seen_coords:
                        self.seen_coords.remove((x_pos, y_pos))
                    y_pos = y_pos + 1

        # x_pos = start.x + x_step
        # y_pos = start.y + y_step
        # while x_pos < self.map.width and y_pos < self.map.height:
        #     if x_step == 0:
        #         self.seen_coords.remove((x_pos, y_pos))
        #     print(f"Removing: {(x_pos, y_pos)}")
        #     self.seen_coords.remove((x_pos, y_pos))
        #     x_pos += x_step
        #     y_pos += y_step










with open("./example_maps/1.txt", "r") as file:
    input = file.readlines()
    input = list(map(lambda x: x.strip(), input))

map = Map(input)
print(map)

# Example 1: Best is 3,4 with 8 other asteroids detected
# Example 2: Best is 5,8 with 33 other asteroids detected
# Example 3: Best is 1,2 with 35 other asteroids detected
# Example 4: Best is 6,3 with 41 other asteroids detected:
# Example 5: Best is 11,13 with 210 other asteroids detected

# #.........
# ...A......
# ...B..a...
# .EDCG....a
# ..F.c.b...
# .....c....
# ..efd.c.gb
# .......c..
# ....f...c.
# ...e..d..c