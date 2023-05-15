"""This file contains all functions that assist the unit tests"""

import csv


def load_csv_file(self, file_path):
    full_string = ''
    with open(file_path, newline='') as csv_file:
        reader = csv.reader(csv_file, quotechar='"')
        for row in reader:
            full_string = full_string + ' '.join(row)
