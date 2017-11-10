import csv

def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    results = []
    for row in reader:
        results.append(row)
        results



csv_path = "Fantasy Football Data Week 1 - Sheet1.csv"

with open(csv_path, "r+") as f_obj:
    csv_reader(f_obj)
