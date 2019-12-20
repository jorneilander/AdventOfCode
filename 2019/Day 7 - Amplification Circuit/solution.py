from os import chdir
from itertools import permutations

chdir("./2019/Day 7 - Amplification Circuit/")


class Amplifier:
    def __init__(self, intcode: str, phase_setting: int, input: int = None):
        self.intcode: list[int] = list(map(lambda x: int(x), intcode.split(",")))
        self.phase_setting: int = phase_setting
        self.input: list[int] = [self.phase_setting] if input is None else [self.phase_setting, input]
        self.instruction_pointer: int = 0
        self.input_pointer: int = 0
        self.output: int = 0

    def get_next_output(self):
        instruction = f"{self.intcode[self.instruction_pointer]:05d}"

        print(f"Instruction: {instruction}")

        opcode = int(instruction[3:])
        first_param_mode = int(instruction[2:3])
        second_param_mode = int(instruction[1:2])
        third_param_mode = int(instruction[0:1])  # noqa F841

        if opcode == 99:
            print(f"Opcode: {opcode}")
            raise Exception("Reached end of intcode")

        if opcode == 1:
            command = self.intcode[self.instruction_pointer:self.instruction_pointer + 4]

            param_one_value = self.intcode[command[1]] if first_param_mode == 0 else command[1]
            param_two_value = self.intcode[command[2]] if second_param_mode == 0 else command[2]
            # print(f"Opcode: {opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")
            self.intcode[command[3]] = param_one_value + param_two_value
            self.instruction_pointer = self.instruction_pointer + 4
            return self.get_next_output()

        if opcode == 2:
            command = self.intcode[self.instruction_pointer:self.instruction_pointer + 4]
            param_one_value = self.intcode[command[1]] if first_param_mode == 0 else command[1]
            param_two_value = self.intcode[command[2]] if second_param_mode == 0 else command[2]
            print(f"Opcode: {opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")
            self.intcode[command[3]] = param_one_value * param_two_value
            self.instruction_pointer = self.instruction_pointer + 4
            return self.get_next_output()

        if opcode == 3:
            command = self.intcode[self.instruction_pointer:self.instruction_pointer + 2]
            print(f"Opcode: {opcode}, command: {command}")
            self.intcode[command[1]] = self.input[self.input_pointer]
            self.input_pointer = self.input_pointer + 1
            self.instruction_pointer = self.instruction_pointer + 2
            return self.get_next_output()

        if opcode == 4:
            command = self.intcode[self.instruction_pointer:self.instruction_pointer + 2]
            param_one_value = self.intcode[command[1]] if first_param_mode == 0 else command[1]
            print(f"Opcode: {opcode}, command: {command}, Param1: {param_one_value}")

            self.instruction_pointer = self.instruction_pointer + 2
            return param_one_value

        if opcode == 5:
            command = self.intcode[self.instruction_pointer:self.instruction_pointer + 3]
            param_one_value = self.intcode[command[1]] if first_param_mode == 0 else command[1]
            param_two_value = self.intcode[command[2]] if second_param_mode == 0 else command[2]
            print(f"Opcode: {opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")
            self.instruction_pointer = param_two_value if param_one_value != 0 else self.instruction_pointer + 3
            return self.get_next_output()

        if opcode == 6:
            command = self.intcode[self.instruction_pointer:self.instruction_pointer + 3]
            param_one_value = self.intcode[command[1]] if first_param_mode == 0 else command[1]
            param_two_value = self.intcode[command[2]] if second_param_mode == 0 else command[2]
            print(f"Opcode: {opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")
            self.instruction_pointer = param_two_value if param_one_value == 0 else self.instruction_pointer + 3
            return self.get_next_output()

        if opcode == 7:
            command = self.intcode[self.instruction_pointer:self.instruction_pointer + 4]
            param_one_value = self.intcode[command[1]] if first_param_mode == 0 else command[1]
            param_two_value = self.intcode[command[2]] if second_param_mode == 0 else command[2]
            print(f"Opcode: {opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")
            self.intcode[command[3]] = 1 if param_one_value < param_two_value else 0
            self.instruction_pointer = self.instruction_pointer + 4
            return self.get_next_output()

        if opcode == 8:
            command = self.intcode[self.instruction_pointer:self.instruction_pointer + 4]
            param_one_value = self.intcode[command[1]] if first_param_mode == 0 else command[1]
            param_two_value = self.intcode[command[2]] if second_param_mode == 0 else command[2]

            self.intcode[command[3]] = 1 if param_one_value == param_two_value else 0
            self.instruction_pointer = self.instruction_pointer + 4
            return self.get_next_output()


def combined_thruster_output(intcode: str, phase_settings: tuple):
    print(f"Trying: {phase_settings}")
    amplifiers: list[Amplifier] = [Amplifier(intcode, phase_setting) for phase_setting in phase_settings]
    amplifiers_pointer: int = 0
    output: int = 0

    try:
        while True:
            amplifiers[amplifiers_pointer].input.append(output)
            output = amplifiers[amplifiers_pointer].get_next_output()
            amplifiers_pointer = 0 if amplifiers_pointer == len(phase_settings) - 1 else amplifiers_pointer + 1
    except Exception:
        print(f"Output: {output}")
        return output


with open("./input.txt", "r") as file:
    input = file.readline()

all_combinations = permutations(range(5, 10))

output = list((combined_thruster_output(input, combination)) for combination in all_combinations)
print(max(output))
