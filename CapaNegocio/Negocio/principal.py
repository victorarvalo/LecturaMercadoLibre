#Script Principal de Lectura de Archivo
from CapaNegocio.Negocio.LecturaArchivo.LecturaCSV import LecturaCSV
ubicacion_archivo = 'C:/Users/Victor/Downloads/technical_challenge_data.csv'
extencion_archivo = ubicacion_archivo.split('.')
if len(extencion_archivo) > 1:
    if extencion_archivo[1] == 'csv':
        csv = LecturaCSV(ubicacion_archivo)
        csv.lectura()
    elif extencion_archivo[1] == 'txt':
        r = ''
    elif extencion_archivo[1] == 'jsonlines':
        s = ''



