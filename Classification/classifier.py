"""
Main classification class, calls the wanted classification method
"""

from sklearn import linear_model


class Classifier:
    """
    Main class, which uses the wanted classification method
    """

    def __init__(self, method_name):
        """ Constructor
        :param method_name: Name of classification algorithm to use
        """
        self.predicted_labels = None  # predicted labels in self.predict
        if method_name == "fist_algo":
            self.classifier = None#linear_model.Ridge()

    def train(self, data_train, labels):
        """ Trains algorithm on training data
        :param data_train: training data
        :param labels: training labels
        """
        self.classifier.fit(data_train, labels)

    def predict(self, data_predict):
        """ Predicts the label for the data
        :param data_predict: Data on which we want to predict labels
        :return: Predicted labels
        """
        self.predicted_labels = self.classifier.predict(data_predict)
        return self.predicted_labels

    def score(self, real_labels):
        """ Get the prediction score for the classifier
        :param real_labels: Reals labels of predicted values
        :return: Prediction score of the classifier for predicted values
        """
        return self.classifier.score(self.predicted_labels, real_labels)
