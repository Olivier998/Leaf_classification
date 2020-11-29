"""
Multiple functions to transform data
"""

from sklearn import preprocessing


def label_encoder(labels):
    """ Convert non-numerical labels to numerical labels
    :param labels: Array of non-numerical labels
    :return: Array of numerical labels
    """
    lab_encoder = preprocessing.LabelEncoder()
    return lab_encoder.fit_transform(labels)


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
