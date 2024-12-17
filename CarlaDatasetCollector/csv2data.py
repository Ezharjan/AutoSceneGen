# with open('apollo_data.csv', 'r') as file:
# with open('pishgu_data_20240703_054827.csv', 'r') as file:
with open('pishgu_data_20240706_043213.csv', 'r') as file:
    lines = file.readlines()

output = []
for line in lines:
    # Remove the column names
    if 'Frame ID' in line:
        continue
    # Remove the commas
    line = line.replace(',', ' ')
    output.append(line.strip())

with open('output_file.txt', 'w') as file:
    file.write('\n'.join(output))