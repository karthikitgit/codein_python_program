import csv

# Custom input file path
input_file_path = 'C:\\Users\\JESUS CHRIST\\OneDrive\\Desktop\\sample.data.csv'

# Process the input data and create rows for the CSV
with open(input_file_path, mode='r') as file:
    input_data = file.readlines()

data = [line.strip().split(',') for line in input_data]

# Custom output file path
output_file_path = 'C:\\Users\\JESUS CHRIST\\OneDrive\\Desktop\\csv\\text_file.txt'

# Write the formatted data to a CSV file at the specified output path with spaces between columns
with open(output_file_path, mode='w', newline='') as file:
    csv_writer = csv.writer(file, delimiter='\t')
    for row in data:
        # Join columns with spaces between each column
        formatted_row = ' '.join(row)
        csv_writer.writerow([formatted_row])

print(f"Formatted data with spaces has been written to {output_file_path}")
