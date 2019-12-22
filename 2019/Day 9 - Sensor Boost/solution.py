from os import chdir
from collections import namedtuple

chdir("./2019/Day 9 - Sensor Boost/")


class CustomList(list):
    def __getitem__(self, key):
        try:
            return list.__getitem__(self, key)
        except IndexError:
            current_length = list.__len__(self)
            appended_list = [0 for x in range(key - (current_length - 1))]
            list.extend(self, appended_list)
            # print(f"Key is missing, length of list was: {current_length}, index requested {key}, size is now {list.__len__(self)}")
            return list.__getitem__(self, key)


class IntcodeComputer:
    def __init__(self, intcode: str, input: list = None):
        self.intcode: list[int] = CustomList(map(lambda x: int(x), intcode.strip().split(",")))
        self.input: list[int] = input
        self.instruction_pointer: int = 0
        self.input_pointer: int = 0
        self.relative_base: int = 0
        self.output: int = 0

    def get_next_output(self):
        while True:

            # print(f"Instruction pointer at {self.instruction_pointer}: {self.intcode[self.instruction_pointer]}")
            instruction = self._get_instruction()
            # print(instruction)

            if instruction.opcode == 99:
                # print(f"Opcode: {instruction.opcode}")
                return True

            elif instruction.opcode == 1:
                command = self.intcode[self.instruction_pointer:self.instruction_pointer + 4]
                # print(f"Opcode: {instruction.opcode}, command: {command}")
                param_one_value, param_two_value, param_three_value = self._get_values(instruction, command, 3)
                # print(f"Opcode: {instruction.opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")
                if instruction.third_param_mode == 2:
                    self.intcode[command[3] + self.relative_base] = param_one_value + param_two_value
                else:
                    self.intcode[command[3]] = param_one_value + param_two_value

                self.instruction_pointer = self.instruction_pointer + 4
                yield

            elif instruction.opcode == 2:
                command = self.intcode[self.instruction_pointer:self.instruction_pointer + 4]
                param_one_value, param_two_value, param_three_value = self._get_values(instruction, command, 3)
                # print(f"Opcode: {instruction.opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")
                if instruction.third_param_mode == 2:
                    self.intcode[command[3] + self.relative_base] = param_one_value * param_two_value
                else:
                    self.intcode[command[3]] = param_one_value * param_two_value

                self.instruction_pointer = self.instruction_pointer + 4
                yield

            elif instruction.opcode == 3:
                # Opcode 3 takes a single integer as input and saves it to the position given by its only parameter.
                # For example, the instruction 3,50 would take an input value and store it at address 50.
                command = self.intcode[self.instruction_pointer:self.instruction_pointer + 2]
                # print(f"Opcode: {instruction.opcode}, command: {command}")

                if instruction.first_param_mode == 2:
                    # print(f"Setting intcode[{command[1] + self.relative_base}] to {self.input[self.input_pointer]}")
                    self.intcode[command[1] + self.relative_base] = self.input[self.input_pointer]
                else:
                    # print(f"Setting intcode[{command[1]}] to {self.input[self.input_pointer]}")
                    self.intcode[command[1]] = self.input[self.input_pointer]

                self.input_pointer = self.input_pointer + 1
                self.instruction_pointer = self.instruction_pointer + 2
                yield

            elif instruction.opcode == 4:
                # Opcode 4 outputs the value of its only parameter.
                # For example, the instruction 4,50 would output the value at address 50.
                command = self.intcode[self.instruction_pointer:self.instruction_pointer + 2]
                # print(f"Opcode: {instruction.opcode}, command: {command}")

                param_one_value = self._get_values(instruction, command, 1)

                # if instruction.first_param_mode == 2:
                #     # print(f"Returning intcode[{self.intcode[command[1] + self.relative_base]}]: {self.intcode[command[1] + self.relative_base]}")
                #     self.instruction_pointer = self.instruction_pointer + 2
                #     return self.intcode[command[1] + self.relative_base]
                # else:
                # print(f"Returning {param_one_value}")
                self.instruction_pointer = self.instruction_pointer + 2
                yield param_one_value

            elif instruction.opcode == 5:
                # Opcode 5 is jump-if-true:
                # if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter.
                # Otherwise, it does nothing.
                command = self.intcode[self.instruction_pointer:self.instruction_pointer + 3]
                param_one_value, param_two_value = self._get_values(instruction, command, 2)
                # print(f"Opcode: {instruction.opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")

                self.instruction_pointer = param_two_value if param_one_value != 0 else self.instruction_pointer + 3
                # print(f"Set instruction_pointer to {self.instruction_pointer}")
                yield

            elif instruction.opcode == 6:
                # Opcode 6 is jump-if-false:
                # if the first parameter is zero, it sets the instruction pointer to the value from the second parameter.
                # Otherwise, it does nothing.
                command = self.intcode[self.instruction_pointer:self.instruction_pointer + 3]
                param_one_value, param_two_value = self._get_values(instruction, command, 2)
                # print(f"Opcode: {instruction.opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")
                self.instruction_pointer = param_two_value if param_one_value == 0 else self.instruction_pointer + 3
                # print(f"Set instruction_pointer to {self.instruction_pointer}")
                yield

            elif instruction.opcode == 7:
                # Opcode 7 is less than:
                # if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter.
                # Otherwise, it stores 0.
                command = self.intcode[self.instruction_pointer:self.instruction_pointer + 4]
                param_one_value, param_two_value, param_three_value = self._get_values(instruction, command, 3)
                # print(f"Opcode: {instruction.opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")

                if instruction.third_param_mode == 2:
                    self.intcode[command[3] + self.relative_base] = 1 if param_one_value < param_two_value else 0
                else:
                    self.intcode[command[3]] = 1 if param_one_value < param_two_value else 0

                self.instruction_pointer = self.instruction_pointer + 4
                yield

            elif instruction.opcode == 8:
                # Opcode 8 is equals:
                # if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter.
                # Otherwise, it stores 0.
                command = self.intcode[self.instruction_pointer:self.instruction_pointer + 4]
                param_one_value, param_two_value, param_three_value = self._get_values(instruction, command, 3)
                # print(f"Opcode: {instruction.opcode}, command: {command}, Param1: {param_one_value}, Param2: {param_two_value}")

                if instruction.third_param_mode == 2:
                    self.intcode[command[3] + self.relative_base] = 1 if param_one_value == param_two_value else 0
                    # print(f"Set intcode[{command[3] + self.relative_base}] to {self.intcode[command[3] + self.relative_base]}")
                else:
                    self.intcode[command[3]] = 1 if param_one_value == param_two_value else 0
                    # print(f"Set intcode[{command[3]}] to {self.intcode[command[3]]}")

                self.instruction_pointer = self.instruction_pointer + 4
                yield

            elif instruction.opcode == 9:
                # Opcode 9 adjusts the relative base by the value of its only parameter
                command = self.intcode[self.instruction_pointer:self.instruction_pointer + 2]
                param_one_value = self._get_values(instruction, command, 1)[0]
                # print(f"Opcode: {instruction.opcode}, command: {command}, Param1: {param_one_value}")
                # print(f"Setting relative_base to {self.relative_base + param_one_value}")
                self.relative_base = self.relative_base + param_one_value
                self.instruction_pointer = self.instruction_pointer + 2
                yield

    def _get_values(self, instruction, command: list, parameters: int):
        return_list = []
        param_list = command[1:parameters + 1]

        for x in range(parameters):
            if instruction[x + 1] == 0:
                return_list.append(self.intcode[param_list[x]])
            elif instruction[x + 1] == 1:
                return_list.append(param_list[x])
            elif instruction[x + 1] == 2:
                return_list.append(self.intcode[param_list[x] + self.relative_base])

        return return_list

    def _get_instruction(self):
        Instruction = namedtuple("Instruction", ["opcode", "first_param_mode", "second_param_mode", "third_param_mode"])

        instruction = f"{self.intcode[self.instruction_pointer]:05d}"
        opcode = int(instruction[3:])
        first_param_mode = int(instruction[2:3])
        second_param_mode = int(instruction[1:2])
        third_param_mode = int(instruction[0:1])
        return Instruction(opcode, first_param_mode, second_param_mode, third_param_mode)


with open("./input.txt", "r") as file:
    input = file.readline()

# input = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
# input = "1102,34915192,34915192,7,4,7,99,0" #should output a 16-digit number
# input = "104,1125899906842624,99" #should output the large number in the middle

intcode = IntcodeComputer(input, [2])
output = []
for x in intcode.get_next_output():
    if x is not None:
        output.append(x)
print(output)
