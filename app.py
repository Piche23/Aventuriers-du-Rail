import flask
from flask import Flask, redirect
from database.database import db, init_database
from database.models import *
from flask import url_for
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)
url_Hugo = "sqlite:///C:\\Users\\hugop\\OneDrive\\Documents\\Hugo\\Aventuriers du rail\\database\\database.db"
app.config["SQLALCHEMY_DATABASE_URI"] = url_Hugo
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)  # (1) flask prend en compte la base de donnee
with app.test_request_context():  # (2) bloc exécuté à l'initialisation de Flask
    init_database()


# Joueurs
@app.route('/')
@app.route('/view/joueurs')
def view_joueurs():
    joueurs = Joueur.get_all_joueur()
    return flask.render_template("template_joueurs.html.jinja2", joueurs=joueurs)



if __name__ == '__main__':
    app.run()
