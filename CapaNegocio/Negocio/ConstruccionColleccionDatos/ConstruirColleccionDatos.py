#Clase para la creación de llaves
from CapaDatos.Modelos.MConfigLectura import BodyItems, DataArchivo, Category, Currency, Seller, ColleccionDatos


class ConstruirCollecionDatos:

    def construirCollecionDatos(self):
        cantidadRegistros = BodyItems.contar_registros()
        contadorRegistros = 1
        while contadorRegistros <= cantidadRegistros:
            # obtenemos 100 registros
            bodyItems = BodyItems.obtener_rango_ids(contadorRegistros, (contadorRegistros + 99))
            collection_datos_lista = self.crearListaCollectionDatos(bodyItems)
            self.guardarCollectionDatos(collection_datos_lista)
            contadorRegistros += 99
    def crearListaCollectionDatos(self, bodyItems):
        coleccion_datos_lista = []
        for body in bodyItems:
            data_archivo = DataArchivo.buscar_llave(DataArchivo, body.llave)
            categoria = Category.buscar_category_id(body.category_id)
            moneda = Currency.buscar_currency_id(body.currency_id)
            moneda = self.validarMoneda(moneda)
            vendedor = Seller.buscar_selle_id(body.seller_id)
            coleccion_data = ColleccionDatos()
            coleccion_data.site = data_archivo.site
            coleccion_data.id = data_archivo.id
            coleccion_data.price = body.price
            coleccion_data.end_time = body.start_time
            coleccion_data.name = categoria.name
            coleccion_data.description = moneda.description
            coleccion_data.nickname = vendedor.nickname
            coleccion_datos_lista.append(coleccion_data)
        return coleccion_datos_lista

    def guardarCollectionDatos(self, collection_datos_lista):
        for data in collection_datos_lista:
            data.save()

    def validarMoneda(self, dato):
        if dato is not None:
            print(dato)
            return dato
        else:
            return Currency('','')
