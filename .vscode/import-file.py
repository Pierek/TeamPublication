import csv

FUNDING = 'C:\\Temp\\test.csv'

def read_funding_data(path):
    with open(path, 'rU') as data:
        reader = csv.DictReader(data)
        for row in reader:
            yield row

if __name__ == "__main__":
    for idx, row in enumerate(read_funding_data(FUNDING)):
        if idx > 10: break
        print (row)