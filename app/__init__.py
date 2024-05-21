from flask import Flask

app = Flask(__name__)

from app.main.routes import main
from app.main.routes2 import main2

app.register_blueprint(main)
app.register_blueprint(main2)
