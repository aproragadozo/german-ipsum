from flask import Flask, render_template, request, url_for, jsonify
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

app.config["DEBUG"] = True


#SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
#    username="aproragadozo",
#    password="P1roska?",
#    hostname="aproragadozo.mysql.pythonanywhere-services.com",
#    databasename="aproragadozo$sentences",
#)

SQLALCHEMY_DATABASE_URI = 'mysql://root:''@localhost/adat'
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
# app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Sentence(db.Model):

    __tablename__ = "sentences"

    id = db.Column('id', db.Integer, primary_key=True)
    content = db.Column('content', db.Unicode)

    def __init__(self, content):
        self.content = content

mondatok = [
    {
        'id': 1,
        'content': 'Was soll den diese Faselei, komm doch mal zum Sache!'
    }
]

@app.route("/")
def hello_world():
    mondat = Sentence.query.get(random.randint(0, Sentence.query.count()))
    # mondat = mondatok[0]
    # if the front-end is Vue, instead of rendering a template,
    # you'll need to return data here,
    # that the Vue app can query the "/" route for
    return render_template("index.html", mondat = mondat)

# run Flask app
if __name__ == "__main__":
    app.run(port=5000)