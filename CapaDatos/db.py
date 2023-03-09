# Creación de objeto db de SQLAlchemy y clase ModeloBase
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ModeloBase:

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def simple_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()

class QuerysConfigLectura:
    @classmethod
    def configuracion_seleccionada(cls):
        return cls.query.filter_by(seleccionado=True).first()

    @classmethod
    def modificar_seleccion(cls, configuracion, valor):
        configuracion.seleccionado = valor
        db.session.commit()

class QuerysDataArchivos:
    @classmethod
    def guardar_todos(cls, instancias):
        db.session.add_all(instancias)
        db.session.commit()
