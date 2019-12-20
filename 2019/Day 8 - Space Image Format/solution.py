from os import chdir
import operator

chdir("./2019/Day 8 - Space Image Format/")


def chunks(text: str, size: int):
    text_pos = 0
    while text_pos < len(text) - 1:
        yield text[text_pos:text_pos + size - 1]
        text_pos = text_pos + size


class Layer():
    def __init__(self, width: int, height: int, layer_code: str):
        self.layer_code: str = layer_code
        self.rows: list = [x for x in chunks(layer_code, width)]
        self.height: int = height
        self.width: int = width


class Image():
    def __init__(self, width: int, height: int, spi_encoded_image: str):
        self.width: int = width
        self.height: int = height
        self.spi_encoded_image: str = spi_encoded_image.strip()
        self.layer_size: int = self.width * self.height
        self.layers: list[Layer] = [
            Layer(self.width, self.height, layer_code)
            for layer_code in chunks(spi_encoded_image, self.layer_size)
        ]


with open("./input.txt", "r") as file:
    input = file.readline()

print(f"Lenght of input: {len(input)}")
image = Image(25, 6, input)

layers_with_0_count = [(layer.layer_code.count("0"), image.layers.index(layer)) for layer in image.layers]
layer_with_least_0_count = image.layers[(min(layers_with_0_count, key=operator.itemgetter(0))[1])]
ones = layer_with_least_0_count.layer_code.count("1")
twos = layer_with_least_0_count.layer_code.count("2")

print(ones * twos)