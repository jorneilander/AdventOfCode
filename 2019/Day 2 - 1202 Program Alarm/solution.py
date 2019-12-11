from os import chdir

chdir("./2019/Day 2 - 1202 Program Alarm/")


def process_intcode(intcode, noun, verb):
    intcode = list(map(lambda x: int(x), intcode.split(",")))
    intcode[1] = noun
    intcode[2] = verb

    def inner(intcode, instruction_pointer=0):
        command = intcode[instruction_pointer:instruction_pointer+4]

        if command[0] == 99:
            return (intcode[0])

        if command[0] == 1:
            intcode[command[3]] = intcode[command[1]] + intcode[command[2]]
            return inner(intcode, instruction_pointer+4)
        if command[0] == 2:
            intcode[command[3]] = intcode[command[1]] * intcode[command[2]]
            return inner(intcode, instruction_pointer+4)

    return inner(intcode)


def traverse_intcode_parameters(intcode, max=100):
    unique_combinations = set(((x, y) for x in range(max) for y in range(max)))

    for combination in unique_combinations:
        noun = combination[0]
        verb = combination[1]
        yield (process_intcode(intcode, noun, verb), noun, verb)


with open("./input.txt", "r") as file:
    input = file.read()

print(process_intcode(input, 12, 2))

for output in traverse_intcode_parameters(input):
    if int(output[0]) == 19690720:
        print(100 * output[1] + output[2])
