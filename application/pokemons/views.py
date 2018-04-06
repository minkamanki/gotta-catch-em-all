from application import app, db
from flask import redirect, render_template, request, url_for
from application.pokemons.models import pokemon
from application.pokemons.forms import PokemonForm
from flask_login import login_required, current_user

@app.route("/pokemons", methods=["GET"])
def pokemons_index():
    return render_template("pokemons/list.html", pokemons = pokemon.query.all())

@app.route("/pokemons/new/")
@login_required
def pokemons_form():
    return render_template("pokemons/new.html", form = PokemonForm())
  
@app.route("/pokemons/<pokemon_id>/", methods=["POST"])
@login_required
def pokemons_set_powerupped(pokemon_id):

    t = pokemon.query.get(pokemon_id)
    t.powerupped = True
    db.session().commit()
  
    return redirect(url_for("pokemons_index"))

@app.route("/pokemons/", methods=["POST"])
@login_required
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
def pokemons_pokemon(pokemon_id):
    return render_template("pokemons/pokemon.html", pokemon = pokemon.query.get(pokemon_id), form= PokemonForm())

@app.route("/pokemons/<pokemon_id>/edit/", methods=["POST"])
@login_required
def pokemons_edit(pokemon_id):
    form = PokemonForm(request.form)
    print(request.form)
    print('hi')
    print('hi')
    print('hi')
    print('hi')

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