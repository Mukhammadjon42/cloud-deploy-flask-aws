from flask import Flask, request
import os, socket

app = Flask(__name__)

@app.get("/")
def root():
    return {
        "service": "flask-cloud-starter",
        "host": socket.gethostname(),
        "env": os.environ.get("APP_ENV", "dev")
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/echo")
def echo():
    try:
        payload = request.get_json(force=True, silent=False)
    except Exception as e:
        return {"error": str(e)}, 400
    return {"received": payload}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
