from flask import request, Blueprint, render_template, url_for, redirect
from flask_restful import Api, Resource
from CapaPresentacion.app.ConfigLectura.schema import ConfigLecturaSchema
from CapaDatos.Modelos.MConfigLectura import ConfigLectura

config_lectura_bp = Blueprint('config_lectura_bp', __name__,
                             template_folder='templates',
                             static_folder='static', static_url_path='/STATIC/')

config_lectura_schema = ConfigLecturaSchema()

api = Api(config_lectura_bp)

@config_lectura_bp.route('/configlectura/listar', methods=('GET', ))
def listar():
    configuraciones = ConfigLectura.get_all()
    return render_template('ConfigLectura/listar.html', configs=configuraciones)

@config_lectura_bp.route('/configlectura/mostrar/<int:id_configuracion>', methods=('GET', ))
def mostrar(id_configuracion):
    configuracion = ConfigLectura.get_by_id(id_configuracion)
    return render_template('ConfigLectura/mostrar.html', config=configuracion)

@config_lectura_bp.route('/configlectura/crear', methods=('GET','POST'))
def crear():
    if request.method == 'GET':
        return render_template('/configlectura/crear.html')
    else:
        config_lectura = ConfigLectura(
            request.form['formato'],
            request.form['separador'],
            'UTF-8')
        config_lectura.formato = request.form['formato']
        config_lectura.separador = request.form['separador']
        config_lectura.encoding = 'UTF-8'
        # La nueva configuración no debe ser creada como configuración seleccionada
        # la selección de configuración se debe hacer en el método de actualizar
        config_lectura.seleccionado = False
        config_lectura.save()
        return redirect(url_for('config_lectura_bp.listar'))

@config_lectura_bp.route('/configlectura/modificarsseleccionada/<int:id_configuracion>', methods=('GET',))
def modificarseleccionada(id_configuracion):
    #Se obtiene la configuracion seleccionada
    configuracion = ConfigLectura.configuracion_seleccionada()
    if(configuracion is not None):
        #Quitamos la selección de la configuración encontrada
        ConfigLectura.modificar_seleccion(configuracion,False)
    #se obtiene la configuración que deseamos seleccionar
    configuracion = ConfigLectura.get_by_id(id_configuracion)
    #se selecciona la nueva configuración
    ConfigLectura.modificar_seleccion(configuracion,True)
    return render_template('ConfigLectura/mostrar.html', config=configuracion)