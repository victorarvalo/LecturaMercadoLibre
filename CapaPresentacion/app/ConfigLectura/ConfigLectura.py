from flask import request, Blueprint, render_template
from flask_restful import Api, Resource
from CapaPresentacion.app.ConfigLectura.schema import ConfigLecturaSchema
from CapaDatos.Modelos.MConfigLectura import ConfigLectura

config_lectura_bp = Blueprint('config_lectura_bp', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='/STATIC/')

config_lectura_schema = ConfigLecturaSchema()

api = Api(config_lectura_bp)

@config_lectura_bp.route('/', methods=('GET', ))
def listar():
    configuraciones = ConfigLectura.get_all()
    return render_template('ConfigLectura/listar.html', configs=configuraciones)

@config_lectura_bp.route('/mostrar/<int:id_configuracion>', methods=('GET', ))
def mostrar(id_configuracion):
    configuracion = ConfigLectura.get_by_id(id_configuracion)
    return render_template('ConfigLectura/mostrar.html', config=configuracion)
