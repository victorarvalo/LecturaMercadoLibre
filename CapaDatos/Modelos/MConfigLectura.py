#Modelo para la configuración de la lectura de archivos
from CapaDatos.db import db, ModeloBase, QuerysConfigLectura, QuerysDataArchivos,\
    QuerysBodyItems, QuerysCategory, QueryCurrency, QuerySeller


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

class Category(db.Model, ModeloBase, QuerysCategory):

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)

    def __init__(self, id, name):
        self.id = id
        self.name = name

class Currency(db.Model, ModeloBase, QueryCurrency):

    id = db.Column(db.String, primary_key=True)
    description = db.Column(db.String)

    def __init__(self, id, description):
        self.id = id
        self.description = description

class Seller(db.Model, ModeloBase, QuerySeller):

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String)

    def __init__(self, id, nickname):
        self.id = id
        self.nickname = nickname

class ColleccionDatos(db.Model, ModeloBase):

    id_data_collection = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String)
    id = db.Column(db.Integer)
    price = db.Column(db.String)
    end_time = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.String)
    nickname = db.Column(db.String)

    def __int__(self, site, id, price, end_time, name, description, nickname):
        self.site = site
        self.id = id
        self.price = price
        self.end_time = end_time
        self.name = name
        self.description = description
        self.nickname = nickname