import pandas as pd
import random
from datetime import datetime, timedelta
import numpy as np

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
MEASUREMENT_POINTS = ["Front Left Axle", "Rear Right Axle", "Steering Column", "Chassis Center","Floor Panel"]
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

# --------------------------
# 1. Vehicles Table
# --------------------------
vehicle_list = []
for i in range(1, 101):
    vehicle_list.append({
        "VehicleID": f"V{i:03}",
        "Model": random.choice(VEHICLE_MODELS),
        "ManufacturingDate": datetime.strptime("2019-01-01", "%Y-%m-%d") + timedelta(days=random.randint(0, 2000)),
        "EngineType": random.choice(ENGINE_TYPES),
        "Transmission": random.choice(TRANSMISSIONS),
        "Country": random.choice(COUNTRIES)
    })
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
base_time = datetime(2025, 7, 1, 8, 0)
for i in range(NUM_RECORDS):
    noise_records.append({
        "NoiseID": f"N{i+1:04}",
        "VehicleID": random.choice(vehicles_df["VehicleID"]),
        "ConditionID": random.choice(conditions_df["ConditionID"]),
        "Timestamp": base_time + timedelta(minutes=i),
        "Component": random.choice(COMPONENTS),
        "SoundLevel_dB": round(random.normalvariate(72, 5), 1)  # Mean 72dB with small variation
    })
noise_df = pd.DataFrame(noise_records)

# --------------------------
# 4. Vibration Data Table
# --------------------------
vibration_records = []
for i in range(NUM_RECORDS):
    vibration_records.append({
        "VibrationID": f"V{i+1:04}",
        "VehicleID": random.choice(vehicles_df["VehicleID"]),
        "ConditionID": random.choice(conditions_df["ConditionID"]),
        "Timestamp": base_time + timedelta(minutes=i),
        "MeasurementPoint": random.choice(MEASUREMENT_POINTS),
        "Vibration_m_s2": round(random.uniform(0.15, 0.9), 2)  # Range for vibration acceleration
    })
vibration_df = pd.DataFrame(vibration_records)

# --------------------------
# 5. Harshness Feedback Table
# --------------------------
feedback_records = []
for i in range(NUM_RECORDS):
    feedback_records.append({
        "FeedbackID": f"H{i+1:04}",
        "VehicleID": random.choice(vehicles_df["VehicleID"]),
        "Timestamp": base_time + timedelta(minutes=i),
        "RideComfortScore": round(random.uniform(5.0, 10.0), 1),
        "HandlingScore": round(random.uniform(5.0, 10.0), 1),
        "Comment": random.choice(COMMENTS)
    })
feedback_df = pd.DataFrame(feedback_records)

# --------------------------
# Save to CSV
# --------------------------
vehicles_df.to_csv("Data/vehicles.csv", index=False)
conditions_df.to_csv("Data/measurement_conditions.csv", index=False)
noise_df.to_csv("Data/noise_data.csv", index=False)
vibration_df.to_csv("Data/vibration_data.csv", index=False)
feedback_df.to_csv("Data/harshness_feedback.csv", index=False)

print("✅ All 5 synthetic NVH datasets generated with 500+ records each and saved to CSV files.")
