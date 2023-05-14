import csv


def data_reader(column):
    with open('iris.csv') as data_file:
        reader = csv.DictReader(data_file, skipinitialspace=True)

        x_data = []
        y_data = []

        for row in reader:
            x_data.append(row['species'])
            y_data.append(row[column])

        y_data = map(float, y_data)

        return x_data, list(y_data)
