from flask import Flask,request,jsonify
import requests
from requests.exceptions import ConnectTimeout, HTTPError
import logging
import os

app=Flask(__name__)

host = os.environ.get('WEATHER_SERVICE_HOST')
port = os.environ.get('WEATHER_SERVICE_PORT')

WEATHER_SERVICE_URL = f"http://{host}:{port}"
@app.route("/report",methods=["GET"])
def report():
    city = request.args.get("city", "kochi")
    try:
        response = requests.get(f"{WEATHER_SERVICE_URL}/weather?city={city}",timeout=5)
        response.raise_for_status()
        data=response.json()
        temperature = data["temperature"]
        description = data["description"]

        if "rain" in description:
            recomendation = "Its raining take an umbrella or raincoat"
        elif "snow" in description:
            recomendation = "Its snowing take a jacket 🧥"
        elif "overcast cloud" in description:
            recomendation = "There might be chances for rain carry umbrella or raincoat"
        elif temperature > 34:
            recomendation = "The temperature is too high! Stay hydrated"
        else:
            recomendation = "Have a good day! Temperature is pleasant"
        return jsonify(city=city, summary=description, recomendation=recomendation)
    except HTTPError as e:
        logging.error(e)
        return jsonify({"error": "Weather service unavailable"}), 503
    except ConnectTimeout as e:
        logging.error(e)
        return jsonify({"error": "Weather service timeout"}), 504
    except Exception as e:
        logging.error(e)
        return jsonify({"error": "Weather service unavailable"}), 500
@app.route("/health",methods=["GET"])
def health():
    logging.info("Health check green!")
    return jsonify(status="Healthy")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081,debug=True)


