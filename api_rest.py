from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name)
# Configura la conexión a la base de datos MySQL

db = mysql.connector.connect(
    host="tu_host_mysql",
    user="tu_usuario_mysql",
    password="tu_contraseña_mysql",
    database="tu_base_de_datos_mysql"
)

# Ruta para obtener todos los elementos de la tabla
@app.route('/api/items', methods=['GET'])
def get_items():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tu_tabla_mysql")
    items = cursor.fetchall()
    cursor.close()
    return jsonify(items)
# Ruta para agregar un nuevo elemento a la tabla
@app.route('/api/items', methods=['POST'])
def add_item():
    data = request.json
    cursor = db.cursor()
    cursor.execute("INSERT INTO tu_tabla_mysql (nombre, descripcion) VALUES (%s, %s)", (data['nombre'], data['descripcion']))
    db.commit()
    cursor.close()
    return jsonify({"message": "Elemento agregado correctamente"})


if __name__ == '__main__':
    app.run(debug=True)