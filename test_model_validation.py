import pandas as pd

import joblib

from sklearn.metrics import accuracy_score

from sklearn.model_selection import train_test_split

import pytest

import os



# Test Case 1: Data Validation Test

def test_data_shape_and_columns():

    """

    Tests if the dataset has the expected shape.

    This is a data validation sanity check.

    """

    # Check if the data file exists before trying to read it

    assert os.path.exists('data/iris.csv'), "Dataset file 'data/iris.csv' not found. Ensure DVC has pulled the data."

    

    df = pd.read_csv('data/iris.csv')

    



    expected_rows = 45

    expected_columns = 8

    

    assert df.shape == (expected_rows, expected_columns), \

        f"Data shape is incorrect. Expected ({expected_rows}, {expected_columns}), but got {df.shape}"

    

    print("\n✅ Data Validation Test Passed: Shape and columns are correct.")



# Test Case 2: Model Evaluation Test

def test_model_accuracy():

    """

    Tests if the trained model's accuracy is above a 90% threshold.

    This is a model evaluation sanity check.

    """

    # Check if model and data files exist

    assert os.path.exists('artifacts/model.joblib'), "Model file 'artifacts/model.joblib' not found. Ensure DVC has pulled the data."

    assert os.path.exists('data/iris.csv'), "Dataset file 'data/iris.csv' not found. Ensure DVC has pulled the data."



    # Load the latest version of the model and data

    model = joblib.load('artifacts/model.joblib')

    df = pd.read_csv('data/iris.csv')



    # Prepare data for testing (assuming last column is the target)

    X = df.iloc[:, :-1]

    y = df.iloc[:, -1]



    # Use a consistent split for reliable testing

    _, X_test, _, y_test = train_test_split(X, y, test_size=0.3, random_state=42)



    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    

    print(f"\nModel accuracy: {accuracy:.2f}")



    assert accuracy > 0.90, f"Model accuracy {accuracy:.2f} is below the 0.90 threshold."

    

    print("✅ Model Evaluation Test Passed: Accuracy is above the 90% threshold.")
# This is a comment to trigger a new CI run
# This is a comment to trigger a new CI run_1
