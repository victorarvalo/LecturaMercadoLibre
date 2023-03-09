from flask import Flask
from CapaDatos.db import db
from .ConfigLectura.ConfigLectura import config_lectura_bp
from .DatosArchivo.DatosArchivo import datos_archivo_bp
from .ext import ma, migrate


def create_app(settings_module):
    app = Flask(__name__)
    app.config.from_object(settings_module)
    # Inicializa las extensiones
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    # Deshabilita el modo estricto de acabado de una URL con /
    app.url_map.strict_slashes = False
    # Registra los blueprints
    app.register_blueprint(datos_archivo_bp)
    app.register_blueprint(config_lectura_bp)
    return app
