from application import app, db
from flask import redirect, render_template, request, url_for
from application.pokemons.models import pokemon
from application.pokemons.forms import PokemonForm
from flask_login import current_user
from application.auth.models import User
from application.pokedatas.models import pokedata
from flask_login import login_required

@app.route("/pokemons", methods=["GET"])
@login_required
def pokemons_index():
    return render_template("pokemons/list.html", pokemons = User.find_pokemons_for_user(current_user.id))

@app.route("/pokemons/new/")
@login_required
def pokemons_form():
    return render_template("pokemons/new.html", form = PokemonForm())
  
@app.route("/pokemons/<pokemon_id>/", methods=["POST"])
def pokemons_set_powerupped(pokemon_id):

    t = pokemon.query.get(pokemon_id)
    t.powerupped = True
    db.session().commit()
  
    return redirect(url_for("pokemons_index"))

@app.route("/pokemons/", methods=["POST"])
def pokemons_create():
    form = PokemonForm(request.form)
    
    if not form.validate():
        return render_template("pokemons/new.html", form = form)

    t = pokemon(form.name.data)
    t.powerupped = form.powerupped.data
    t.cp = form.cp.data
    t.hp = form.hp.data
    t.dust = form.dust.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("pokemons_index"))

@app.route("/pokemons/<pokemon_id>/", methods=["GET"])
@login_required
def pokemons_pokemon(pokemon_id):
    return render_template("pokemons/pokemon.html", pokemon = pokemon.query.get(pokemon_id), form= PokemonForm(), current_user=current_user)

@app.route("/pokemons/<pokemon_id>/edit/", methods=["POST"])
def pokemons_edit(pokemon_id):
    form = PokemonForm(request.form)

    if not form.validate():
        return render_template("pokemons/pokemon.html", form = form)

    t = pokemon.query.get(pokemon_id)
    t.name = form.name.data
    t.powerupped = form.powerupped.data
    t.cp = form.cp.data
    t.hp = form.hp.data
    t.dust = form.dust.data

    db.session().commit()
  
    return render_template("pokemons/pokemon.html", pokemon = pokemon.query.get(pokemon_id), form= PokemonForm())

@app.route("/pokemons/<pokemon_id>/delete/", methods=["POST"])
def pokemons_delete(pokemon_id):
    db.session.delete(pokemon.query.get(pokemon_id))
    db.session().commit()
    return redirect(url_for("pokemons_index"))