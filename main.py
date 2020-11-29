"""
 Projet personnel
__author__      :   Olivier Lefebvre
__date__        :   Novembre 2020
"""

import Data.database
import Classification.classifier
import Data.DataTransformations


def main():
    # set the database
    db = Data.database.Database()  # Get data
    db.remove_columns(["id"])  # remove columm "id"
    db.split_train_data(0.7)  # Split training value into train/validation data sets, where XX% is for training
    train_dataset, valid_dataset = db.get_train_validation_data()  # Get separate train and validation data

    # Get training values
    label_train = train_dataset["species"]  # Get training leaf species (target)
    label_train = Data.DataTransformations.label_encoder(label_train)  # Convert labels type
    data_train = train_dataset.drop("species", "columns")

    # Get validation values
    label_valid = valid_dataset["species"]  # Get validation leaf species (target)
    label_valid = Data.DataTransformations.label_encoder(label_valid)  # Convert labels type
    data_valid = valid_dataset.drop("species", "columns")

    # set classification method
    classifier = Classification.classifier.Classifier("Ridge", m=0, lambd=0.1)
    classifier.train(data_train, label_train)
    predicted = classifier.predict(data_valid)
    print(classifier.score(label_valid))
    #print(classifier.score(label_valid))

if __name__ == "__main__":
    main()
