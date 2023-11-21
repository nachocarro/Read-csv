import csv

import charts

import utils

def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter =",")     
        header = next(reader)
        #print(header)
        data = []
        for row in reader:
            iterable = zip(header, row)                                               #crea tuplas clave, valor
            country_dict = {key: value for (key, value) in iterable}
            data.append(country_dict)
        return data

if __name__ == "__main__":
    data = read_csv("/home/ignaciomcarro/Proyectos-python/Leer-csv/data.csv")