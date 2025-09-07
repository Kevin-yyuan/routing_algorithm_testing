
import pandas as pd
import numpy as np
import os

# Create the data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Set the parameters for the data generation
n_samples = 1000
control_fuel_mean = 37.85 # Liters
eco_fuel_mean = 9.5
control_time_mean = 30
eco_time_mean = 32

# Generate the data
data = {
    'delivery_id': range(n_samples * 2),
    'algorithm': ['control'] * n_samples + ['eco'] * n_samples,
    'fuel_consumption': np.concatenate([
        np.random.normal(control_fuel_mean, 1.5, n_samples),
        np.random.normal(eco_fuel_mean, 1.5, n_samples)
    ]),
    'delivery_time': np.concatenate([
        np.random.normal(control_time_mean, 5, n_samples),
        np.random.normal(eco_time_mean, 5, n_samples)
    ])
}

# Create a DataFrame and save it to a CSV file
df = pd.DataFrame(data)
df.to_csv('data/delivery_data.csv', index=False)

print("Sample data generated and saved to data/delivery_data.csv")
