import pandas as pd
import numpy as np
import random
import os
from datetime import datetime, timedelta

# Seed for reproducibility
np.random.seed(42)

# Constants
start_date = datetime(2025, 1, 1)
manufacturers = ['Bosch', 'Shimano', 'Specialized', 'Trek']
models_per_manufacturer = 5
tests_per_model = 5
speeds_per_test = [5, 10, 15, 20, 25, 30]

components = [
    'Motor', 'Frame', 'Crankset', 'Battery', 'Fork', 'Chain', 'Rear Shock',
    'Handlebar', 'Pedal Assist Sensor', 'Gear Shifter', 'Brake Lever', 'Derailleur'
]
road_surfaces = ['Asphalt', 'Gravel', 'Cobblestone', 'Dirt', 'Forest Trail']
conditions = ['Dry', 'Wet', 'Uphill', 'Downhill', 'Windy', 'Cold Weather']
feedback_comments = [
    "Very smooth ride", "Too noisy", "Strong vibration on rough roads",
    "Comfortable handling", "Noticeable harshness", "Quiet and stable",
    "Needs improvement in suspension", "Good performance overall"
]

# Generate 20 unique models (5 per manufacturer)
model_list = []
for mfg in manufacturers:
    for i in range(1, models_per_manufacturer + 1):
        model_list.append((f"{mfg[0:3]}00{i}", mfg))

# Generate synthetic data
data = []
test_id = 1

for model_name, manufacturer in model_list:
    mfg_date = start_date - timedelta(days=np.random.randint(200, 1000))
    used_surfaces = random.sample(road_surfaces, tests_per_model)

    for surface in used_surfaces:
        condition = random.choice(conditions)

        for speed in speeds_per_test:
            timestamp = start_date + timedelta(
                days=np.random.randint(0, 180),
                hours=np.random.randint(0, 24),
                minutes=np.random.randint(0, 60)
            )

            for component in components:
                noise = round(np.random.normal(70, 5), 1)
                vibration = round(np.random.normal(2.5, 0.7), 2)
                harshness_score = round(np.clip(np.random.normal(3.5, 1.2), 1, 5), 1)
                feedback = random.choice(feedback_comments)

                data.append([
                    test_id, model_name, manufacturer, mfg_date.strftime('%Y-%m-%d'),
                    timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    noise, vibration, harshness_score, speed, feedback,
                    component, surface, condition
                ])
        test_id += 1

# Create main DataFrame
df = pd.DataFrame(data, columns=[
    'TestID', 'Model', 'Manufacturer', 'ManufacturingDate', 'Timestamp',
    'Noise_dB', 'Vibration_mps2', 'HarshnessScore', 'Speed_kmph', 'CustomerFeedback',
    'Component', 'RoadSurface', 'OperatingCondition'
])

# Dimension Tables
dim_model = df[['Model', 'Manufacturer', 'ManufacturingDate']].drop_duplicates().reset_index(drop=True)
dim_model['ModelID'] = dim_model.index + 1

dim_component = df[['Component']].drop_duplicates().reset_index(drop=True)
dim_component['ComponentID'] = dim_component.index + 1

dim_surface = df[['RoadSurface']].drop_duplicates().reset_index(drop=True)
dim_surface['SurfaceID'] = dim_surface.index + 1

dim_condition = df[['OperatingCondition']].drop_duplicates().reset_index(drop=True)
dim_condition['ConditionID'] = dim_condition.index + 1

# Fact Table with Foreign Keys
fact_nvh = df.merge(dim_model, on=['Model', 'Manufacturer', 'ManufacturingDate'], how='left') \
             .merge(dim_component, on='Component', how='left') \
             .merge(dim_surface, on='RoadSurface', how='left') \
             .merge(dim_condition, on='OperatingCondition', how='left')

fact_nvh = fact_nvh[[
    'TestID', 'Timestamp', 'Noise_dB', 'Vibration_mps2', 'HarshnessScore', 'Speed_kmph',
    'CustomerFeedback', 'ModelID', 'ComponentID', 'SurfaceID', 'ConditionID'
]]

# Save to CSV
output_dir = "Produced_Data"
os.makedirs(output_dir, exist_ok=True)

fact_nvh.to_csv(os.path.join(output_dir, "Test_Data.csv"), index=False)
dim_model.to_csv(os.path.join(output_dir, "Model.csv"), index=False)
dim_component.to_csv(os.path.join(output_dir, "Component.csv"), index=False)
dim_surface.to_csv(os.path.join(output_dir, "Surface.csv"), index=False)
dim_condition.to_csv(os.path.join(output_dir, "Condition.csv"), index=False)

print("\n✅ All files saved to folder 'Produced_Data'")
