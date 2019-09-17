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
    return render_template("index.html", mondat = mondat)

    #turns out render_template is much better suited to what I'm trying to do
    #leaving the data-return option here for reference
    #row_as_dict = []
    #cell_as_dict = {
    #    'id': mondat.id,
    #    'content': mondat.content
    #}
    #row_as_dict.append(cell_as_dict)
    #return jsonify(cell_as_dict)

# run Flask app
if __name__ == "__main__":
    app.run(port=5000)