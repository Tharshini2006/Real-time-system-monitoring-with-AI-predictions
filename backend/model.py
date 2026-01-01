import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

# Paths
DATA_FILE = os.path.join("..", "data", "system_data.csv")
MODEL_FILE = "cpu_predictor.pkl"


def train_cpu_prediction_model():
    """
    Trains a Linear Regression model to predict CPU usage
    based on RAM and Disk usage.
    """

    # Check if data file exists
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError("system_data.csv not found. Run monitor.py first.")

    # Load data
    data = pd.read_csv(DATA_FILE)

    # Required columns check
    required_columns = {"cpu", "ram", "disk"}
    if not required_columns.issubset(data.columns):
        raise ValueError("CSV file must contain cpu, ram, and disk columns")

    # Features and target
    X = data[["ram", "disk"]]
    y = data["cpu"]

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Save trained model
    joblib.dump(model, MODEL_FILE)

    print("✅ CPU prediction model trained and saved as cpu_predictor.pkl")


if __name__ == "__main__":
    train_cpu_prediction_model()
