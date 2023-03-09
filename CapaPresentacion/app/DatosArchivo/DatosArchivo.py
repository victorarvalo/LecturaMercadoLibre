from flask import request, Blueprint, render_template, url_for, redirect
from flask_restful import Api
from CapaPresentacion.app.ConfigLectura.schema import DataArchivoSchema

datos_archivo_bp = Blueprint('datos_archivo_bp', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='/STATIC/')

datos_archivo_schema = DataArchivoSchema()

api = Api(datos_archivo_bp)