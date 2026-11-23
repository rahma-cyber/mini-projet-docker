import os
from flask import Flask

app = Flask(__name__)

MESSAGE = os.getenv("APP_MESSAGE", "Bienvenue sur l'application conteneurisée !")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

@app.route("/")
def home():
    return f"<h1>{MESSAGE}</h1><p>Version : {APP_VERSION}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
