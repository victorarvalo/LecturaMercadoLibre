#Clase con funciones de validación de archivo vs configuración de lectura
class ValidarConfiguracion:

    @classmethod
    def validaFormato(cls, formato_archivo, formato):
        if formato_archivo == formato:
            return True
        return False

    @classmethod
    def validaSeparador(cls, separador_archivo, separador):
        if separador_archivo == separador:
            return True
        return False

    @classmethod
    def validaEncoding(cls, encoding_archivo, encoding):
        if encoding_archivo == encoding:
            return True
        return False