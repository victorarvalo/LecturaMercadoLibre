#Esta clase se encarga de hacer el consumo del endpoint Items de Mercado Libre
import json
import multiprocessing

import requests as requests

from CapaConsumoRest.ConsultaItems.CMultiprocesoItems import Tarea, MultiProcesoItems
from CapaDatos.Modelos.MConfigLectura import DataArchivo, BodyItems
from CapaPresentacion.app.ConfigLectura.schema import BodyItemsSchema

class ConsultaItems:

    def consultarItems(self):
        cantidadRegistros = DataArchivo.contar_registros()
        contadorRegistros = 1
        while contadorRegistros <= cantidadRegistros:
            # obtenemos 20 registros
            dataArchivos = DataArchivo.obtener_rango_ids_no_vacias(contadorRegistros, (contadorRegistros + 20))
            self.consumirItems(dataArchivos)
            contadorRegistros += 20

    def consumirItems(self, dataArchivos):
        tareas = multiprocessing.JoinableQueue()
        resultados = multiprocessing.Queue()
        for data in dataArchivos:
            tareas.put(Tarea(data))
        con = MultiProcesoItems(tareas, resultados)
        con.start()
        tareas.join()
        cantidad = len(dataArchivos)
        listaResultados = []
        while cantidad:
            result = resultados.get()
            if not isinstance(result, str):
                listaResultados.append(result)
            cantidad -= 1
        self.guardarBodyItems(listaResultados)

    def guardarBodyItems(self, lista_resultados):
        for resultado in lista_resultados:
            resultado.save()