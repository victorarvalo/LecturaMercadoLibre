# Clase para lectura de archivos CSV
import csv
from CapaDatos.Modelos.MConfigLectura import DataArchivo
from CapaNegocio.Negocio.CValidarConfiguracion import ValidarConfiguracion
class LecturaCSV:

    def __init__(self, ubicacion_archivo):
        self.ubicacion_archivo = ubicacion_archivo
        self.cantidad_registros_guardar = 100
    def lectura(self):

        with open(self.ubicacion_archivo, newline='') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            spamreader = csv.reader(csvfile, dialect=dialect)
            contador = 0
            listaDatos = []
            for row in spamreader:
                listaDatos.append(DataArchivo(row[0], row[1]))
                contador += 1
                if contador == self.cantidad_registros_guardar:
                    DataArchivo.guardar_todos(listaDatos)
                    listaDatos = []
                    contador = 0
            #Guardamos los registros faltantes
            DataArchivo.guardar_todos(listaDatos)