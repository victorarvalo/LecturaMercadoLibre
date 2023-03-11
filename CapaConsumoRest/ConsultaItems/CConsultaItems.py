#Esta clase se encarga de hacer el consumo del endpoint Items de Mercado Libre
import json

import requests as requests
from CapaDatos.Modelos.MConfigLectura import DataArchivo, BodyItems
from CapaPresentacion.app.ConfigLectura.schema import BodyItemsSchema

class ConsultaItems:

    def consultarItems(self):
        cantidadRegistros = DataArchivo.contar_registros()
        contadorRegistros = 1
        body_items = []
        while contadorRegistros <= cantidadRegistros:
            #obtenemos 100 registros
            dataArchivos = DataArchivo.obtener_rango_ids_no_vacias(contadorRegistros, (contadorRegistros + 101))
            for data in dataArchivos:
                # Realizamos la consulta de Items
                str_consulta = 'https://api.mercadolibre.com/items?ids=' + data.llave
                resultado = requests.get(str_consulta)
                # Creamos json con el texto de la respuesta
                json_resultado = json.loads(resultado.text)
                # Obtenemos el diccionario de body
                body_diccionario = json_resultado[0].get('body')
                # Creamos el objeto BodyItems
                body_item = BodyItems(
                    validarDatos('id',body_diccionario.get('id')),
                    validarDatos('price',body_diccionario.get('price')),
                    validarDatos('start_time',body_diccionario.get('start_time')),
                    validarDatos('category_id',body_diccionario.get('category_id')),
                    validarDatos('currency_id',body_diccionario.get('currency_id')),
                    validarDatos('seller_id',body_diccionario.get('seller_id'))
                 )
                body_items.append(body_item)
            break
        print(len(body_items))

def validarDatos(item, valor):
    #Validamos el campo id, start_time, category_id, currency_id
    if item == 'id' or item == 'start_time' or item == 'category_id' or item == 'currency_id':
        if isinstance(valor, str):
            return valor
        else:
            return None
    #Validamos el campo price y seller_id
    if item == 'price' or item == 'seller_id':
        if isinstance(valor, float) or isinstance(valor, int):
            return valor
        else:
            return None
