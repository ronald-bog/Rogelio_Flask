from flask import Blueprint, render_template, request

main2 = Blueprint("main2", __name__)


@main2.route("/form")
def formulario():
    base = False
    lista = [
        "Rogelio",
        "Ana",
        "Sofia",
        "Luis",
        "Nestor",
        "Vicente",
        "sgsdfg",
        "yhrty",
        "iki",
        "fdgdf",
        "rtyuty",
        "tyutyu",
        "56456",
        "574",
        "gujyt",
        "ghj",
        "ghjgh",
        "ghjk",
    ]
    nuevaVar = True
    return render_template("index.html", base=base, arreglo=lista, nuevaVar=nuevaVar)


@main2.route("/procesarF", methods=["POST"])
def procesarF():
    nombre = request.form["nombrexyz"]
    entero = int(nombre)
    tipo = type(entero).__name__
    return f"El tipo de dato es: {tipo}"


@main2.route("/procesarUnico", methods=["GET", "POST"])
def procesarU():
    nombre = None
    if request.method == "POST":
        nombre = request.form["nombre"]
    return render_template("index.html", nombre=nombre)
