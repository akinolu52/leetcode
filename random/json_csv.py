import csv
import json

json_path = "/Users/mac/Desktop/web/frontend/leetcode/random/bank_list.json"

# Read JSON data from file
with open(json_path, 'r') as json_file:
    data = json.load(json_file)

# Specify CSV file name
csv_file_name = 'output.csv'

# Write CSV file
with open(csv_file_name, 'w', newline='') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Write header
    header = data[0].keys()
    csv_writer.writerow(header)

    # Write data
    for row in data:
        csv_writer.writerow(row.values())

print(f'CSV file "{csv_file_name}" created successfully.')
