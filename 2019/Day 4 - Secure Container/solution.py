from os import chdir

chdir("./2019/Day 4 - Secure Container/")


def valid_password(input):
    combinations_of_two = [(input[x], input[x+1]) for x in range(5)]

    increase_rule = set(filter(lambda x: x[0] > x[1], combinations_of_two))
    if len(increase_rule) > 0:
        return False

    adjacent_rule = list(filter(
        lambda x: x[0] == x[1] and
        input.count(x[0]) < 3,
        combinations_of_two))
    if len(adjacent_rule) == 0:
        return False

    return True


input = set(range(172930, 683082 + 1))
result = len(list(filter(lambda x: valid_password(str(x)), input)))

print(result)
