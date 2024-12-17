import os
import csv
import sys

def transpose_csv(input_file, output_file):
    # Open the input CSV file
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Convert the order of the columns (move the first column to the second and the second column to the first)
    # reorganized_data = [[row[1], row[0]] + row[2:] for row in data]
    # keep original data
    reorganized_data = data

    # Transpose the data (convert columns to rows and rows to columns)
    transposed_data = list(map(list, zip(*reorganized_data[1:])))  # Start from the second row (index 1) to skip the header

    # Open the output CSV file and write the transposed data
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(transposed_data)

def main():
    # Get the input directory from the command line
    if len(sys.argv) < 2:
        print("Please provide the input directory as a command-line argument.")
        return

    input_dir = sys.argv[1]

    # Get the current directory
    current_dir = os.getcwd()

    # Create the 'dataset_converted' folder inside the current directory
    output_dir = os.path.join(current_dir, 'dataset_converted')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through all CSV files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, f'msrl_{filename}')
            transpose_csv(input_file, output_file)
            print(f"Successfully transposed and stored {input_file} to {output_file}!")

if __name__ == "__main__":
    main()