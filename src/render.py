from PIL import Image, ImageDraw

from parse import ImageParser
from files import TEST_IMAGES


def render(num, filepath, destination='.'):
    # Create a new 28x28 image in L mode (1-dimensional pixels)
    x, y = 28, 28
    image = Image.new('L', (x, y))

    # Create an ImageDraw object to draw pixels on the image
    draw = ImageDraw.ImageDraw(image)

    im_parser = ImageParser(filepath)
    images = im_parser.parse()

    for n in range(num):
        im = next(images)
        for i in range(len(im)):
            row = i // x
            col = i % y
            draw.point((col, row), fill=(im[i],))
        image.save(os.path.join(destination, f'image_{n+1}.png'))


if __name__ == '__main__':
    import argparse
    import os

    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int, help='number of images to render')
    parser.add_argument('-d', type=str, help='<OPTIONAL> output destination')
    args = parser.parse_args()

    if args.d:
        if os.path.isdir(args.d):
            render(args.number, TEST_IMAGES, args.d)
        else:
            print(f'No such directory: {args.d}')
    else:
        render(args.number, TEST_IMAGES)
