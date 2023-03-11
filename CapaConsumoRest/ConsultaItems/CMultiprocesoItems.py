#Esta clase se encarga de realizar el multiprocesamiento de las consultas a la API
import multiprocessing
class MultiProcesoItems:

    def __init__(self, tareas_cola, resultados_cola):
        multiprocessing.Process.__init__(self)
        self.tareas_cola = tareas_cola
        self.resultados_cola = resultados_cola

    def run(self):
        pass


class Tarea:

    def __init__(self, dataArchivos):
        self.dataArchivos = dataArchivos


