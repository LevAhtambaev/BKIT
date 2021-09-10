from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

from PIL import Image, ImageDraw, ImageFont


def get_picture(r, c, s):
    im = Image.new('RGB', (800, 400), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('C:/Users/hoppl/Downloads/ofont.ru_Times New Roman.ttf', size=20)
    scale = 50
    draw.rectangle((10, 10, 10 + scale * r.width, 10 + scale * r.height), fill='blue', outline=(0, 0, 0))
    draw.ellipse((200, 10, 200 + 2 * scale * c.r, 10 + 2 * scale * c.r), fill='green', outline=(0, 0, 0))
    draw.rectangle((500, 50, 500 + scale * s.width, 50 + scale * s.height), fill='red', outline=(0, 0, 0))
    draw.text((20, 250), 'Rectangle', font=font, fill='black')
    draw.text((270, 250), 'Ellipse', font=font, fill='black')
    draw.text((520, 250), 'Square', font=font, fill='black')

    im.show()


def main():
    variant = 2
    r = Rectangle("синего", variant, 4)
    c = Circle("зеленого", variant)
    s = Square("красного", variant)
    print(r)
    print(c)
    print(s)

    get_picture(r, c, s)


if __name__ == "__main__":
    main()
