import math
import sys

from PIL import Image


class Size:
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


class Color:
    def __init__(self, r: int, g: int, b: int):
        self.__r = r
        self.__g = g
        self.__b = b
        self.__rgb = [r, g, b]

    @property
    def r(self) -> int:
        return self.__r

    @property
    def g(self) -> int:
        return self.__g

    @property
    def b(self) -> int:
        return self.__b

    @property
    def rgb(self) -> list:
        return [self.__r, self.__g, self.__b]


def wallpaper(size: Size, inner: Color, outer: Color):
    image = Image.new('RGB', size.xy)  # Create the image
    for y in range(size.y):
        for x in range(size.x):
            # Find the distance to the center
            center = math.sqrt((x - size.x/2) ** 2 + (y - size.y/2) ** 2)
            # Make it on a scale from 0 to 1
            center = float(center) / (math.sqrt(2) * size.x/2)
            # Calculate r, g, and b values
            r = outer.r * center + \
                inner.r * (1 - center)
            g = outer.g * center + \
                inner.g * (1 - center)
            b = outer.b * center + \
                inner.b * (1 - center)
            # Place the pixel
            image.putpixel((x, y), (int(r), int(g), int(b)))
    return image


if __name__ == '__main__':
    output = './wallpaper.jpg'
    if len(sys.argv) > 1 and sys.argv[1]:
        output = sys.argv[1]
    image = wallpaper(Size(800, 600), Color(0, 0, 0), Color(34, 34, 34))
    image.save(output)
