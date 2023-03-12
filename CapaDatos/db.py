# Creación de objeto db de SQLAlchemy y clase ModeloBase
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import between
from sqlalchemy.orm import load_only

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
    @classmethod
    def obtener_rango_ids(self, id_inicial, id_final):
        return db.session.query(self).where(between(self.id_data_archivo,id_inicial,id_final)).all()

    @classmethod
    def obtener_rango_ids_no_vacias(self, id_inicial, id_final):
        return db.session.query(self)\
            .where((between(self.id_data_archivo, id_inicial, id_final)) &
                   (self.llave != ''))\
            .all()

    @classmethod
    def modificar_llave(cls, dataArchivo, valor):
        dataArchivo.llave = valor
        db.session.commit()
    @classmethod
    def contar_registros(cls):
        return db.session.query(cls).count()

class QuerysBodyItems:

    @classmethod
    def guardar_item_todos(cls, instancias):
        db.session.add_all(instancias)
        print(f'inst: {instancias}, len: {len(instancias)}')
        db.session.commit

    @classmethod
    def distintc_category_id(cls):
        lista_tuplas_category_ids = db.session.query(cls.category_id).distinct().all()
        lista_category_ids = []
        for tupla in lista_tuplas_category_ids:
            lista_category_ids.append(tupla[0])#Solo tomamos el primer valor de la tupla
        return  lista_category_ids

    @classmethod
    def distinct_currency_id(cls):
        lista_tuplas_currency_ids = db.session.query(cls.currency_id).distinct().all()
        lista_currency_ids = []
        for tupla in lista_tuplas_currency_ids:
            #no tomamos los currency_id vacios
            if tupla[0] != '':
                lista_currency_ids.append(tupla[0])#Solo tomamos el primer valor de la tupla
        return lista_currency_ids