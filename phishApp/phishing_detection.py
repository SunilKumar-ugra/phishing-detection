import numpy as np
from phishApp import feature_extraction
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression as lr
import os

# from flask import jsonify


def resolve(url):
    # Importing dataset
    data = np.loadtxt(os.path.dirname(__file__)+"/dataset.csv", delimiter=",")

    # Seperating features and labels
    X = data[:, :-1]
    y = data[:, -1]

    # Seperating training features, testing features, training labels & testing labels
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    clf = rfc()
    clf.fit(X_train, y_train)

    # rfc.predict(X_train, X_test);

    score = clf.score(X_test, y_test)

    # print("accuracy = ", score * 100)

    X_new = []

    X_input = url
    X_new = feature_extraction.generate_data_set(X_input)
    X_new = np.array(X_new).reshape(1, -1)

    try:
        prediction = clf.predict(X_new)
        if prediction == 1:
            return "Legitimate Url"
        else:
            return "Suspicious Url"
    except:
        return "Phishing Url"
