import csv

columns_header = ["name" , "age", "gender"]

rows_data = [
    ["irtiza", "24", "male"],
    ["haroon", "27", "male"]
]

with open("custome_file.csv","w")as f:
    csv_writer = csv.writer(f, delimiter = "|")

    csv_writer.writerow(columns_header)
    csv_writer.writerows(rows_data)

print()

print("now we want to write data in dictionary form so")

columns_data = ["name" , "department" , "reg #"]
rows = [
    {"name" : "irtiza","department": "BSCS", "reg #" : "5945"},
    {"name" : "Haroon","department": "BSSE", "reg #" : "5896"},
    {"name" : "usama","department": "BSCS", "reg #" : "5999"}
]

with open("custom_file2.csv","w")as dict_file:
    dict_file2 = csv.DictWriter(dict_file, fieldnames=columns_data, delimiter = "|" )

    dict_file2.writeheader()
    dict_file2.writerows(rows)