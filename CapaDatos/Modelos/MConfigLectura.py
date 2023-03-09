#Modelo para la configuración de la lectura de archivos
from CapaDatos.db import ModeloBase, QuerysConfigLectura
from CapaPresentacion.app import db
class ConfigLectura(db.Model, ModeloBase, QuerysConfigLectura):

    id = db.Column(db.Integer, primary_key = True)
    formato = db.Column(db.String)
    separador = db.Column(db.String)
    encoding = db.Column(db.String)
    seleccionado = db.Column(db.Boolean)

    def __init__(self, formato, separador, encoding):
        self.formato = formato
        self.separador = separador
        self.encoding = encoding
        self.seleccionado = False

class DataArchivo(db.Model, ModeloBase, QuerysConfigLectura):
    id_data_archivo = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String)
    id = db.Column(db.String)

    def __int__(self, site, id):
        self.site = site
        self.id = id