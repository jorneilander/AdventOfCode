from os import chdir

chdir("./2019/Day 5 - Sunny with a Chance of Asteroids/")


def process_intcode(intcode, input=None):
    intcode = list(map(lambda x: int(x), intcode.split(",")))

    def inner(intcode, instruction_pointer=0):
        instruction = f"{intcode[instruction_pointer]:05d}"

        print(f"Instruction: {instruction}")

        opcode = int(instruction[3:])
        first_param_mode = int(instruction[2:3])
        second_param_mode = int(instruction[1:2])
        third_param_mode = int(instruction[0:1])

        if opcode == 99:
            return (intcode[0])

        if opcode == 1:
            command = intcode[instruction_pointer:instruction_pointer + 4]

            param_one_value = intcode[command[1]] if first_param_mode == 0 else command[1]
            param_two_value = intcode[command[2]] if second_param_mode == 0 else command[2]
            print(f"Opcode: {opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")
            intcode[command[3]] = param_one_value + param_two_value
            return inner(intcode, instruction_pointer + 4)

        if opcode == 2:
            command = intcode[instruction_pointer:instruction_pointer + 4]
            param_one_value = intcode[command[1]] if first_param_mode == 0 else command[1]
            param_two_value = intcode[command[2]] if second_param_mode == 0 else command[2]
            print(f"Opcode: {opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")
            intcode[command[3]] = param_one_value * param_two_value
            return inner(intcode, instruction_pointer+4)

        if opcode == 3:
            command = intcode[instruction_pointer:instruction_pointer + 2]
            print(f"Opcode: {opcode}, command: {command}")
            intcode[command[1]] = input
            return inner(intcode, instruction_pointer+2)

        if opcode == 4:
            command = intcode[instruction_pointer:instruction_pointer + 2]
            param_one_value = intcode[command[1]] if first_param_mode == 0 else command[1]
            print(f"Opcode: {opcode}, command: {command}, Param1: {param_one_value}")
            print(param_one_value)
            return inner(intcode, instruction_pointer+2)

        if opcode == 5:
            command = intcode[instruction_pointer:instruction_pointer + 3]
            param_one_value = intcode[command[1]] if first_param_mode == 0 else command[1]
            param_two_value = intcode[command[2]] if second_param_mode == 0 else command[2]
            print(f"Opcode: {opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")

            if param_one_value != 0:
                return inner(intcode, param_two_value)
            return inner(intcode, instruction_pointer+3)

        if opcode == 6:
            command = intcode[instruction_pointer:instruction_pointer + 3]
            param_one_value = intcode[command[1]] if first_param_mode == 0 else command[1]
            param_two_value = intcode[command[2]] if second_param_mode == 0 else command[2]
            print(f"Opcode: {opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")

            if param_one_value == 0:
                return inner(intcode, param_two_value)
            return inner(intcode, instruction_pointer+3)

        if opcode == 7:
            command = intcode[instruction_pointer:instruction_pointer + 4]
            param_one_value = intcode[command[1]] if first_param_mode == 0 else command[1]
            param_two_value = intcode[command[2]] if second_param_mode == 0 else command[2]

            intcode[command[3]] = 1 if param_one_value < param_two_value else 0
            return inner(intcode, instruction_pointer+4)

        if opcode == 8:
            command = intcode[instruction_pointer:instruction_pointer + 4]
            param_one_value = intcode[command[1]] if first_param_mode == 0 else command[1]
            param_two_value = intcode[command[2]] if second_param_mode == 0 else command[2]

            intcode[command[3]] = 1 if param_one_value == param_two_value else 0
            return inner(intcode, instruction_pointer+4)

    return inner(intcode)

with open("./input.txt", "r") as file:
    input = file.readline()

process_intcode(input, input=5)