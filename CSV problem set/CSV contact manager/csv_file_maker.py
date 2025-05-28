import csv

column_header = ["Name", "Phone", "Email"]
row_data = [
    ["irtiza", "03155459124", "irtizaazam@gmail.com"],
    ["usama", "03145467890", "usama@gmail.com"],
    ["haroon", "03345645789", "haroon@gmail.com" ]
]
with open("contacts.csv","w", newline ='')as f:
    file_writer = csv.writer(f, delimiter = ",")

    file_writer.writerow(column_header)
    file_writer.writerows(row_data)
