# Clase para lectura de archivos CSV
import csv
from CapaNegocio.Negocio.CValidarConfiguracion import ValidarConfiguracion
class LecturaCSV:

    def __init__(self, ubicacion_archivo):
        self.ubicacion_archivo = ubicacion_archivo

    def lectura(self):
        with open(self.ubicacion_archivo, newline='') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            spamreader = csv.reader(csvfile, dialect=dialect)
            for row in spamreader:
                try:
                    if isinstance(int(row[1]),int):
                        print(', '.join(row))
                except:
                    continue