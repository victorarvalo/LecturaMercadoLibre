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
