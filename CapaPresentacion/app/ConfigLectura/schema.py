from marshmallow import fields
from CapaPresentacion.app.ext import ma

class ConfigLecturaSchema(ma.Schema):

    id = fields.Integer(dump_only=True)
    formato = fields.String()
    separador = fields.String()
    encoding = fields.String()
    seleccionado = fields.Boolean()
