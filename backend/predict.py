import joblib
import os

# Model file path
MODEL_FILE = "cpu_predictor.pkl"


def load_model():
    """
    Loads the trained ML model from disk.
    """
    if not os.path.exists(MODEL_FILE):
        raise FileNotFoundError(
            "Trained model not found. Run model.py first to train the model."
        )
    return joblib.load(MODEL_FILE)


# Load model once (efficient)
model = load_model()


def predict_cpu(ram_usage: float, disk_usage: float) -> float:
    """
    Predicts CPU usage based on RAM and Disk usage.
    """
    prediction = model.predict([[ram_usage, disk_usage]])
    return float(prediction[0])
