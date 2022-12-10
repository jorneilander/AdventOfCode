from typing import List
import pathlib


class BingoCard:
    number_grid: List[List[int]]


class Bingo:
    drawn_numbers: List[int]
    game_generator_input: List[str]
    bingo_cards: List[BingoCard] = []

    def load_game_generator_input(
        self, location: pathlib.Path = pathlib.Path(__file__).parent.resolve()
    ) -> None:
        with open(f"{location}/input.txt", "r") as file:
            input_raw: List[str] = file.readlines()
            self.game_generator_input = [x.replace("\n", "") for x in input_raw]

    def load_drawn_numbers(self) -> None:
        if self.game_generator_input is None:
            self.load_game_generator_input()

        self.drawn_numbers = [int(x) for x in self.game_generator_input[0].split(",")]

    def load_bingo_cards(self) -> None:
        if self.game_generator_input is None:
            self.load_game_generator_input()

        bingo_cards_input_raw = self.game_generator_input[2:]
        bingo_cards_input = [line for line in bingo_cards_input_raw if line != ""]
        bingo_cards_amount = int(len(bingo_cards_input) / 5)

        for card_number in range(bingo_cards_amount):
            bingo_card = BingoCard()
            starting_point = card_number * 4
            bingo_card_numbers = bingo_cards_input[starting_point : starting_point + 5]
            bingo_card.number_grid = [
                list(filter(None, x.replace("  ", " ").split(" ")))
                for x in bingo_card_numbers
            ]

            self.bingo_cards.append(bingo_card)
            print(f"Added bingo card: {bingo_card.number_grid}")


if __name__ == "__main__":
    bingo = Bingo()
    bingo.load_game_generator_input()
    bingo.load_bingo_cards()
