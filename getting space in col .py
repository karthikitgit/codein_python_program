import csv

# Custom input file path
input_file_path = 'C:\\Users\\JESUS CHRIST\\OneDrive\\Desktop\\sample.data.csv'

# Custom output file path
output_file_path = 'C:\\Users\\JESUS CHRIST\\OneDrive\\Desktop\\csv\\sorted_text_file.txt'

# Read the CSV file into a list of dictionaries
data = []
with open(input_file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(row)

# Sort the data based on multiple columns: 'Firstnm', 'Lastnm', and 'phonenumber'
sorted_data = sorted(data, key=lambda x: (x['Firstnm'], x['Lastnm'], x['phonenumber']))

# Write the sorted data to a new text file, replacing commas with spaces
with open(output_file_path, mode='w', newline='') as file:
    fieldnames = ['Firstnm', 'Lastnm', 'phonenumber']
    for row in sorted_data:
        formatted_row = ' '.join([row[field].replace(',', '') for field in fieldnames])
        file.write(formatted_row + '\n')

print(f"Data sorted based on 'Firstnm', 'Lastnm', and 'phonenumber' without commas has been written to {output_file_path}")
