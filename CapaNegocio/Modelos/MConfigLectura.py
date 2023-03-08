#Modelo para la configuración de la lectura de archivos
from ...CapaDatos import db
from ...CapaDatos.db import ModeloBase
class ConfigLectura(db.Model, ModeloBase):

    id = db.Column(db.Integer, primary_key = True)
    formato = db.Column(db.String)
    separador = db.Column(db.String)
    encoding = db.Column(db.String)
    seleccionado = db.Column(db.Bool)

    def __init__(self, formato, separador, encoding):
        self.formato = formato
        self.separador = separador
        self.encoding = encoding
        self.seleccionado = False

