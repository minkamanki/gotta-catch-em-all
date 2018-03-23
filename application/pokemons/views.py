from application import app, db
from flask import redirect, render_template, request, url_for
from application.pokemons.models import pokemon

@app.route("/pokemons", methods=["GET"])
def pokemons_index():
    return render_template("pokemons/list.html", pokemons = pokemon.query.all())

@app.route("/pokemons/new/")
def pokemons_form():
    return render_template("pokemons/new.html")
  
@app.route("/pokemons/<pokemon_id>/", methods=["POST"])
def pokemons_set_done(pokemon_id):

    t = pokemon.query.get(pokemon_id)
    t.done = True
    db.session().commit()
  
    return redirect(url_for("pokemons_index"))

@app.route("/pokemons/", methods=["POST"])
def pokemons_create():
    t = pokemon(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("pokemons_index"))