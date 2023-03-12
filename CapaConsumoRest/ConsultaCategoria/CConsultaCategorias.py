#Esta clase se encarga de hacer el consumo del endpoint Categorias de Mercado Libre
import multiprocessing

from CapaDatos.Modelos.MConfigLectura import BodyItems


class ConsultaCategorias:

    def consultarCategoria(self):
        #Obtenemos los diferentes Id's de categorias desde la tabla body_items
        category_id_lista = BodyItems.distintc_columna('category_id')
        contadorRegistros = 0
        while contadorRegistros <= len(category_id_lista):
            #obtenemos 20 registros
            category_id_grupo = category_id_lista[contadorRegistros:(contadorRegistros + 20)]
            break

    def consumirCategory(self, category_id_grupo):
        tareas = multiprocessing.JoinableQueue()
        resultados = multiprocessing.Queue()
        for data in category_id_grupo:
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
