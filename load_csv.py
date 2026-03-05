import csv

FILE_PATH = 'events-1.csv'

def load_csv(file_path):
    items = []

    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append(row)
    return items

# print(load_csv(FILE_PATH))