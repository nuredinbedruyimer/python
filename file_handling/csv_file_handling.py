import csv


with open('/home/nuredin/Documents/python/file_handling/sample_data.csv', "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)