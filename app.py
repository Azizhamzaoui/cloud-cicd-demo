from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "local")


@app.route("/")
def home():
    return jsonify({
        "message": "Hello from CI/CD pipeline",
        "environment": APP_ENV,
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
