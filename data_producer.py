import pandas as pd
import random
from datetime import datetime, timedelta
import numpy as np
import os

# Ensure Data folder exists
os.makedirs("Data", exist_ok=True)

NUM_RECORDS = 1000

# Constants
VEHICLE_MODELS = [" Sedan-X", "SUV-Z ", "Hatch-a", "COUPE-Y", " van-m", "Truck-T "]
ENGINE_TYPES = ["Petrol", "Diesel", "hybrid", "Electric ", None]
TRANSMISSIONS = ["automatic", "Manual", " MANUAL", "Automatic "]
COUNTRIES = [" Germany ", "usa", "JAPAN", "South Korea", "france "]

ROAD_SURFACES = ["Asphalt", " gravel", "Concrete ", "CobbleStone", "dirt "]
WEATHER = ["Sunny", "Rainy", " cloudy", "Dry", "Snowy"]
LOADS = ["Light Load", "medium", "Full Load", " "]
COMPONENTS = ["engine", "Cabin", "exhaust", "tires", "Transmission"]
MEASUREMENT_POINTS = ["Front Left Axle", "Rear Right Axle", "steering column", "Chassis center", "floor Panel"]
COMMENTS = [
    " Smooth ride with slight vibrations.",
    "Noticeable noise from tires ",
    "handles well on rough terrain ",
    "Cabin noise higher than expected",
    "VIBRATIONS felt on steering wheel",
    "Comfortable and quiet ",
    "needs Suspension TUNING",
    " Great handling in wet conditions"
]

base_time = datetime(2025, 7, 1, 8, 0)

# Vehicles Table
vehicle_list = []
for i in range(1, 101):
    record = {
        "VehicleID": f"V{i:03}",
        "Model": random.choice(VEHICLE_MODELS),
        "ManufacturingDate": random.choice([
            (datetime.strptime("2019-01-01", "%Y-%m-%d") + timedelta(days=random.randint(0, 2000))).strftime("%Y-%m-%d"),
            (datetime.strptime("2019-01-01", "%Y-%m-%d") + timedelta(days=random.randint(0, 2000))).strftime("%d/%m/%Y")
        ]),
        "EngineType": random.choice(ENGINE_TYPES),
        "Transmission": random.choice(TRANSMISSIONS),
        "Country": random.choice(COUNTRIES),
        "Location": random.choice(["Berlin, Germany", "Tokyo, Japan", "Texas, USA", "Paris, France", "Seoul, South Korea"])  # needs splitting
    }

    # Inject missing values
    if random.random() < 0.02:
        record["Transmission"] = ""

    vehicle_list.append(record)

vehicles_df = pd.DataFrame(vehicle_list)
vehicles_df = pd.concat([vehicles_df, vehicles_df.sample(5)])  # Add some duplicates

# Measurement Conditions Table
condition_list = []
for i in range(1, 21):
    condition_list.append({
        "ConditionID": f"C{i:03}",
        "RoadSurface": random.choice(ROAD_SURFACES),
        "Speed_kmph": str(random.randint(30, 120)) if random.random() < 0.2 else random.randint(30, 120),
        "Weather": random.choice(WEATHER),
        "Load": random.choice(LOADS)
    })
conditions_df = pd.DataFrame(condition_list)

# Noise Data Table
noise_records = []
for i in range(NUM_RECORDS):
    noise_level = round(random.normalvariate(72, 5), 1)
    if random.random() < 0.02:
        noise_level = random.choice([135.0, 145.0])  # Outlier

    noise_records.append({
        "NoiseID": f"N{i+1:04}",
        "VehicleID": random.choice(vehicles_df["VehicleID"]),
        "ConditionID": random.choice(conditions_df["ConditionID"]),
        "Timestamp": base_time + timedelta(minutes=i),
        "Component": random.choice(COMPONENTS),
        "SoundLevel_dB": str(noise_level) if random.random() < 0.1 else noise_level
    })
noise_df = pd.DataFrame(noise_records)

# Vibration Data Table
vibration_records = []
for i in range(NUM_RECORDS):
    vibration = round(random.uniform(0.15, 0.9), 2)
    if random.random() < 0.02:
        vibration = round(random.uniform(-1.0, -0.1), 2)  # Invalid

    vibration_records.append({
        "VibrationID": f"V{i+1:04}",
        "VehicleID": random.choice(vehicles_df["VehicleID"]),
        "ConditionID": random.choice(conditions_df["ConditionID"]),
        "Timestamp": base_time + timedelta(minutes=i),
        "MeasurementPoint": random.choice(MEASUREMENT_POINTS),
        "Vibration_m_s2": str(vibration) if random.random() < 0.05 else vibration
    })
vibration_df = pd.DataFrame(vibration_records)

# Harshness Feedback Table
feedback_records = []
for i in range(NUM_RECORDS):
    ride_score = round(random.uniform(5.0, 10.0), 1)
    handling_score = round(random.uniform(5.0, 10.0), 1)
    if random.random() < 0.02:
        ride_score = random.choice([11.0, 4.0])  # Invalid

    feedback_records.append({
        "FeedbackID": f"H{i+1:04}",
        "VehicleID": random.choice(vehicles_df["VehicleID"]),
        "Timestamp": base_time + timedelta(minutes=i),
        "RideComfortScore": str(ride_score) if random.random() < 0.1 else ride_score,
        "HandlingScore": handling_score,
        "Comment": random.choice(COMMENTS)
    })
feedback_df = pd.DataFrame(feedback_records)

# Save to CSV
vehicles_df.to_csv("Data/vehicles.csv", index=False)
conditions_df.to_csv("Data/measurement_conditions.csv", index=False)
noise_df.to_csv("Data/noise_data.csv", index=False)
vibration_df.to_csv("Data/vibration_data.csv", index=False)
feedback_df.to_csv("Data/harshness_feedback.csv", index=False)

print("✅ Data created with realistic anomalies for cleaning: whitespace, formatting, duplicates, type mismatch, etc.")
