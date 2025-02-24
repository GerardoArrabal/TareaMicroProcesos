from flask import Flask, jsonify, abort
import requests

app4 = Flask(__name__)

@app4.route('/<int:municipioid>/<string:parametro1>/<string:parametro2>', methods=['GET'])
@app4.route('/<int:municipioid>/<string:parametro2>/<string:parametro1>', methods=['GET'])
def get_combined(municipioid, parametro1, parametro2):
    try:
        # Llamadas a microproceso1 y microproceso2
        meteo_url = f"http://localhost:5000/{municipioid}/geo"
        municipio_url = f"http://localhost:5001/{municipioid}/demo" 

        info = {}

        if parametro1 == "municipio" or parametro2 == "municipio":
            response = requests.get(municipio_url)
            if response.status_code == 200:
                municipio_data = response.json()
                info["Provincia"] = municipio_data.get("Provincia", "No disponible")

        if parametro1 == "meteo" or parametro2 == "meteo":
            response = requests.get(meteo_url)
            if response.status_code == 200:
                meteo_data = response.json()
                info["Temperatura"] = meteo_data.get("Temperatura", "No disponible")
                info["Temperatura máxima"] = meteo_data.get("Temperatura máxima", "No disponible")
                info["Temperatura mínima"] = meteo_data.get("Temperatura mínima", "No disponible")
                info["Humedad"] = meteo_data.get("Humedad", "No disponible")
                info["Viento"] = meteo_data.get("Viento", "No disponible")
                info["Precipitacion"] = meteo_data.get("Precipitacion", "No disponible")
                info["Lluvia"] = meteo_data.get("Lluvia", "No disponible")

        if parametro1 == "demo" or parametro2 == "demo":
            info["POBLACION_MUNI"] = 6191  
            info["POBLACION_CAPITAL"] = 4518
            info["POBLACION_MASC"] = 2000
            info["POBLACION_FEM"] = 2518

        if not info:
            abort(400, description="Error 400: Parámetros no válidos.")

        return jsonify(info)

    except Exception as e:
        return jsonify({'error': f'Error inesperado: {str(e)}'}), 500

if __name__ == '__main__':
    app4.run(port=5003)
