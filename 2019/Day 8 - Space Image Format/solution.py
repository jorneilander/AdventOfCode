from os import chdir

chdir("./2019/Day 8 - Space Image Format/")


def chunks(text: str, size: int):
    text_pos: int = 0
    while text_pos < len(text) - 1:
        yield text[text_pos:text_pos + size]
        text_pos = text_pos + size


class Layer():
    def __init__(self, width: int, height: int, layer_code: str):
        self.layer_code: str = layer_code
        self.rows: list = [row for row in chunks(layer_code, width)]
        self.height: int = height
        self.width: int = width

    def __repr__(self):
        return self.layer_code


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
        self.final_image = Layer(self.width, self.height, "".join(self._render_image()))

    def _render_image(self):
        reversed_layers = reversed(self.layers)
        image_pixels: list = ["_" for x in range(self.layer_size)]

        for layer in reversed_layers:
            for x in range(self.layer_size):
                if layer.layer_code[x] == "0":
                    image_pixels[x] = "_"
                elif layer.layer_code[x] == "1":
                    image_pixels[x] = "8"
                elif layer.layer_code[x] == "2":
                    pass
        return image_pixels


with open("./input.txt", "r") as file:
    input = file.readline()

image = Image(25, 6, input)

for row in image.final_image.rows:
    print("".join(row))
