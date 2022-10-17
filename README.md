Desarrollo de Pruebas de Ingreso para Habi
==========================================
# Herramientas
  Para el desarrolo de esta prueba vamos utilizar el lenguaje de python como se solicita, adicionalmente utilizaremos las sigueintes librerias:
  <ul>
    <li><b>http.serve:</b> Este módulo define clases para implementar servidores HTTP (servidores Web) y utilizaremos las siguientes clases           <b>BaseHTTPRequestHandler</b> y <b>HTTPServer</b>.</li>
  <li><b>BaseHTTPRequestHandler:</b> Esta clase se utiliza para controlar las solicitudes HTTP que llegan al servidor y Esta clase se utiliza para controlar las solicitudes HTTP que llegan al servidor.</li>
  <li><b>HTTPServer:</b>Esta clase se basa en la clase TCPServer almacenando la dirección del servidor como variables de instancia llamadas nombre_del_servidor y puerto_del_servidor. El servidor es accesible por el handler, típicamente a través de la variable de instancia servidor del handler.</li>
  </ul>
  
 # Estructura de Proyecto
 Se utiliza la siguiente estrutura para desarrollar el proyecto:
 <ul>
  <li><b>config:</b>En esta carpeta de crear el archivo contine el archivo de configuracion de la informacion de acceso a la base de datos.</li>
  <li><b>database:</b> En esta carpeta se crea la clase con los metodos para realizar la conexion a la base de datos</li>
  <li><b>htt_handler:</b> En esta carpte ase crea la clase para controlar las solicitus GET y POST que se hagan al desarrollo de nuestros servicios.</li>
  <li><b>models:</b> En esta carpeta de crean las clases para gestionar la informacion de la base de datos.</li>
  <li><b>tests:</b>En esta carpeta se colocaran todas las clases necesarias para poder realizar los test unitarios.</li>
  <li><b>main.py:</b>Desd este archivo se realizara la ejecución del proyecto.</li>
</ul>

# Segundo Requerimiento
Se crear esta tabla para almacenar la informacion de los "Me gusta" para cada uno de los inmubles</br>
CREATE TABLE property_like_history (</br>
  id INT NOT NULL AUTO_INCREMENT,</br>
  auth_user_id INT NOT NULL,</br>
  property_id INT NOT NULL,</br>
  date DATE NOT NULL,</br>
  PRIMARY KEY (id),</br>
  FOREING KEY (auth_user_id) REFERENCES auth_user(id),</br>
  FOREING KEY (property_id) REFERENCES property(id)</br>
 ) TYPE = INNODB;</br>
 Se crear las relaciones con la tabla auth_user para asociar el usuario que da like a la propiedad y conla tabla property para asociar la la propiedad que se quiere dar el "Me Gusta".
