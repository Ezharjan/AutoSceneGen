import os
import csv
import os.path

def convert_csv_to_txt(csv_file, txt_file):
    with open(csv_file, 'r') as file:
        lines = file.readlines()

    output = []
    for line in lines:
        # Remove the column names
        if 'Frame ID' in line:
            continue
        # Remove the commas
        line = line.replace(',', ' ')
        output.append(line.strip())

    with open(txt_file, 'w') as file:
        file.write('\n'.join(output))

def convert_spaces_to_tabs(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    new_lines = []
    for line in lines:
        values = line.strip().split()
        new_values = []
        for value in values:
            if '.' in value:
                new_values.append(value)
            else:
                new_values.append(f"{value}.0")
        new_lines.append('\t'.join(new_values))

    try:
        with open(file_path, 'w') as file:
            file.write('\n'.join(new_lines))
        print(f"File '{file_path}' has been updated.")
    except IOError:
        print(f"Error: Unable to write to file '{file_path}'.")

def main():
    # Get the current directory
    current_dir = os.getcwd()

    # Create the 'ngsim' folder if it doesn't exist
    ngsim_dir = os.path.join(current_dir, 'ngsim')
    if not os.path.exists(ngsim_dir):
        os.makedirs(ngsim_dir)

    # Iterate through all CSV files in the current directory
    for filename in os.listdir(current_dir):
        if filename.endswith('.csv'):
            csv_file = os.path.join(current_dir, filename)
            txt_file = os.path.join(ngsim_dir, f'ngsim_carpe_tr{len(os.listdir(ngsim_dir))}.txt')
            convert_csv_to_txt(csv_file, txt_file)
            convert_spaces_to_tabs(txt_file)

if __name__ == "__main__":
    main()