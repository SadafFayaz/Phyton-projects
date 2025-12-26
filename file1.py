# 2. Read CSV file and print each row
import csv
with open("data.csv", "r") as file:
    r = csv.reader(file)
    for row in r:
        print(row)
