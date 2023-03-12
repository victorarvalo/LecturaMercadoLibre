from marshmallow import fields
from CapaPresentacion.app.ext import ma

class ConfigLecturaSchema(ma.Schema):

    id = fields.Integer(dump_only=True)
    formato = fields.String()
    separador = fields.String()
    encoding = fields.String()
    seleccionado = fields.Boolean()

class DataArchivoSchema(ma.Schema):

    id_data_archivo = fields.Integer(dump_only=True)
    site = fields.String()
    id = fields.String()

class BodyItemsSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    llave = fields.String()
    price = fields.Integer()
    start_time = fields.String()
    category_id = fields.String()
    currency_id = fields.String()
    seller_id = fields.Integer()

class CategorySchema(ma.Schema):
    id = fields.String(dump_only=True)
    name = fields.String()

class CurrencySchema(ma.Schema):
    id = fields.String(dump_only=True)
    description = fields.String()

class SellerSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nickname = fields.String()

class ColleccionDatosSchema(ma.Schema):
    id_data_collection = fields.Integer(dump_only=True)
    site = fields.String()
    id = fields.Integer()
    price = fields.String()
    end_time = fields.String()
    name = fields.String()
    description = fields.String()
    nickname = fields.String()