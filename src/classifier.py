import joblib
from os.path import join
from sklearn import tree, svm

from files import PATH_TO_MODELS


def save_model(model):
    filename = join(PATH_TO_MODELS, f'{model.name}.sav')
    joblib.dump(model, filename)


class SVMClassifier(svm.SVC):

    def __init__(self, features, labels):
        super().__init__()
        self.name = 'svc'
        self.features = features
        self.labels = labels

    def train(self):
        super().fit(self.features, self.labels)


class DecisionTreeClassifier(tree.DecisionTreeClassifier):

    def __init__(self, features, labels):
        super().__init__()
        self.name = 'decision_tree'
        self.features = features
        self.labels = labels

    def train(self):
        super().fit(self.features, self.labels)
