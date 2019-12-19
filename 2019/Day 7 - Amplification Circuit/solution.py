from os import chdir
from itertools import permutations

chdir("./2019/Day 7 - Amplification Circuit/")


def process_intcode(intcode, input_param_one=None, input_param_two=None):
    mutable_intcode = list(map(lambda x: int(x), intcode.split(","))).copy()

    def inner(inner_intcode, instruction_pointer=0):
        instruction = f"{inner_intcode.copy()[instruction_pointer]:05d}"

        print(f"Instruction: {instruction}")

        opcode = int(instruction[3:])
        first_param_mode = int(instruction[2:3])
        second_param_mode = int(instruction[1:2])
        third_param_mode = int(instruction[0:1])

        try:
            if opcode == 99:
                return inner.return_output

            if opcode == 1:
                command = inner_intcode[instruction_pointer:instruction_pointer + 4]

                param_one_value = inner_intcode[command[1]] if first_param_mode == 0 else command[1]
                param_two_value = inner_intcode[command[2]] if second_param_mode == 0 else command[2]
                print(f"Opcode: {opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")
                inner_intcode[command[3]] = param_one_value + param_two_value
                return inner(inner_intcode, instruction_pointer + 4)

            if opcode == 2:
                command = inner_intcode[instruction_pointer:instruction_pointer + 4]
                param_one_value = inner_intcode[command[1]] if first_param_mode == 0 else command[1]
                param_two_value = inner_intcode[command[2]] if second_param_mode == 0 else command[2]
                print(f"Opcode: {opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")
                inner_intcode[command[3]] = param_one_value * param_two_value
                return inner(inner_intcode, instruction_pointer+4)

            if opcode == 3:
                command = inner_intcode[instruction_pointer:instruction_pointer + 2]
                print(f"Opcode: {opcode}, command: {command}")
                inner_intcode[command[1]] = input_param_one if inner.input_param_pos == 0 else input_param_two
                inner.input_param_pos += 1
                return inner(inner_intcode, instruction_pointer+2)

            if opcode == 4:
                command = inner_intcode[instruction_pointer:instruction_pointer + 2]
                param_one_value = inner_intcode[command[1]] if first_param_mode == 0 else command[1]
                print(f"Opcode: {opcode}, command: {command}, Param1: {param_one_value}")
                inner.return_output = param_one_value
                return inner(inner_intcode, instruction_pointer+2)

            if opcode == 5:
                command = inner_intcode[instruction_pointer:instruction_pointer + 3]
                param_one_value = inner_intcode[command[1]] if first_param_mode == 0 else command[1]
                param_two_value = inner_intcode[command[2]] if second_param_mode == 0 else command[2]
                print(f"Opcode: {opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")

                if param_one_value != 0:
                    return inner(inner_intcode, param_two_value)
                return inner(inner_intcode, instruction_pointer+3)

            if opcode == 6:
                command = inner_intcode[instruction_pointer:instruction_pointer + 3]
                param_one_value = inner_intcode[command[1]] if first_param_mode == 0 else command[1]
                param_two_value = inner_intcode[command[2]] if second_param_mode == 0 else command[2]
                print(f"Opcode: {opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")

                if param_one_value == 0:
                    return inner(inner_intcode, param_two_value)
                return inner(inner_intcode, instruction_pointer+3)

            if opcode == 7:
                command = inner_intcode[instruction_pointer:instruction_pointer + 4]
                param_one_value = inner_intcode[command[1]] if first_param_mode == 0 else command[1]
                param_two_value = inner_intcode[command[2]] if second_param_mode == 0 else command[2]
                print(f"Opcode: {opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")
                inner_intcode[command[3]] = 1 if param_one_value < param_two_value else 0
                return inner(inner_intcode, instruction_pointer+4)

            if opcode == 8:
                command = inner_intcode[instruction_pointer:instruction_pointer + 4]
                param_one_value = inner_intcode[command[1]] if first_param_mode == 0 else command[1]
                param_two_value = inner_intcode[command[2]] if second_param_mode == 0 else command[2]

                inner_intcode[command[3]] = 1 if param_one_value == param_two_value else 0
                return inner(inner_intcode, instruction_pointer+4)
        except:
            return None

    inner.return_output = 0
    inner.input_param_pos = 0
    return inner(mutable_intcode)


def combined_thruster_output(intcode: str, phase_settings: tuple):
    output = 0
    for phase_setting in phase_settings:
        output = process_intcode(intcode, input_param_one=phase_setting, input_param_two=output)
    return int(output)



with open("./input.txt", "r") as file:
    input = file.readline()

# input = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"

all_combinations = permutations(range(5))

print(max((list((combined_thruster_output(input, combination)) for combination in all_combinations))))
