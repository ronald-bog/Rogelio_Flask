from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def index():
    return "HOLA"

if __name__ == "__main__":
    app.run(host="127.0.0.96", port=3996, debug=True)