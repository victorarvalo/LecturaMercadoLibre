#Script Principal de Lectura de Archivo
from CapaNegocio.Negocio.LecturaArchivo.LecturaCSV import LecturaCSV
from CapaNegocio.Negocio.CreacionLlaves.CreacionLlaves import CreacionLlaves
from CapaConsumoRest.ConsultaItems.CConsultaItems import  ConsultaItems
def procesamiento(ubicacion_archivo):
    # realizar la lectura del archivo y escritura de datos en la base de datos
    leerYGuardarDatos(ubicacion_archivo)
    #Creación de llaves para consumo de API Mercado Libre
    creacion_llaves = CreacionLlaves()
    creacion_llaves.crear_llaves()
def leerYGuardarDatos(ubicacion_archivo):
    extencion_archivo = ubicacion_archivo.split('.')
    if len(extencion_archivo) > 1:
        if extencion_archivo[1] == 'csv':
            csv = LecturaCSV(ubicacion_archivo)
            # Pendiente hacer la validación de configuraciones
            csv.lectura()
        elif extencion_archivo[1] == 'txt':
            r = ''
        elif extencion_archivo[1] == 'jsonlines':
            s = ''

def consumirAPIMercadoLibre():
    consulta_items = ConsultaItems()
    consulta_items.consultarItems()
