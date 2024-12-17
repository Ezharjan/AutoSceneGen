import csv

# Open the input CSV file
with open('input.csv', 'r') as input_file:
    reader = csv.reader(input_file)
    data = list(reader)

# Transpose the data (convert columns to rows and rows to columns)
transposed_data = list(map(list, zip(*data)))
# transposed_data = list(map(list, zip(*data[1:])))  # Start from the second row (index 1) to skip the header

# Open the output CSV file and write the transposed data
with open('output.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(transposed_data)