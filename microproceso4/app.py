from flask import Flask, jsonify, abort
import requests
import json

app4 = Flask(__name__)

@app4.route('/<int:municipioid>/<string:parametro1>/<string:parametro2>', methods=['GET'])
@app4.route('/<int:municipioid>/<string:parametro2>/<string:parametro1>', methods=['GET'])
def get_combined(municipioid, parametro1, parametro2):
    try:
        response = requests.get(f"https://www.el-tiempo.net/api/json/v2/provincias/18/municipios/{municipioid}")
        data = response.json()

        info = {}

        if parametro1 == "municipio" or parametro2 == "municipio":
            info["Provincia"] = data["municipio"]["NOMBRE"]

        if parametro1 == "meteo" or parametro2 == "meteo":
            info["Temperatura"] = data["temperatura_actual"]
            info["Temperatura máxima"] = data["temperaturas"]["max"]
            info["Temperatura mínima"] = data["temperaturas"]["min"]
            info["Humedad"] = data["humedad"]
            info["Viento"] = data["viento"]
            info["Precipitacion"] = data["precipitacion"]
            info["Lluvia"] = data["lluvia"]

        if parametro1 == "demo" or parametro2 == "demo":
            info["POBLACION_MUNI"] = 6191  
            info["POBLACION_CAPITAL"] = 4518
            info["POBLACION_MASC"] = 2000
            info["POBLACION_fem"] = 2518

        if not info:
            abort(400, description="Error 400: Parámetros no válidos.")

        return jsonify(info)

    except Exception as e:
        return jsonify({'error': f'Error inesperado: {str(e)}'}), 500


if __name__ == '__main__':
    app4.run(port=5003)
