from flask import Flask, jsonify, abort
import json

app3 = Flask(__name__)

@app3.route('/<int:municipioid>/demo', methods=['GET'])
def get_demo(municipioid):
    try:
        with open("demo.json", 'r', encoding='utf-8') as file:
            datos_municipio = json.load(file)

        if datos_municipio['municipioid'] == municipioid:
            return jsonify({
                "municipioid": datos_municipio['municipioid'],
                "POBLACION_MUNI": datos_municipio['POBLACION_MUNI'],
                "POBLACION_CAPITAL": datos_municipio['POBLACION_CAPITAL'],
                "POBLACION_MASC": datos_municipio['POBLACION_MASC'],
                "POBLACION_fem": datos_municipio['POBLACION_fem']
            })
        else:
            abort(404, description='Error 404: Municipio no encontrado')

    except Exception as e:
        return jsonify({'error': f'Error al leer el archivo JSON: {str(e)}'}), 500

if __name__ == '__main__':
    app3.run(port=5003)
