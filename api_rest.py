from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

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

# Ruta para actualizar un elemento en la tabla por su ID
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    cursor = db.cursor()
    cursor.execute("UPDATE tu_tabla_mysql SET nombre = %s, descripcion = %s WHERE id = %s", (data['nombre'], data['descripcion'], item_id))
    db.commit()
    cursor.close()
    return jsonify({"message": "Elemento actualizado correctamente"})

# Uso: Envia una solicitud PUT a /api/items/{id} con los datos a actualizar en el cuerpo de la solicitud en formato JSON.
# Ruta para eliminar un elemento de la tabla por su ID
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM tu_tabla_mysql WHERE id = %s", (item_id,))
    db.commit()
    cursor.close()
    return jsonify({"message": "Elemento eliminado correctamente"})

# Uso: Envía una solicitud DELETE a /api/items/{id} para eliminar un elemento por su ID.


if __name__ == '__main__':
    app.run(debug=True)
