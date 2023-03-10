#Clase para la creación de llaves
from sqlalchemy import update
from sqlalchemy.sql.expression import bindparam
from CapaDatos.Modelos.MConfigLectura import DataArchivo
class CreacionLlaves:

    def crear_llaves(self):
        cantidadRegistros = DataArchivo.contar_registros()
        contadorRegistros = 1
        while contadorRegistros <= cantidadRegistros:
            #obtenemos 100 registros
            dataArchivos = DataArchivo.obtener_rango_ids(contadorRegistros, (contadorRegistros + 99))
            #Creamos la lista para actualizar la tabla en el campo llave
            listDataArchivos = self.crear_lista_diccionarios(dataArchivos)
            for data in listDataArchivos:
                #Actualizamos el registro
                DataArchivo.modificar_llave(data,data.llave)
            contadorRegistros += 100



    def crear_lista_diccionarios(self, dataArchivos):
        listDataArchivos = []
        for data in dataArchivos:
            if self.validar_datos(data):
                llave = data.site + data.id
                data.llave = llave
                listDataArchivos.append(data)
        return  listDataArchivos

    def validar_datos(self, data):
        try:
            numero = int(data.id)
            if data.site == '':
                return False
            return True
        except:
            return False
