import pandas as pd
import numpy as np
import random
import os
from datetime import datetime, timedelta

# Seed for reproducibility
np.random.seed(42)

# Parameters
n_rows = 500
start_date = datetime(2025, 1, 1)

# Sample data options
manufacturers = ['Bosch', 'Shimano', 'Specialized', 'Trek', 'Canyon', 'Haibike']
models = [
    ('Aventure.2', 'Aventon'),
    ('Pathlite:ON 5', 'Canyon'),
    ('Pace 500.3', 'Aventon'),
    ('AllMtn 3', 'Haibike'),
    ('Grand Canyon:ON 7', 'Canyon'),
    ('CX Line TrailMaster', 'Bosch'),
    ('Cargo Line eHauler', 'Bosch'),
    ('Sinch.2 Foldable', 'Aventon'),
    ('Trekking 4', 'Haibike'),
    ('Torque:ON 8', 'Canyon'),
    ('HardNine 6', 'Haibike'),
    ('Soltera.2', 'Aventon'),
    ('Neuron:ON 6', 'Canyon'),
    ('XDURO NDURO 3.0', 'Haibike'),
    ('Level.2 Commuter', 'Aventon'),
    ('Spectral:ON CF 7', 'Canyon'),
    ('FullNine 8', 'Haibike'),
    ('Performance Line SportX', 'Bosch'),
    ('Precede:ON CF 9', 'Canyon'),
    ('Active Line UrbanCruiser', 'Bosch'),
    ('Pace 350.3', 'Aventon')
]

components = [
    'Motor', 'Frame', 'Crankset', 'Battery', 'Fork', 'Chain', 'Rear Shock',
    'Handlebar', 'Pedal Assist Sensor', 'Gear Shifter', 'Brake Lever', 'Derailleur'
]
road_surfaces = ['Asphalt', 'Gravel', 'Cobblestone', 'Dirt', 'Forest Trail', 'Bike Lane']
conditions = ['Dry', 'Wet', 'Uphill', 'Downhill', 'Windy', 'Cold Weather']
feedback_comments = [
    "Very smooth ride", "Too noisy", "Strong vibration on rough roads",
    "Comfortable handling", "Noticeable harshness", "Quiet and stable",
    "Needs improvement in suspension", "Good performance overall"
]

# Generate synthetic data
data = []
for i in range(1, n_rows + 1):
    model, manufacturer = random.choice(models)
    mfg_date = start_date - timedelta(days=np.random.randint(200, 1000))
    timestamp = start_date + timedelta(days=np.random.randint(0, 180),
                                       hours=np.random.randint(0, 24),
                                       minutes=np.random.randint(0, 60))
    noise = round(np.random.normal(70, 5), 1)
    vibration = round(np.random.normal(2.5, 0.7), 2)
    harshness_score = round(np.clip(np.random.normal(3.5, 1.2), 1, 5), 1)
    feedback = random.choice(feedback_comments)
    component = random.choice(components)
    surface = random.choice(road_surfaces)
    condition = random.choice(conditions)

    data.append([
        i, model, manufacturer, mfg_date.strftime('%Y-%m-%d'), timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        noise, vibration, harshness_score, feedback,
        component, surface, condition
    ])

# Create main DataFrame
df = pd.DataFrame(data, columns=[
    'TestID', 'Model', 'Manufacturer', 'ManufacturingDate', 'Timestamp',
    'Noise_dB', 'Vibration_mps2', 'HarshnessScore', 'CustomerFeedback',
    'Component', 'RoadSurface', 'OperatingCondition'
])

# --- Create Dimension Tables ---

# Model Dimension (add Manufacturer)
dim_model = df[['Model', 'Manufacturer', 'ManufacturingDate']].drop_duplicates().reset_index(drop=True)
dim_model['ModelID'] = dim_model.index + 1

# Component Dimension
dim_component = df[['Component']].drop_duplicates().reset_index(drop=True)
dim_component['ComponentID'] = dim_component.index + 1

# Surface Dimension
dim_surface = df[['RoadSurface']].drop_duplicates().reset_index(drop=True)
dim_surface['SurfaceID'] = dim_surface.index + 1

# Condition Dimension
dim_condition = df[['OperatingCondition']].drop_duplicates().reset_index(drop=True)
dim_condition['ConditionID'] = dim_condition.index + 1

# --- Create Fact Table with Foreign Keys ---
fact_nvh = df.merge(dim_model, on=['Model', 'Manufacturer', 'ManufacturingDate'], how='left') \
             .merge(dim_component, on='Component', how='left') \
             .merge(dim_surface, on='RoadSurface', how='left') \
             .merge(dim_condition, on='OperatingCondition', how='left')

fact_nvh = fact_nvh[[
    'TestID', 'Timestamp', 'Noise_dB', 'Vibration_mps2', 'HarshnessScore', 'CustomerFeedback',
    'ModelID', 'ComponentID', 'SurfaceID', 'ConditionID'
]]

# Create folder if not exists
output_dir = "Produced_Data"
os.makedirs(output_dir, exist_ok=True)

# Save CSVs into the folder
fact_nvh.to_csv(os.path.join(output_dir, "Test_Data.csv"), index=False)
dim_model.to_csv(os.path.join(output_dir, "Model.csv"), index=False)
dim_component.to_csv(os.path.join(output_dir, "Component.csv"), index=False)
dim_surface.to_csv(os.path.join(output_dir, "Surface.csv"), index=False)
dim_condition.to_csv(os.path.join(output_dir, "Condition.csv"), index=False)

# Print confirmation
print("\n✅ All files saved in the 'Produced_Data' folder:")
for file in os.listdir(output_dir):
    print("  -", file)
