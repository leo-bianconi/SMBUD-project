import json
import random

# Define the function to reduce the dataset
def reduce_json_dataset(input_file, output_file, sample_size):
    with open(input_file, 'r') as file:
        data = json.load(file)  # Load the JSON data

    if len(data) < sample_size:
        raise ValueError("Sample size exceeds the number of available entities in the dataset.")

    # Select a random sample of entities
    reduced_data = random.sample(data, sample_size)

    # Write the reduced dataset to a new file
    with open(output_file, 'w') as file:
        json.dump(reduced_data, file, indent=4)

# File paths
input_file_path = "mongodb/dataset/Crime_Data.json"
output_file_path = "mongodb/dataset/Crime_Data_Reduced.json"

# Desired sample size
sample_size = 30000

# Reduce the dataset
reduce_json_dataset(input_file_path, output_file_path, sample_size)

print(f"Reduced dataset saved to {output_file_path}")