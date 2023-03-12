#Esta clase se encarga de realizar el multiprocesamiento de las consultas a la API
import json
import multiprocessing

import requests

from CapaDatos.Modelos.MConfigLectura import BodyItems


class MultiProcesoItems(multiprocessing.Process):

    def __init__(self, tareas_cola, resultados_cola):
        multiprocessing.Process.__init__(self)
        self.tareas_cola = tareas_cola
        self.resultados_cola = resultados_cola

    def run(self):
        while True:
            siguiente_tareas = self.tareas_cola.get()
            if siguiente_tareas is None:
                break
            resultado = siguiente_tareas()
            self.tareas_cola.task_done()
            self.resultados_cola.put(resultado)


class Tarea:

    def __init__(self, data):
        self.data = data

    def __call__(self):
        # Realizamos la consulta de Items
        str_consulta = 'https://api.mercadolibre.com/items?ids=' + self.data.llave
        resultado = requests.get(str_consulta)
        # Creamos json con el texto de la respuesta
        json_resultado = json.loads(resultado.text)
        #Obtenemos el código de la respuesta
        codigo = json_resultado[0].get('code')
        if codigo == 200:
            # Obtenemos el diccionario de body
            body_diccionario = json_resultado[0].get('body')
            # Creamos el objeto BodyItems
            body_item = BodyItems(
                self.validarDatos('id', body_diccionario.get('id')),
                self.validarDatos('price', body_diccionario.get('price')),
                self.validarDatos('start_time', body_diccionario.get('start_time')),
                self.validarDatos('category_id', body_diccionario.get('category_id')),
                self.validarDatos('currency_id', body_diccionario.get('currency_id')),
                self.validarDatos('seller_id', body_diccionario.get('seller_id'))
            )
            return body_item
        else:
            return f'Error al consumir con llave {self.data.llave}'


