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
