from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "¡Hola, Uso de Docker-compose APP-2 arriba!, cambio al 17-Ene..."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
