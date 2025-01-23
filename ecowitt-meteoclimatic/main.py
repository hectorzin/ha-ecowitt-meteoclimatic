import json
import logging
from flask import Flask, request
import requests
from datetime import datetime
import os

# File paths
json_file = "/data/options.json"

# Load the JSON file
with open(json_file, "r") as f:
    data = json.load(f)

HOME_ASSISTANT_SERVER = data.get("home_assistant_server")
PATH = data.get("path")
HOME_ASSISTANT_PORT = data.get("home_assistant_port")
STATION_CODE = data.get("station_code")
API_KEY = data.get("api_key")
COMPONENT_PORT = 8120
SEND_TO_METEOCLIMATIC=data.get("send_to_meteoclimatic")
DEBUG = data.get("debug", False)

# Configuración inicial
HOME_ASSISTANT_WEBHOOK = f"http://{HOME_ASSISTANT_SERVER}:{HOME_ASSISTANT_PORT}{PATH}"
METEOCLIMATIC_API = "http://api.m11c.net/v2/ew/{station_code}/{api_key}"



logger = logging.getLogger(__name__)

# Configuración del logger
logging.basicConfig(
    level=logging.DEBUG if DEBUG else logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),  # Para imprimir en consola
        logging.FileHandler("/data/app.log")  # Para guardar en un archivo
    ]
)

# Inicializar servidor Flask
app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def receive_data():
    try:
        # Recibir datos enviados por la estación Ecowitt
        data = request.form.to_dict() if request.form else request.args.to_dict()
        logger.debug(f"Datos recibidos: {json.dumps(data)}")

        # Enviar datos a Home Assistant como la propia estación
        try:
            ha_response = requests.post(HOME_ASSISTANT_WEBHOOK, data=data)
            ha_status = ha_response.status_code
            logger.info(f"Enviado a Home Assistant. Estado: {ha_status}")
        except Exception as e:
            logger.error(f"Error enviando a Home Assistant: {e}")
            ha_status = "Error"

        # Enviar datos a Meteoclimatic como la propia estación
        if SEND_TO_METEOCLIMATIC:
            try:
                meteoclimatic_url = METEOCLIMATIC_API.format(station_code=STATION_CODE, api_key=API_KEY)
                mc_response = requests.post(meteoclimatic_url, data=data)
                mc_status = mc_response.status_code
                logger.info(f"Enviado a Meteoclimatic. Estado: {mc_status}")
            except Exception as e:
                logger.error(f"Error enviando a Meteoclimatic: {e}")
                mc_status = "Error"

        # Respuesta al cliente (estación Ecowitt)
        return "OK", 200

    except Exception as e:
        logger.exception("Error procesando datos")
        return "Error interno del servidor", 500

if __name__ == "__main__":
    # Ejecutar el servidor Flask
    app.run(host="0.0.0.0", port=COMPONENT_PORT)
