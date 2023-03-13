#Esta clase se encarga de hacer el consumo del endpoint Usuarios de Mercado Libre
import json
import multiprocessing

import requests

from CapaConsumoRest.ConsultaUsers.CMultiprocesoUsers import MultiProcesoUser, Tarea
from CapaDatos.Modelos.MConfigLectura import BodyItems, Seller


class ConsultaUsuarios:

    def consultarUsuario(self):
        # Limpiamos la tabla Seller
        Seller.query.delete()
        # Obtenemos los diferentes Id's de usuario desde la tabla body_items
        usuarios_id_lista = BodyItems.distinct_seller_id()
        print(len(usuarios_id_lista))
        contadorRegistros = 0
        while contadorRegistros <= len(usuarios_id_lista):
            # obtenemos 20 registros
            usuarios_id_grupo = usuarios_id_lista[contadorRegistros:(contadorRegistros + 20)]
            self.consumirUser(usuarios_id_grupo)
            contadorRegistros += 20

    def consumirUser(self, usuarios_id_grupo):
        tareas = multiprocessing.JoinableQueue()
        resultados = multiprocessing.Queue()
        for usuario_id in usuarios_id_grupo:
            tareas.put(Tarea(usuario_id))
        con = MultiProcesoUser(tareas, resultados)
        con.start()
        tareas.join()
        cantidad = len(usuarios_id_grupo)
        listaResultados = []
        while cantidad:
            result = resultados.get()
            if not isinstance(result, str):
                listaResultados.append(result)
            cantidad -= 1
        self.guardarUsuarios(listaResultados)

    def guardarUsuarios(self, listaResultados):
        for resultado in listaResultados:
            resultado.save()