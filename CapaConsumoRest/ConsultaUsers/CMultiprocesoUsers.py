#Esta clase se encarga de realizar el multiprocesamiento de las consultas a la API
import json
import multiprocessing

import requests

from CapaDatos.Modelos.MConfigLectura import Seller


class MultiProcesoUser(multiprocessing.Process):

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

    def __init__(self, seller_id):
        self.seller_id = seller_id

    def __call__(self):
        # Realizamos la consulta de Category
        str_consulta = f'https://api.mercadolibre.com/users/{self.seller_id}'
        resultado = requests.get(str_consulta)
        # Creamos json con el texto de la respuesta
        json_resultado = json.loads(resultado.text)
        # Obtenemos el código de la respuesta
        if resultado.status_code == 200:
            # Creamos el objeto Category
            seller = Seller
            category = Seller(json_resultado.get('id'), json_resultado.get('nickname'))
            return category
        else:
            return f'Error al consumir con id {self.seller_id}'



