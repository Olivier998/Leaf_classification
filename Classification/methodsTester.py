"""
Tests multiple hyper-parameters for chosen method
"""
import Classification.classifier
import pandas as pd
from Data.globalParameters import M_list, lambda_list


def find_parameters_list(method_name, data_holder):
    dataframe_list = []
    data_train, label_train = data_holder.get_training_data()
    data_valid, label_valid = data_holder.get_validation_data()

    for m in M_list:  # m=3 takes too much time
        for lambd_i in lambda_list:
            # Define classifier
            classifier = Classification.classifier.Classifier(method_name, m=m, lambd=lambd_i)
            # Train method on data
            classifier.train(data_train, label_train)
            # Predict labels
            classifier.predict(data_valid)
            # Get prediction score
            score = classifier.score(label_valid)
            dataframe_list.append(pd.DataFrame([[m, lambd_i, score]], columns=['M', 'lambd', 'score']))
    data = pd.concat(dataframe_list, ignore_index=True)  # concat DataFrames
    return data
