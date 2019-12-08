import math
import sys

from PIL import Image


class imgSize:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y
        self.__xy = (x, y)

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def xy(self) -> tuple:
        return (self.__x, self.__y)


def main(output: str, size: imgSize):
    image = Image.new('RGB', size.xy)  # Create the image
    innerColor = [80, 80, 255]  # Color at the center
    outerColor = [0, 0, 80]  # Color at the corners
    for y in range(size.y):
        for x in range(size.x):
            # Find the distance to the center
            distanceToCenter = math.sqrt(
                (x - size.x/2) ** 2 + (y - size.y/2) ** 2)
            # Make it on a scale from 0 to 1
            distanceToCenter = float(distanceToCenter) / \
                (math.sqrt(2) * size.x/2)
            # Calculate r, g, and b values
            r = outerColor[0] * distanceToCenter + \
                innerColor[0] * (1 - distanceToCenter)
            g = outerColor[1] * distanceToCenter + \
                innerColor[1] * (1 - distanceToCenter)
            b = outerColor[2] * distanceToCenter + \
                innerColor[2] * (1 - distanceToCenter)
            # Place the pixel
            image.putpixel((x, y), (int(r), int(g), int(b)))
    image.save(output)
    print('output>', output)


if __name__ == '__main__':
    main(sys.argv[1], imgSize(800, 600))
