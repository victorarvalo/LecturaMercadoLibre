#Script Principal de Lectura de Archivo
from CapaConsumoRest.ConsultaCategoria.CConsultaCategorias import ConsultaCategorias
from CapaConsumoRest.ConsultaUsers.CConsultaUsuarios import ConsultaUsuarios
from CapaConsumoRest.ConsumoCurrencies.CConsultaCurrencies import ConsultaCurrencies
from CapaNegocio.Negocio.ConstruccionColleccionDatos.ConstruirColleccionDatos import ConstruirCollecionDatos
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


