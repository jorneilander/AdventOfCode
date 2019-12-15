from os import chdir

chdir("./2019/Day 6 - Universal Orbit Map/")

with open("./input.txt", "r") as file:
    input = file.readlines()


orbits_list = list(map(lambda x: x.rstrip().split(")"), input))
orbits_dict = {
    orbiting_station: orbited_station
    for orbited_station, orbiting_station
    in orbits_list}


def parse_orbits_dict(orbits_dict):
    total = 0
    routes = []

    def inner(one, two, route, acc=0):
        route.append(two)
        orbited_station = orbits_dict.get(two)
        if orbited_station is not None:
            return inner(two, orbited_station, route, acc + 1)
        return acc + 1, route

    for k, v in orbits_dict.items():
        x = inner(k, v, [k])
        total = total + x[0]
        routes.append(x[1])

    return total, routes


all_orbits, all_routes = parse_orbits_dict(orbits_dict)

applicable_routes_you = [x for x in all_routes if x[0] == "YOU"][0]
applicable_routes_san = [x for x in all_routes if x[0] == "SAN"][0]

shared_stations_on_applicable_routes = [
    station_you
    for station_you in applicable_routes_you
    for station_san in applicable_routes_san
    if station_you == station_san]

steps = [
        applicable_routes_san.index(station) - 1 +
        applicable_routes_you.index(station) - 1
        for station in shared_stations_on_applicable_routes
]

print(min(steps))
