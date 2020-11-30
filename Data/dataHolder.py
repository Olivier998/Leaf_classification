"""
Keeps important data in a class
"""


class Dataholder:
    """ Keeps important data, to allow easier access """

    def __init__(self):
        """ Constructor """
        self.data_train = None
        self.data_valid = None
        self.label_train = None
        self.label_valid = None

    def set_training_data(self, data_train, label_train):
        """ Set class parameters for training data
        :param data_train: data_train
        :param label_train: label_train
        """
        self.data_train = data_train
        self.label_train = label_train

    def set_validation_data(self, data_valid, label_valid):
        """ Set class parameters for validation data
        :param data_valid: data_valid
        :param label_valid: label_valid
        """
        self.data_valid = data_valid
        self.label_valid = label_valid

    def get_training_data(self):
        """ Returns training data """
        return self.data_train, self.label_train

    def get_validation_data(self):
        """ Returns validation data """
        return self.data_valid, self.label_valid
