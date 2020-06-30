from os import pardir, makedirs
from os.path import dirname, join, abspath, exists

PARENT_DIR = abspath(join(dirname(abspath(__file__)), pardir))

PATH_TO_MODELS = join(PARENT_DIR, 'trained_models')
PATH_TO_TEST_DATA = join(PARENT_DIR, 'test_data')
PATH_TO_TRAINING_DATA = join(PARENT_DIR, 'training_data')

TRAINING_IMAGES = join(PATH_TO_TRAINING_DATA, 'train-images-idx3-ubyte')
TRAINING_LABELS = join(PATH_TO_TRAINING_DATA, 'train-labels-idx1-ubyte')
TEST_IMAGES = join(PATH_TO_TEST_DATA, 't10k-images-idx3-ubyte')
TEST_LABELS = join(PATH_TO_TEST_DATA, 't10k-labels-idx1-ubyte')

SVM_CLASSIFIER = join(PATH_TO_MODELS, 'svc.sav')
MODELS = {'svc': SVM_CLASSIFIER}


PATHS = [PATH_TO_MODELS, PATH_TO_TEST_DATA, PATH_TO_TRAINING_DATA]
for PATH in PATHS:
    if not exists(PATH):
        makedirs(PATH)
