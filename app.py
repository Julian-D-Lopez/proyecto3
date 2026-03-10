from flask import Flask, jsonify, render_temqplate
from backend import cargar_localidad, obtener_sitp, obtener_info
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/api/localidad")
def api_localidad():
    return jsonify(cargar_localidad())

@app.route("/api/sitp")
def api_sitp():
    return jsonify(obtener_sitp())

@app.route("/api/info")
def api_info():
    return jsonify(obtener_info())
if __name__ == "__main__":
    app.run(debug=True)