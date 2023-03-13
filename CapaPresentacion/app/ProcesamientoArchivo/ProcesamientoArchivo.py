import datetime
import os

from flask import Blueprint, render_template, request
from flask_restful import Api
from werkzeug.utils import secure_filename
import CapaNegocio.Negocio.principal
from CapaDatos.Modelos.MConfigLectura import ConfigLectura, ColleccionDatos

procesamiento_archivo_bp = Blueprint('procesamiento_archivo_bp', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='/STATIC/')

api = Api(procesamiento_archivo_bp)

@procesamiento_archivo_bp.route("/Procesamiento/captura")
def cargar_archivo():
    return render_template('ProcesamientoArchivo/captura.html')

@procesamiento_archivo_bp.route("/ProcesamientoArchivo/procesar", methods=['POST'])
def procesar_archivo():
    if request.method == 'POST':
        #Obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        # Guardamos el archivo en el directorio "Archivos PDF"
        f.save(os.path.join('Archivos', filename))
        return render_template("/ProcesamientoArchivo/procesar.html", filename=filename)

@procesamiento_archivo_bp.route("/ProcesamientoArchivo/iniciar", methods=['POST'])
def iniciar_archivo():
    if request.method == 'POST':
        respuesta = []
        fecha_inicial = datetime.datetime.now()
        #Obtenemos la configuración del archivo para validar
        configuracion_archivo = ConfigLectura.configuracion_seleccionada()
        if configuracion_archivo is None:
            resultado = 'No hay una configuración seleccionada'
            fecha_final = datetime.datetime.now()
            diferencia = fecha_final - fecha_inicial
            respuesta.append(diferencia)
            respuesta.append(resultado)
            return render_template('ProcesamientoArchivo/iniciar.html', respuestas=respuesta)
        #Obtenemos el nombre del archivo a procesar
        filename = request.form['filename']
        #Obtenemos el path del archivo a procesar
        path = os.path.join('Archivos', filename)
        resultado = CapaNegocio.Negocio.principal.procesamiento(path, configuracion_archivo)
        if isinstance(resultado, str):
            fecha_final = datetime.datetime.now()
            diferencia = fecha_final - fecha_inicial
            respuesta.append(diferencia)
            respuesta.append(resultado)
            return render_template('ProcesamientoArchivo/iniciar.html', respuestas=respuesta)
        CapaNegocio.Negocio.principal.consumirAPIMercadoLibreItem()
        CapaNegocio.Negocio.principal.consumirAPIMercadoLibreCategoria()
        CapaNegocio.Negocio.principal.consumirAPIMercadoLibreMonedas()
        CapaNegocio.Negocio.principal.consumirAPIMercadoLibreUsuarios()
        CapaNegocio.Negocio.principal.construirDataCollection()
        fecha_final = datetime.datetime.now()
        diferencia = fecha_final - fecha_inicial
        respuesta.append(diferencia)
        respuesta.append(resultado)
        return render_template('ProcesamientoArchivo/iniciar.html', respuestas=respuesta)

@procesamiento_archivo_bp.route("/ProcesamientoArchivo/ver")
def ver_registros():
    #Obtenemos todos los registros de la tabla CollecionDatos
    colecciones_datos = ColleccionDatos.get_all()
    return render_template('/ProcesamientoArchivo/ver.html', registros=colecciones_datos)