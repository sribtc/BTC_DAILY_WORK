import yaml
from joblib import dump, load
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from sklearn.tree import DecisionTreeClassifier

import matplotlib.pyplot as plt
import seaborn as sns


class DiseasePrediction:
    def __init__(self, model_name=None):
        try:
            with open("./config.yaml", "r") as f:
                self.config = yaml.safe_load(f)
        except Exception as e:
            print("Error reading the config file....")

        self.verbose = self.config["verbose"]
        self.train_features,self.train_labels,self.train_df,= self.load_train_dataset()
        self.test_features,self.test_labels,self.test_df,= self.load_test_dataset()
        self.feature_correlation(data_frame=self.train_df, show_fig=False)
        self.model_name = model_name
        self.model_save_path = self.config["model_save_path"]

    def load_train_dataset(self):
        df_train = pd.read_csv(self.config["dataset"]["training_data_path"])
        cols = df_train.columns
        cols = cols[:-2]
        train_features = df_train[cols]
        train_labels = df_train["prognosis"]

        if self.verbose:
            print(f"Length of the training data", df_train.shape)
            print("Training Features", train_features.shape)
            print("Train Lables", train_labels.shape)

        return train_features, train_labels, df_train

    def load_test_dataset(self):
        df_test = pd.read_csv(self.config["dataset"]["test_data_path"])
        cols = df_test.columns
        cols = cols[:-1]
        test_features = df_test[cols]
        test_labels = df_test["prognosis"]

        if self.verbose:
            print("Length of Test Data", df_test.shape)
            print("Test Features", test_features.shape)
            print("Test Labels", test_labels.shape)

        return test_features,test_labels,df_test

    def feature_correlation(self, data_frame=None, show_fig=False):
        corr = data_frame.corr(numeric_only=True)
        sns.heatmap(corr, square=True, annot=False, cmap="YlGnBu")
        plt.title("Feature Correlation")
        plt.tight_layout()
        if show_fig:
            plt.show()
        plt.savefig("feature_correlation.png")

    def train_val_split(self):
        X_train, X_val, y_trian, y_val = train_test_split(
            self.train_features,
            self.train_labels,
            test_size=self.config["dataset"]["validation_size"],
            random_state=self.config["random_state"],
        )

        if self.verbose:
            print(
                "Number of Training Features: {0}\t Number of Training Labels: {1}".format(
                    len(X_train), len(y_trian)
                )
            )

            print(
                "Number of Validation features: {0}\t Number of Validation Lables: {1}".format(
                    len(X_val), len(y_val)
                )
            )

        return X_train, y_trian, X_val, y_val

    def select_model(self):
        if self.model_name == "decision_tree":
            self.clf = DecisionTreeClassifier(
                criterion=self.config["model"]["decision_tree"]["criterion"]
            )

        return self.clf

    def train_model(self):
        X_train, y_train, X_val, y_val = self.train_val_split()
        classifer = self.select_model()
        classifer = classifer.fit(X_train, y_train)
        confidence = classifer.score(X_val, y_val)
        y_pred = classifer.predict(X_val)
        accuracy = accuracy_score(y_pred, y_val)
        conf_mat = confusion_matrix(y_pred, y_val)
        clf_report = classification_report(y_val, y_pred)
        score = cross_val_score(classifer, X_val, y_val, cv=3)

        if self.verbose:
            print("\n Training Accuracy", confidence)
            print("\n Validation_prediction", y_pred)
            print("\n Validation accuracy", accuracy)
            print("\n Validation confusion_matrix", conf_mat)
            print("\n Cross Validation Score", score)
            print("\n Classification report", clf_report)

        dump(classifer, str(self.model_save_path + self.model_name + ".joblib"))

    def make_prediction(self, saved_model_name=None, test_data=None):
        try:
            clf = load(str(self.model_save_path + self.model_name + ".joblib"))
        except Exception as e:
            print("Model not found")
        if test_data is not None:
            result = clf.predict(test_data)
            return result
        else:
            result = clf.predict(self.test_features)
        accuracy = accuracy_score(self.test_labels, result)
        clf_report = classification_report(self.test_labels, result)
        return accuracy, clf_report


if __name__ == "__main__":
    current_model_name = "decision_tree"
    dp = DiseasePrediction(model_name=current_model_name)
    dp.train_model()
    test_accuracy, classification_report = dp.make_prediction(
        saved_model_name=current_model_name
    )
    print("Model Tets Accuracy", test_accuracy)
    print("Test Data Classification Report", classification_report)
