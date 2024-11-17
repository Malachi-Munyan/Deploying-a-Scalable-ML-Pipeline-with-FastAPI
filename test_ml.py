import pytest
import numpy as numpy
import pandas as pd
from ml.model import train_model, compute_model_metrics
from ml.data import process_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# TODO: implement the first test. Change the function name and input as needed
def test_column_count():
    """
    Test to verify 15 columns in the dataset
    """
    df = pd.read_csv("data/census.csv")
    column_count = 15

    assert len(df.columns) == column_count


def test_model_algorithm():
    """
    Test to confirm the usage of Random Forest Classifier
    """
    X_holder = pd.DataFrame({'feature_1': [1, 2, 3], 'feature_2': ['A', 'B', 'C']})
    y_holder = pd.Series([0,1,0])
    X_holder_encoded = pd.get_dummies(X_holder)
    model = train_model(X_holder_encoded, y_holder)

    assert isinstance(model, RandomForestClassifier)


def test_metrics():
    """
    Test the compute_model_metrics are operating within expected values
    """
    y_true = pd.Series([0, 1, 0, 1])
    y_pred = pd.Series([0, 0, 1, 1])
    precision, recall, f1 = compute_model_metrics(y_true, y_pred)

    assert precision == 0.5
    assert recall == 0.5
    assert f1 == 0.5
