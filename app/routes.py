from app import app
from flask import render_template

@app.route("/accueil")
def accueil():
    return render_template('accueil.html')