import csv
import os

file_path = "result_9048_1_frame.txt"

# Read the input file
with open(file_path, 'r') as file:
    data = file.read().strip()

# Split the input data into rows
rows = [row.strip() for row in data.split('\n')]

# Construct the output file name
output_file = os.path.splitext(os.path.basename(file_path))[0] + ".csv"

# Create a CSV file
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the header row
    writer.writerow(['frame_id', 'object_id', 'object_type', 'position_x', 'position_y', 'position_z', 'object_length', 'object_width', 'object_height', 'heading'])
    
    # Write the data rows
    for row in rows:
        values = [float(x) for x in row.split()]
        writer.writerow(values)

print(f"CSV file '{output_file}' created successfully.")