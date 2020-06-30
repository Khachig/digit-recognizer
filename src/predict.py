from PIL import Image

from files import MODELS


def get_pixel_data(image_file):
    im = Image.open(image_file)
    pixels = list(im.getdata())
    im.close()
    return pixels


def get_classifier(classifier):
    import joblib
    filename = MODELS[classifier]
    clf = joblib.load(filename)
    return clf


if __name__ == '__main__':
    from argparse import ArgumentParser
    import os

    class Parser(ArgumentParser):

        def print_help(self):
            message = """usage: train.py [-h] classifier

positional arguments:
  classifier  type of classifier

optional arguments:
  -h, --help  show this help message and exit

types of classifiers:
  decision_tree  DecisionTreeClassifier
  mlp            MLPClassifier
  svm            SVMClassifier
"""
            print(message)

    parser = Parser()
    parser.add_argument('classifier', type=str, help='type of classifier')
    parser.add_argument('-f', type=str, nargs='+',
                        help='path to image file(s)')
    args = parser.parse_args()

    pixel_data = []
    for img in args.f:
        if os.path.exists(img):
            pixels = get_pixel_data(img)
            pixel_data.append(pixels)
        else:
            print(f'No such file: {img}')

    classifier = get_classifier(args.classifier)
    predictions = classifier.predict(pixel_data)
    print('Recognized digits: ' +
          ' '.join([str(prediction) for prediction in predictions]))
