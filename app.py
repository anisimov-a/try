from flask import Flask

app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
    return "index"

@app.route("/about")
def about():
    return "<h1>Про сайт</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=False, debug=True)

