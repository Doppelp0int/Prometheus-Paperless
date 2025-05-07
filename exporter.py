from flask import Flask, Response
import requests

app = Flask(__name__)

# Konfiguriere deine Paperless-URL und API-Token
PAPERLESS_URL = "PAPERLESSURL//api/documents/"
PAPERLESS_TOKEN = "API-KEY"

@app.route("/metrics")
def metrics():
    try:
        res = requests.get(PAPERLESS_URL, headers={"Authorization": f"Token {PAPERLESS_TOKEN}"})
        res.raise_for_status()
        data = res.json()
        count = data["count"]
        return Response(f"paperless_documents_total {count}\n", mimetype="text/plain")
    except Exception as e:
        return Response(f"# Error: {str(e)}\n", mimetype="text/plain", status=500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
