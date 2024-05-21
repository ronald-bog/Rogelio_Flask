from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/hello")
def index():
    return "HOLA"


@app.route("/form")
def formulario():
    base = "Rogelio"
    return render_template("index.html", base=base)


@app.route("/procesarF", methods=["POST"])
def procesarF():
    nombre = request.form["nombrexyz"]
    entero = int(nombre)
    tipo = type(entero).__name__
    return f"El tipo de dato es:  {tipo}"


@app.route("/procesarUnico", methods=["GET", "POST"])
def procesarU():
    nombre = None
    if request.method == "POST":
        nombre = request.form["nombre"]
    return render_template("index.html", nombre=nombre)


if __name__ == "__main__":
    app.run(host="127.0.0.96", port=3996, debug=True)

    #
