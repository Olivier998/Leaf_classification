"""
Class to get raw data from csv files and split train data into training and validation data sets
"""
import pandas as pd
from sklearn.model_selection import train_test_split


class Database:
    """ This class gets training, validation and testing data from csv files. """

    def __init__(self, folder="Data/"):
        """ Constructor
        :param folder: Name of folder containing Data_files/test.csv and Data_files/train.csv
        """
        self.test_data = pd.read_csv(folder + "Data_files/test.csv")
        self.complete_train_data = pd.read_csv(folder + "Data_files/train.csv")
        self.validation_data = None
        self.train_data = None

    def get_unique_values(self, column="species"):
        """ returns all unique labels in an array, which we can use to encode labels """
        return self.complete_train_data[column].unique()

    def get_test_data(self):
        """
        :return: testing dataset
        """
        return self.test_data

    def get_train_data(self):
        """ Returns complete train data set, without validation
        :return: training data set
        """
        return self.complete_train_data

    def get_train_validation_data(self):
        """ Returns train and validation data sets
        :return: training data set, validation data set
        """
        if self.validation_data is None:  # if train data is not already split
            self.split_train_data()
        return self.train_data, self.validation_data

    def remove_columns(self, columns):
        """ removes columns from data sets
        :param columns: List of string for every columns header to remove
        """
        list_dataset = [self.test_data, self.complete_train_data, self.train_data, self.validation_data]
        for column in columns:
            for dataset in list_dataset:
                try:  # Try to remove each column
                    dataset.pop(column)
                except:
                    continue

    def split_train_data(self, percent_train=0.7):
        """ Shuffles then split train data into train and validation data sets

        :param percent_train: Percentage of data to use as training data set
        """
        self.train_data, self.validation_data = train_test_split(self.complete_train_data, train_size=percent_train)
