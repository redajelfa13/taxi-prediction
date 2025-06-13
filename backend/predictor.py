import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

fare_model = joblib.load(os.path.join(BASE_DIR, "fare_model.pkl"))
distance_model = joblib.load(os.path.join(BASE_DIR, "distance_model.pkl"))

def predict_fare(trip_distance: float) -> float:
    return float(fare_model.predict([[trip_distance]])[0])

def predict_distance(fare_amount: float) -> float:
    return float(distance_model.predict([[fare_amount]])[0])
