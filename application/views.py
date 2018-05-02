from flask import render_template
from application import app
from application.pokemons.models import pokemon

@app.route("/")
def index():
    return render_template("index.html", bestpokemons = pokemon.find_pokemons_best())