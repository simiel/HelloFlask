from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Simiel's first web app in python :)"


app.run(host='0.0.0.0', port=81)
