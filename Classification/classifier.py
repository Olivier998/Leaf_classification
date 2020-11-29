"""
Main classification class, calls the wanted classification method
"""

from sklearn.linear_model import RidgeClassifier
from sklearn.metrics import accuracy_score
from Data.DataTransformations import polynomial_projection


class Classifier:
    """
    Main class, which uses the wanted classification method
    """

    def __init__(self, method_name, m=1, lambd=1):
        """ Constructor
        :param method_name: Name of classification algorithm to use
        :param m: Dimension to project data
        :param lambd: Regularization strength
        """
        self.predicted_labels = None  # predicted labels in self.predict
        self.M = m
        if method_name == "Ridge":
            self.classifier = RidgeClassifier(alpha=lambd)

    def train(self, data_train, labels):
        """ Trains algorithm on training data
        :param data_train: training data
        :param labels: training labels
        """
        data = polynomial_projection(self.M, data_train)
        self.classifier.fit(data, labels)

    def predict(self, data_predict):
        """ Predicts the label for the data
        :param data_predict: Data on which we want to predict labels
        :return: Predicted labels
        """
        data = polynomial_projection(self.M, data_predict)
        self.predicted_labels = self.classifier.predict(data)
        return self.predicted_labels

    def score(self, real_labels):
        """ Get the prediction score for the classifier
        :param real_labels: Reals labels of predicted values
        :return: Prediction score of the classifier for predicted values
        """
        return accuracy_score(real_labels, self.predicted_labels)
