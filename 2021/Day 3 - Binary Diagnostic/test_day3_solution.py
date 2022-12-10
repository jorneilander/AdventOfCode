from day3_solution import Submarine

input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

submarine = Submarine()
submarine.diagnostic_report = input


def test_seperate_digits():
    answer = [
        [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0],
    ]

    assert submarine._seperate_digits(input) == answer


def test_get_gamma_rate() -> None:
    answer_decimal: int = 22

    assert submarine.get_gamma_rate() == answer_decimal


def test_get_epsilon_rate() -> None:
    answer_decimal: int = 9

    assert submarine.get_epsilon_rate() == answer_decimal


def test_get_power_consumption() -> None:
    answer = 198

    assert submarine.get_power_consumption() == answer


def test_get_oxygen_generator_rating() -> None:
    answer = 23

    assert submarine.get_oxygen_generator_rating() == answer


def test_get_co2_scrubber_rating() -> None:
    answer = 10

    assert submarine.get_co2_scrubber_rating() == answer


def test_get_life_support_rating() -> None:
    answer = 230

    assert submarine.get_life_support_rating() == answer
