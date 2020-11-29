"""
Multiple functions to transform data
"""

from sklearn import preprocessing


class LabelEncoder:
    """ Class to convert string variables (labels) to integer numbers """
    def __init__(self, unique_labels):
        """ Constructor : Fit label encoder """
        self.lab_encoder = preprocessing.LabelEncoder()
        self.lab_encoder.fit(unique_labels)

    def label_converter(self, labels):
        """ Convert non-numerical labels to numerical labels, based on already made fit
            :param labels: Array of non-numerical labels
            :return: Array of numerical labels
            """
        return self.lab_encoder.transform(labels)  # Else


def polynomial_projection(m, data):
    """ Projects data to M dimensions
    :param m: Degree of the polynomial
    :param data: Data to transform
    :return: Transformed array if m > 0, else original data
    """
    if m == 0:
        return data
    poly = preprocessing.PolynomialFeatures(m)
    return poly.fit_transform(data)
