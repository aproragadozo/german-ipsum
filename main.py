from flask import Flask, render_template, request, url_for, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        variable_start_string='%%',  # Default is '{{', I'm changing this because Vue.js uses '{{' / '}}'
        variable_end_string='%%',
    ))

app = CustomFlask(__name__)  # This replaces your existing "app = Flask(__name__)"

cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config.from_pyfile('db.cfg')

db = SQLAlchemy(app)

class Sentence(db.Model):

    __tablename__ = "sentences"

    id = db.Column('id', db.Integer, primary_key=True)
    content = db.Column('content', db.Unicode)

    def __init__(self, content):
        self.content = content

mondatok = []

@app.route("/")
def hello_world():
    mondat = Sentence.query.get(random.randint(0, Sentence.query.count()))
    mondatok.append(mondat)
    return jsonify({"mondatok": [mondat for mondat in mondatok]})
    # return render_template("index.html", mondat = mondatok[0])

# accept cors headers
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

# run Flask app
if __name__ == "__main__":
    app.run(port=5000)