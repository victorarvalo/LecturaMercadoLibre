#Modelo para la configuración de la lectura de archivos
from CapaDatos.db import db, ModeloBase, QuerysConfigLectura, QuerysDataArchivos, QuerysBodyItems


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

class DataArchivo(db.Model, ModeloBase, QuerysDataArchivos):

    id_data_archivo = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String)
    id = db.Column(db.String)
    llave = db.Column(db.String)

    def __init__(self, site, id):
        self.site = site
        self.id = id
        self.llave = ''

class BodyItems(db.Model, ModeloBase, QuerysBodyItems):

    id = db.Column(db.Integer, primary_key=True)
    llave = db.Column(db.String)
    price = db.Column(db.Float)
    start_time = db.Column(db.String)
    category_id = db.Column(db.String)
    currency_id = db.Column(db.String)
    seller_id = db.Column(db.Integer)

    def __init__(self, llave, price, start_time, category_id, currency_id, seller_id):
        self.llave = llave
        self.price = price
        self.start_time = start_time
        self.category_id = category_id
        self.currency_id = currency_id
        self.seller_id = seller_id

class Category(db.Model, ModeloBase):

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, id, name):
        self.id = id
        self.name = name

class Currency(db.Model, ModeloBase):

    id = db.Column(db.String, primary_key=True)
    description = db.Column(db.String)

    def __init__(self, id, description):
        self.id = id
        self.description = description