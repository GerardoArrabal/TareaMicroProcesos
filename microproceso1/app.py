from flask import Flask, jsonify, abort
import json

app1 = Flask(__name__)

@app1.route('/<int:municipioid>/geo', methods=['GET'])
def get_geo(municipioid):
    try:
        # Leer el archivo municipio.json
        with open("municipio.json",'r', encoding='utf-8') as file:
            datos_municipio = json.load(file)

        # Verificar si el municipioid coincide con el del JSON
        if municipioid != datos_municipio['municipioid']:
            abort(404, description='Error 404: Municipio no encontrado')

        # Si coincide, devolver los datos del JSON
        return jsonify(datos_municipio)

    except Exception as e:
        return jsonify({'error': f'Error al leer el archivo JSON: {str(e)}'}), 500

if __name__ == '__main__':
    app1.run(port=5000)
