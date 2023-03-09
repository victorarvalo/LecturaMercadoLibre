#Modelo para la configuración de la lectura de archivos
from CapaDatos.db import db, ModeloBase, QuerysConfigLectura
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
