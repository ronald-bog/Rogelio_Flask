from flask import Blueprint

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/hello")
def index():
    return "HOLA"
