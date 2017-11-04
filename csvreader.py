import csv
with open('Fantasy Football Data Week 3 - Sheet1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
