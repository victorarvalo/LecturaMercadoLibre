import datetime

from flask import Blueprint, render_template
from flask_restful import Api

import CapaNegocio.Negocio.principal
from CapaPresentacion.app.ConfigLectura.schema import DataArchivoSchema

datos_archivo_bp = Blueprint('datos_archivo_bp', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='/STATIC/')

datos_archivo_schema = DataArchivoSchema()

api = Api(datos_archivo_bp)

@datos_archivo_bp.route('/DatosArchivos/guardar', methods=('GET',))
def guardar():
    fecha_inicial = datetime.datetime.now()
    ubicacion_archivo = 'C:/Users/Victor/Downloads/technical_challenge_data.csv'
    CapaNegocio.Negocio.principal.procesamiento(ubicacion_archivo)
    CapaNegocio.Negocio.principal.consumirAPIMercadoLibreItem()
    CapaNegocio.Negocio.principal.consumirAPIMercadoLibreCategoria()
    CapaNegocio.Negocio.principal.consumirAPIMercadoLibreMonedas()
    CapaNegocio.Negocio.principal.consumirAPIMercadoLibreUsuarios()
    CapaNegocio.Negocio.principal.construirDataCollection()
    fecha_final = datetime.datetime.now()
    diferencia = fecha_final - fecha_inicial
    return render_template('DatosArchivos/guardar.html', tiempo=diferencia)
