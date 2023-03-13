#Script Principal de Lectura de Archivo
from CapaConsumoRest.ConsultaCategoria.CConsultaCategorias import ConsultaCategorias
from CapaConsumoRest.ConsultaUsers.CConsultaUsuarios import ConsultaUsuarios
from CapaConsumoRest.ConsumoCurrencies.CConsultaCurrencies import ConsultaCurrencies
from CapaNegocio.Negocio.CValidarConfiguracion import ValidarConfiguracion
from CapaNegocio.Negocio.ConstruccionColleccionDatos.ConstruirColleccionDatos import ConstruirCollecionDatos
from CapaNegocio.Negocio.LecturaArchivo.LecturaCSV import LecturaCSV
from CapaNegocio.Negocio.CreacionLlaves.CreacionLlaves import CreacionLlaves
from CapaConsumoRest.ConsultaItems.CConsultaItems import  ConsultaItems
import csv
def procesamiento(ubicacion_archivo, configuracion_archivo):
    # realizar la lectura del archivo y escritura de datos en la base de datos
    mensaje = leerYGuardarDatos(ubicacion_archivo, configuracion_archivo)
    #Validamos si hay mensaje de error
    if isinstance(mensaje, str):
        return mensaje
    #Creación de llaves para consumo de API Mercado Libre
    creacion_llaves = CreacionLlaves()
    creacion_llaves.crear_llaves()
def leerYGuardarDatos(ubicacion_archivo, configuracion_archivo):
    extencion_archivo = ubicacion_archivo.split('.')
    if len(extencion_archivo) > 1:
        if extencion_archivo[1] == 'csv':
            #Realizamos las validaciones del archivo de Excel
            if ValidarConfiguracion.validaFormato(configuracion_archivo.formato, extencion_archivo[1]):
                #Realizamos la lectura del archivo para validar el separador
                with open(ubicacion_archivo, newline='') as csvfile:
                    dialect = csv.Sniffer().sniff(csvfile.read(1024))
                    csvfile.seek(0)
                    if not ValidarConfiguracion.validaSeparador(configuracion_archivo.separador, dialect.delimiter):
                        return 'Separador del archivo erroneo'
            else:
                return 'Formato de archivo erroneo'
            csv_archivo = LecturaCSV(ubicacion_archivo)
            csv_archivo.lectura()
            return None
        elif extencion_archivo[1] == 'txt':
            return None
        elif extencion_archivo[1] == 'jsonlines':
            return None
        else:
            return 'El archivo no tiene una extención valida (.csv - .txt - .jsonlines)'

def consumirAPIMercadoLibreItem():
    consulta_items = ConsultaItems()
    consulta_items.consultarItems()

def consumirAPIMercadoLibreCategoria():
    consulta_categorias = ConsultaCategorias()
    consulta_categorias.consultarCategoria()

def consumirAPIMercadoLibreMonedas():
    consuta_currencies = ConsultaCurrencies()
    consuta_currencies.consultarCurrencie()

def consumirAPIMercadoLibreUsuarios():
    consultar_usuarios = ConsultaUsuarios()
    consultar_usuarios.consultarUsuario()

def construirDataCollection():
    contruir_colleccion_datos = ConstruirCollecionDatos()
    contruir_colleccion_datos.construirCollecionDatos()


