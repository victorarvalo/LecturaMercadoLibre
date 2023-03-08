# Modelo de recolección de datos a guardar en la base de datos
from ...CapaDatos import db
from ...CapaDatos.db import ModeloBase

class DataCollection(db.Model, ModeloBase):

    id_data_collection = db.Column(db.Integer, primary_key = True)
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