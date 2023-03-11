import datetime

from flask import request, Blueprint, render_template, url_for, redirect
from flask_restful import Api

import CapaNegocio.Negocio.principal
from CapaPresentacion.app.ConfigLectura.schema import DataArchivoSchema
from CapaDatos.Modelos.MConfigLectura import DataArchivo

datos_archivo_bp = Blueprint('datos_archivo_bp', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='/STATIC/')

datos_archivo_schema = DataArchivoSchema()

api = Api(datos_archivo_bp)

@datos_archivo_bp.route('/DatosArchivos/guardar', methods=('GET',))
def guardar():
    fecha_inicial = datetime.datetime.now()
    ubicacion_archivo = 'C:/Users/Victor/Downloads/technical_challenge_data.csv'
    #CapaNegocio.Negocio.principal.procesamiento(ubicacion_archivo)
    CapaNegocio.Negocio.principal.consumirAPIMercadoLibre()
    fecha_final = datetime.datetime.now()
    diferencia = fecha_final - fecha_inicial
    return render_template('DatosArchivos/guardar.html', tiempo=diferencia)
