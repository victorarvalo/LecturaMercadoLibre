#Esta clase se encarga de hacer el consumo del endpoint Categorias de Mercado Libre
import json
import multiprocessing

import requests

from CapaConsumoRest.ConsultaCategoria.CMultiprocesoCategory import Tarea, MultiProcesoCategory
from CapaDatos.Modelos.MConfigLectura import BodyItems, Category


class ConsultaCategorias:

    def consultarCategoria(self):
        # Obtenemos los diferentes Id's de categorias desde la tabla body_items
        category_id_lista = BodyItems.distintc_category_id()
        contadorRegistros = 0
        while contadorRegistros <= len(category_id_lista):
            # obtenemos 20 registros
            category_id_grupo = category_id_lista[contadorRegistros:(contadorRegistros + 20)]
            self.consumirCategory(category_id_grupo)
            contadorRegistros += 20

    def consumirCategory(self, category_id_grupo):
        tareas = multiprocessing.JoinableQueue()
        resultados = multiprocessing.Queue()
        for category_id in category_id_grupo:
            tareas.put(Tarea(category_id))
        con = MultiProcesoCategory(tareas, resultados)
        con.start()
        tareas.join()
        cantidad = len(category_id_grupo)
        listaResultados = []
        while cantidad:
            result = resultados.get()
            if not isinstance(result, str):
                listaResultados.append(result)
            cantidad -= 1
        self.guardarCategory(listaResultados)

    def guardarCategory(self, listaResultados):
        for resultado in listaResultados:
            resultado.save()