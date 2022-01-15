import os
import json

from flask import Flask

app = Flask(__name__, static_folder="app")


@app.route("/health")
def health():
    return '{"status": "ok"}'


@app.route("/version")
def version():
    return '{"version": "1.0"}'



@app.route("/<path:path>")
def send_file(path):
    return app.send_static_file(path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000')
