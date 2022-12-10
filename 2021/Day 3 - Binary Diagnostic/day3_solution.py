import pathlib
from typing import List
from collections import Counter

import sys

print(sys.getrecursionlimit())

sys.path.append("./2021/Day 2 - Dive/")
import day2_solution


class Submarine(day2_solution.Submarine):
    diagnostic_report: List[str]

    def load_diagnostic_report(
        self, location: pathlib.Path = pathlib.Path(__file__).parent.resolve()
    ) -> None:

        with open(f"{location}/input.txt", "r") as file:
            input_raw: List[str] = file.readlines()
            self.diagnostic_report = [x.replace("\n", "") for x in input_raw]

    def get_gamma_rate(self) -> int:
        if self.diagnostic_report is None:
            self.load_diagnostic_report()

        input = self._seperate_digits(self.diagnostic_report)
        output: List[int] = []

        [output.append(str(Counter(x).most_common()[0][0])) for x in input]

        answer = int("".join(output), 2)
        print(f"Gamma rate: {answer}")
        return answer

    def get_epsilon_rate(self) -> int:
        if self.diagnostic_report is None:
            self.load_diagnostic_report()

        input = self._seperate_digits(self.diagnostic_report)

        output: List[int] = []

        [output.append(str(Counter(x).most_common()[-1][0])) for x in input]

        answer = int("".join(output), 2)
        print(f"Epsilon rate: {answer}")
        return answer

    def get_power_consumption(self) -> int:
        return self.get_gamma_rate() * self.get_epsilon_rate()

    # make this a generatable functions, only diff is which bit to choose and least amount
    def get_oxygen_generator_rating(self) -> int:
        if self.diagnostic_report is None:
            self.load_diagnostic_report()

        def _loop(
            position: int = 0,
            diagnostic_report_filtered: List[str] = self.diagnostic_report,
        ):

            bits_in_scope: List[str] = [x[position] for x in diagnostic_report_filtered]
            bit_count = Counter(bits_in_scope).most_common()

            if len(bit_count) > 1:
                most_common_bit = (
                    bit_count[0][0] if bit_count[0][1] != bit_count[1][1] else "1"
                )

            diagnostic_report_filtered = list(
                filter(
                    lambda x: x[position] == most_common_bit, diagnostic_report_filtered
                )
            )

            if len(diagnostic_report_filtered) == 1:
                oxygen_generator_rating = int(diagnostic_report_filtered[0], 2)
                print(f"Oxygen generator rating: {oxygen_generator_rating}")
                return oxygen_generator_rating
            else:
                return _loop(position + 1, diagnostic_report_filtered)

        return _loop()

    def get_co2_scrubber_rating(self) -> int:
        if self.diagnostic_report is None:
            self.load_diagnostic_report()

        def _loop(
            position: int = 0,
            diagnostic_report_filtered: List[str] = self.diagnostic_report,
        ):

            bits_in_scope: List[str] = [x[position] for x in diagnostic_report_filtered]
            bit_count = Counter(bits_in_scope).most_common()

            if len(bit_count) > 1:
                most_common_bit = (
                    bit_count[-1][0] if bit_count[0][1] != bit_count[1][1] else "0"
                )

            diagnostic_report_filtered = list(
                filter(
                    lambda x: x[position] == most_common_bit, diagnostic_report_filtered
                )
            )

            if len(diagnostic_report_filtered) == 1:
                oxygen_generator_rating = int(diagnostic_report_filtered[0], 2)
                print(f"Oxygen generator rating: {oxygen_generator_rating}")
                return oxygen_generator_rating
            else:
                return _loop(position + 1, diagnostic_report_filtered)

        return _loop()

    def get_life_support_rating(self) -> int:
        life_support_rating = (
            self.get_co2_scrubber_rating() * self.get_oxygen_generator_rating()
        )
        print(f"Life support rating: {life_support_rating}")
        return life_support_rating

    def _seperate_digits(self, input: List[str]) -> List[List[int]]:

        output: List[List[int]] = []

        for index in range(len(input[0])):
            output.append([])

        for row in input:
            for index, digit in enumerate(row):
                (output[index]).append(int(digit))

        return output


if __name__ == "__main__":
    submarine = Submarine()
    submarine.load_diagnostic_report()
    submarine.get_life_support_rating()
