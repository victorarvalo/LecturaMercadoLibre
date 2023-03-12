import datetime
import os

from flask import Blueprint, render_template, request
from flask_restful import Api
from werkzeug.utils import secure_filename
import CapaNegocio.Negocio.principal

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
        #Obtenemos el nombre del archivo a procesar
        filename = request.form['filename']
        #Obtenemos el path del archivo a procesar
        path = os.path.join('Archivos', filename)
        fecha_inicial = datetime.datetime.now()
        CapaNegocio.Negocio.principal.procesamiento(path)
        CapaNegocio.Negocio.principal.consumirAPIMercadoLibreItem()
        CapaNegocio.Negocio.principal.consumirAPIMercadoLibreCategoria()
        CapaNegocio.Negocio.principal.consumirAPIMercadoLibreMonedas()
        CapaNegocio.Negocio.principal.consumirAPIMercadoLibreUsuarios()
        CapaNegocio.Negocio.principal.construirDataCollection()
        fecha_final = datetime.datetime.now()
        diferencia = fecha_final - fecha_inicial
        return render_template('ProcesamientoArchivo/iniciar.html', tiempo=diferencia)


