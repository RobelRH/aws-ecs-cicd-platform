import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "local")
COMMIT_SHA = os.getenv("COMMIT_SHA", "local")


@app.route("/")
def home():
    return f"""
    <html>
      <head>
        <title>Cloud Deployment Platform</title>
      </head>
      <body>
        <h1>Cloud Deployment Platform</h1>
        <p><strong>Status:</strong> Healthy</p>
        <p><strong>Version:</strong> {APP_VERSION}</p>
        <p><strong>Commit:</strong> {COMMIT_SHA}</p>
      </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(
        status="healthy",
        version=APP_VERSION
    )


@app.route("/api/version")
def version():
    return jsonify(
        version=APP_VERSION,
        commit=COMMIT_SHA
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)