import csv

def read_data():
    reader = csv.reader(open('./input.csv','r'))
    # header = list(reader)[0]
    # data = []
    data = [row for row in reader]
    header = data[0]
    return header,data[1:]

print(read_data())

