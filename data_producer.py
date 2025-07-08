import pandas as pd
import random
from datetime import datetime, timedelta
import numpy as np
import os

# Ensure Data folder exists
os.makedirs("Data", exist_ok=True)

# --------------------------
# Setup Constants
# --------------------------
NUM_RECORDS = 1000
VEHICLE_MODELS = ["Sedan-X", "SUV-Z", "Hatch-A", "Coupe-Y", "Van-M", "Truck-T"]
ENGINE_TYPES = ["Petrol", "Diesel", "Hybrid", "Electric"]
TRANSMISSIONS = ["Automatic", "Manual"]
COUNTRIES = ["Germany", "USA", "Japan", "South Korea", "France"]

ROAD_SURFACES = ["Asphalt", "Gravel", "Concrete", "Cobblestone", "Dirt"]
WEATHER = ["Sunny", "Rainy", "Cloudy", "Dry", "Snowy"]
LOADS = ["Light Load", "Medium", "Full Load"]
COMPONENTS = ["Engine", "Cabin", "Exhaust", "Tires", "Transmission"]
MEASUREMENT_POINTS = ["Front Left Axle", "Rear Right Axle", "Steering Column", "Chassis Center", "Floor Panel"]
COMMENTS = [
    "Smooth ride with slight vibrations.",
    "Noticeable noise from tires.",
    "Handles well on rough terrain.",
    "Cabin noise higher than expected.",
    "Vibrations felt on steering wheel.",
    "Comfortable and quiet.",
    "Needs suspension tuning.",
    "Great handling in wet conditions."
]

base_time = datetime(2025, 7, 1, 8, 0)

# --------------------------
# 1. Vehicles Table
# --------------------------
vehicle_list = []
for i in range(1, 101):
    record = {
        "VehicleID": f"V{i:03}",
        "Model": random.choice(VEHICLE_MODELS),
        "ManufacturingDate": datetime.strptime("2019-01-01", "%Y-%m-%d") + timedelta(days=random.randint(0, 2000)),
        "EngineType": random.choice(ENGINE_TYPES),
        "Transmission": random.choice(TRANSMISSIONS),
        "Country": random.choice(COUNTRIES)
    }

    # Inject anomaly: missing EngineType in 3% of cases
    if random.random() < 0.03:
        record["EngineType"] = None

    vehicle_list.append(record)

vehicles_df = pd.DataFrame(vehicle_list)

# --------------------------
# 2. Measurement Conditions Table
# --------------------------
condition_list = []
for i in range(1, 21):
    condition_list.append({
        "ConditionID": f"C{i:03}",
        "RoadSurface": random.choice(ROAD_SURFACES),
        "Speed_kmph": random.randint(30, 120),
        "Weather": random.choice(WEATHER),
        "Load": random.choice(LOADS)
    })
conditions_df = pd.DataFrame(condition_list)

# --------------------------
# 3. Noise Data Table
# --------------------------
noise_records = []
for i in range(NUM_RECORDS):
    noise_level = round(random.normalvariate(72, 5), 1)

    # Inject anomaly: extreme outliers in 2% cases
    if random.random() < 0.02:
        noise_level = random.choice([135.0, 145.0])  # Unrealistic

    record = {
        "NoiseID": f"N{i+1:04}",
        "VehicleID": random.choice(vehicles_df["VehicleID"]),
        "ConditionID": random.choice(conditions_df["ConditionID"]),
        "Timestamp": base_time + timedelta(minutes=i),
        "Component": random.choice(COMPONENTS),
        "SoundLevel_dB": noise_level
    }
    noise_records.append(record)

noise_df = pd.DataFrame(noise_records)

# --------------------------
# 4. Vibration Data Table
# --------------------------
vibration_records = []
for i in range(NUM_RECORDS):
    vibration = round(random.uniform(0.15, 0.9), 2)

    # Inject anomaly: invalid negative vibration in 2%
    if random.random() < 0.02:
        vibration = round(random.uniform(-1.0, -0.1), 2)

    record = {
        "VibrationID": f"V{i+1:04}",
        "VehicleID": random.choice(vehicles_df["VehicleID"]),
        "ConditionID": random.choice(conditions_df["ConditionID"]),
        "Timestamp": base_time + timedelta(minutes=i),
        "MeasurementPoint": random.choice(MEASUREMENT_POINTS),
        "Vibration_m_s2": vibration
    }
    vibration_records.append(record)

vibration_df = pd.DataFrame(vibration_records)

# --------------------------
# 5. Harshness Feedback Table
# --------------------------
feedback_records = []
for i in range(NUM_RECORDS):
    ride_score = round(random.uniform(5.0, 10.0), 1)
    handling_score = round(random.uniform(5.0, 10.0), 1)

    # Inject anomaly: invalid comfort scores
    if random.random() < 0.02:
        ride_score = random.choice([11.0, 4.0])  # Out of 1-10 scale

    record = {
        "FeedbackID": f"H{i+1:04}",
        "VehicleID": random.choice(vehicles_df["VehicleID"]),
        "Timestamp": base_time + timedelta(minutes=i),
        "RideComfortScore": ride_score,
        "HandlingScore": handling_score,
        "Comment": random.choice(COMMENTS)
    }
    feedback_records.append(record)

feedback_df = pd.DataFrame(feedback_records)

# --------------------------
# Save to CSV
# --------------------------
vehicles_df.to_csv("Data/vehicles.csv", index=False)
conditions_df.to_csv("Data/measurement_conditions.csv", index=False)
noise_df.to_csv("Data/noise_data.csv", index=False)
vibration_df.to_csv("Data/vibration_data.csv", index=False)
feedback_df.to_csv("Data/harshness_feedback.csv", index=False)

print("✅ All 5 synthetic NVH datasets generated with anomalies and saved to 'Data/' folder.")
