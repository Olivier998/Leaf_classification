""" File to store global settings and allow easier modifications """

# hyper-parameters values
M_list = range(2)  # Values for polynomial projection, M=2 takes some time, M>=3 takes a lot of time
lambda_list = [10**-n for n in range(0, 6)]  # Values for regularization term, must be in terms of 10**-n

# All implemented methods names (should be implemented in Classification\classifier.py)
methods_list = ["Choose a method", "Ridge", "Logistic Regression", "SGD", "Perceptron", "SVM",
                "Random forest", "ML Perceptron"]

# Data files location
test_data_location = "Data_files/test.csv"
train_data_location = "Data_files/train.csv"
