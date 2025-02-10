from flask import Flask, jsonify, abort
import requests

app2 = Flask(__name__)

@app2.route('/<int:municipioid>/meteo', methods=['GET'])
def get_meteo(municipioid):
    
    # Realizamos el fetch a la API
    response = requests.get(f"https://www.el-tiempo.net/api/json/v2/provincias/18/municipios/{municipioid}")
    data = response.json()
    info = {
        "Provincia": data["municipio"]["NOMBRE"],
        "Temperatura": data["temperatura_actual"],
        "Temperatura máxima": data["temperaturas"]["max"],
        "Temperatura mínima": data["temperaturas"]["min"],
        "Humedad": data["humedad"],
        "Viento": data["viento"],
        "Precipitacion": data["precipitacion"],
        "Lluvia": data["lluvia"]
    }
    return info

    
if __name__ == '__main__':
    app2.run(port=5001, debug=True)
