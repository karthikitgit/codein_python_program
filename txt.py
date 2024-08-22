import csv

input_file_path = 'C:\\Users\\JESUS CHRIST\\OneDrive\\Desktop\\sample.data.csv'

with open(input_file_path, mode='r') as file:
    input_data = file.readlines()

data = [line.strip().split(',') for line in input_data]

output_file_path = 'C:\\Users\\JESUS CHRIST\\OneDrive\\Desktop\\csv\\text_file.txt'

with open(output_file_path, mode='w', newline='') as file:
    csv_writer = csv.writer(file, delimiter='\t')
    for row in data:
        formatted_row = ' '.join(row)
        csv_writer.writerow([formatted_row])

print(f"Formatted data with spaces has been written to {output_file_path}")
