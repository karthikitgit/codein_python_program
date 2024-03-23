import csv

# Provided data
input_data = [
    "Firstnm,Lastnm,phonenumber",
    "gunda,kishore,98574222",
    "sai,karthik,54565655",
    "naveen,kumar,41456161",
    "bala,krishna,56161616"
]

# Process the input data and create rows for the CSV
data = [line.split(',') for line in input_data]

# Custom output file path
output_file_path = 'C:\\Users\\JESUS CHRIST\\OneDrive\\Desktop\\csv\\text_file.txt'


with open(output_file_path, mode='w', newline='') as file:
    csv_writer = csv.writer(file, delimiter='\t')
    for row in data:
        # Join columns with spaces between each column
        formatted_row = ' '.join(row)
        csv_writer.writerow([formatted_row])

print(f"Formatted data with spaces has been written to {output_file_path}")
