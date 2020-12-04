"""
 Projet personnel
__author__      :   Olivier Lefebvre
__date__        :   Novembre 2020
"""

import Data.database
import Data.DataTransformations
import Data.dataHolder
import Visualisation.main_box


def main():
    # set dataHolder
    holder = Data.dataHolder.Dataholder()

    # set the database
    db = Data.database.Database()  # Get data
    db.remove_columns(["id"])  # remove columm "id"
    db.split_train_data(0.7)  # Split training value into train/validation data sets, where XX% is for training
    train_dataset, valid_dataset = db.get_train_validation_data()  # Get separate train and validation data

    # Set encoder
    unique_labels = db.get_unique_values("species")
    encoder = Data.DataTransformations.LabelEncoder(unique_labels)

    # Get training values
    label_train = train_dataset["species"].values  # Get training leaf species (target) in an array
    label_train = encoder.label_converter(label_train)  # Convert labels type
    data_train = train_dataset.drop("species", "columns")

    # Add training values to data holder
    holder.set_training_data(data_train=data_train, label_train=label_train)

    # Get validation values
    label_valid = valid_dataset["species"].values  # Get validation leaf species (target)
    label_valid = encoder.label_converter(label_valid)  # Convert labels type
    data_valid = valid_dataset.drop("species", "columns")

    # Add validation values to data holder
    holder.set_validation_data(data_valid=data_valid, label_valid=label_valid)

    # create interface
    Visualisation.main_box.show_interface(holder)

    import Classification.methodsTester
    #Classification.methodsTester.find_parameters_list("SGD",
    #                                                  holder)

    # set classification method
    # for m in range(2):  # m=3 takes too much time
    #     for lambd_i in [2**-n for n in range(0, 10)]:
    #         classifier = Classification.classifier.Classifier(method, m=m, lambd=lambd_i)
    #         classifier.train(data_train, label_train)
    #         predicted = classifier.predict(data_valid)
    #         print("m={}, lambda={}, accuracy={}".format(m, lambd_i, classifier.score(label_valid)))


    # classifier = Classification.classifier.Classifier(method, m=1, lambd=0.01)
    # classifier.train(data_train, label_train)
    # predicted = classifier.predict(data_valid)
    # print(classifier.score(label_valid))


if __name__ == "__main__":
    main()
