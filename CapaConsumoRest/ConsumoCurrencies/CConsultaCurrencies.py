#Esta clase se encarga de hacer el consumo del endpoint Categorias de Mercado Libre
import multiprocessing

from CapaConsumoRest.ConsumoCurrencies.CMultiprocesoCurrency import MultiProcesoCurrency, Tarea
from CapaDatos.Modelos.MConfigLectura import BodyItems, Currency


class ConsultaCurrencies:

    def consultarCurrencie(self):
        # Limpiamos la tabla Currency
        Currency.query.delete()
        # Obtenemos los diferentes Id's de monedas desde la tabla body_items
        currency_id_lista = BodyItems.distinct_currency_id()
        contadorRegistros = 0
        while contadorRegistros <= len(currency_id_lista):
            # obtenemos 20 registros
            currency_id_grupo = currency_id_lista[contadorRegistros:(contadorRegistros + 20)]
            self.consumirCurrency(currency_id_grupo)
            contadorRegistros += 20
        print(currency_id_lista)

    def consumirCurrency(self, currency_id_grupo):
        tareas = multiprocessing.JoinableQueue()
        resultados = multiprocessing.Queue()
        for currency_id in currency_id_grupo:
            tareas.put(Tarea(currency_id))
        con =  MultiProcesoCurrency(tareas, resultados)
        con.start()
        tareas.join()
        cantidad = len(currency_id_grupo)
        listaResultados = []
        while cantidad:
            result = resultados.get()
            if not isinstance(result, str):
                listaResultados.append(result)
            cantidad -= 1
        self.guardarCurrency(listaResultados)

    def guardarCurrency(self, listaResultados):
        for resultado in listaResultados:
            resultado.save()