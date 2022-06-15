# CSV File
# extension - .csv
# CSV stands for Comma Seperated Value
# All the data in this file are comma seperated

import csv

rows = []
with open("DS290422-Python-Bharati\\csv_file_handling\\test.csv",'r') as file:
    data = csv.reader(file)
    
    header = next(data)
    print(header)

    for row in data:
        rows.append(row)

    print(rows)

    print(f"Rows Count : {data.line_num}")

for i in rows[:2]:
    print(i)