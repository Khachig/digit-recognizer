from classifier import DecisionTreeClassifier, SVMClassifier, save_model
from parse import ImageParser, LabelParser

from files import TRAINING_IMAGES, TRAINING_LABELS, TEST_IMAGES, TEST_LABELS


def get_data(image_file, label_file):
    im_parser = ImageParser(image_file)
    lb_parser = LabelParser(label_file)
    images, labels = im_parser.parse(), lb_parser.parse()
    return images, labels


def train_classifier(classifier):
    features, labels = get_data(TRAINING_IMAGES, TRAINING_LABELS)
    features, labels = list(features), list(labels)
    clf = classifier(features, labels)
    clf.train()
    return clf


def sim_ratio(a, b):
    same = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            same += 1
    return same / len(a)


def test_accuracy(clf):
    features, labels = get_data(TEST_IMAGES, TEST_LABELS)
    features, labels = list(features), list(labels)
    predictions = clf.predict(features)
    accuracy = sim_ratio(predictions, labels)
    return accuracy


if __name__ == '__main__':
    from argparse import ArgumentParser

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
    args = parser.parse_args()

    classifiers = {'decision_tree': DecisionTreeClassifier,
                   'svc': SVMClassifier}

    clf = train_classifier(classifiers[args.classifier])
    accuracy = test_accuracy(clf) * 100
    print(f'The {clf.name} works with {accuracy}% accuracy.')

    # Saving the model to avoid retraining
    save_model(clf)
