Proyecto Desafio de Mercado Libre
Desarrollado por: Víctor Manuel Arévalo Fandiño

+++++++++++++++Activación del entorno Virtual++++++++++++++++
En la carpeta principal del proyecto correr en la línea de comandos

source env/Scripts/activate

++++++++++++++Inicialización de la Base de Datos++++++++++++++++++++
En la carpeta principal del proyecto correr en la línea de comandos

flask db init
flask db migrate -m "Initial_db"
flask db upgrade

+++++++++++++Configuración de las variables de entorno de la Aplicación+++++++++++++
En la carpeta principal del proyecto correr en la línea de comandos

export FLASK_APP="entrypoint:app"
export FLASK_ENV="development"
export APP_SETTINGS_MODULE="config.default"

++++++++++Inicio de la aplicación++++++++++++++++++++++
En la carpeta principal del proyecto correr en la línea de comandos

flask run -p 5000


--------------------------------------------------------------------------------------
URL's de la aplicación:

1. Para obtener la lista de los registros de configuración de lectura de archivos
http://127.0.0.1:5000/configlectura/listar
si un registro no se encuentra seleccionado por defecto, aparece el botón seleccionar
el cual genera una petición a la url número 4 para seleccionar la configuración de lectura
de archivo y posteriormente lleva al usuario a la url número 2

2. Para obtener los detalles de un registro de configuración de lectura de archivos
http://127.0.0.1:5000/configlectura/mostrar/<int:id_configuracion>

3.Para crear una configuración de lectura de archivos
http://127.0.0.1:5000/configlectura/crear
Después de crear una nueva configuración el usuario es direccionado a la url número 1

4. Para modificar la configuración de lectura de archivos seleccionada para el procesamiento
http://127.0.0.1:5000/configlectura/modificarsseleccionada/<int:id_configuracion>

5. Para realizar la captura un archivo
http://127.0.0.1:5000/Procesamiento/captura

6. Para guardar una copia del archivo seleccionado en la carpeta Archivos de la aplicación
http://127.0.0.1:5000/ProcesamientoArchivo/procesar

7. Iniciar el procesamiento de la información del archivo
http://127.0.0.1:5000/ProcesamientoArchivo/iniciar
En esta página se muestra el resultado del procedimiento (Error o OK) y el tiempo que duró la ejecución

8. Para ver los registros obtenidos tras el procesamiento del archivo
http://127.0.0.1:5000/ProcesamientoArchivo/ver
Esta página muestra los registros de la tabla ColleccionDatos