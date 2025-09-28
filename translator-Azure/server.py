from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
CORS(app)  # Libera acesso do front-end (localhost)

# 🔑 Configurações da API da Azure
subscription_key = "sua chave aqui"
endpoint = "O seu ponto de extremidade aqui"
location = "sua localizacao aqui"

def translator_text(text, target_language="pt"):
    path = '/translate'
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(os.urandom(16))
    }

    body = [{ 'text': text }]
    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': target_language
    }

    response = requests.post(constructed_url, params=params, headers=headers, json=body)
    response_json = response.json()

    try:
        return response_json[0]['translations'][0]['text']
    except Exception as e:
        return f"Erro na tradução: {e}"

# 📌 Rota para o front-end chamar
@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")
    target_language = data.get("lang", "pt")

    translated_text = translator_text(text, target_language)
    return jsonify({"translation": translated_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
