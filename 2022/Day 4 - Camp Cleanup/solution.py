import pathlib
from typing import List, Tuple


def calculate_list_overlap(
    list1: List[int], list2: List[int]
) -> Tuple[List[int], bool]:
    """Compares two lists of integers for overlap

    Args:
        list1 (List[int]): First list used in the comparison
        list2 (List[int]): Second list used in the comparison

    Returns:
        Tuple[List[int], bool]: list of overlapping integers, boolean indicating full overlap
    """

    if len(list1) == 0 or len(list2) == 0:
        return tuple(0, False)

    list_smallest: List[int] = list1 if len(list1) < len(list2) else list2
    list_largest: List[int] = list2 if len(list2) > len(list1) else list1

    list_overlap: List[bool] = [
        element for element in list_smallest if element in list_largest
    ]

    return list_overlap, len(list_smallest) == len(list_overlap)


location = pathlib.Path = pathlib.Path(__file__).parent.resolve()

with open(f"{location}/input.txt", "r") as file:
    input: List[str] = file.readlines()
input_sanitized: List[str] = [x.replace("\n", "") for x in input]


pairs_overlap_amount: int = 0
pairs_overlap_full_amount: int = 0

for line in input_sanitized:
    elf1_sections_input, elf2_sections_input = line.split(",")
    elf1_sections = list(
        range(
            int(elf1_sections_input.split("-")[0]),
            int(elf1_sections_input.split("-")[1]) + 1,
        )
    )
    elf2_sections = list(
        range(
            int(elf2_sections_input.split("-")[0]),
            int(elf2_sections_input.split("-")[1]) + 1,
        )
    )
    overlap, full_overlap = calculate_list_overlap(elf1_sections, elf2_sections)

    if full_overlap:
        pairs_overlap_amount += 1
        pairs_overlap_full_amount += 1
        continue
    if overlap:
        pairs_overlap_amount += 1


print(
    f"Overlapping pairs: {pairs_overlap_amount}, of which fully overlapping: {pairs_overlap_full_amount}"
)
