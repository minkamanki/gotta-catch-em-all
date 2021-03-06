from application import app, login_manager, db
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
    form = PokemonForm()
    form.pokedata_id.choices = [(g.id, g.name) for g in pokedata.query.order_by('name')]
    return render_template("pokemons/new.html", form = form)

@app.route("/pokemons/<pokemon_id>/", methods=["POST"])
def pokemons_set_powerupped(pokemon_id):

    t = pokemon.query.get(pokemon_id)
    t.powerupped = True
    db.session().commit()
  
    return redirect(url_for("pokemons_index"))

@app.route("/pokemons/", methods=["POST"])
def pokemons_create():
    form = PokemonForm(request.form)
    form.pokedata_id.choices = [(g.id, g.name) for g in pokedata.query.order_by('name')]    
    if not form.validate():
        return render_template("pokemons/new.html", form = form)

    t = pokemon(form.name.data)
    t.powerupped = form.powerupped.data
    t.cp = form.cp.data
    t.hp = form.hp.data
    t.dust = form.dust.data
    t.account_id = current_user.id    
    t.pokedata_id = form.pokedata_id.data

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("pokemons_index"))

@app.route("/pokemons/<pokemon_id>/", methods=["GET"])
@login_required
def pokemons_pokemon(pokemon_id):
    p = pokemon.query.get(pokemon_id)
    form= PokemonForm()
    form.pokedata_id.default = p.pokedata_id
    form.process()
    
    return render_template("pokemons/pokemon.html", pokemon = p, form= form, current_user=current_user, pokemondata = pokedata.query.get(p.pokedata_id))

@app.route("/pokemons/<pokemon_id>/edit/", methods=["POST"])
@login_required
def pokemons_edit(pokemon_id):
    form = PokemonForm(request.form)
    p = pokemon.query.get(pokemon_id)
    
    if not form.validate():
        return render_template("pokemons/pokemon.html", pokemon = p, form = form, pokemondata = pokedata.query.get(p.pokedata_id))

    t = pokemon.query.get(pokemon_id)
    if t.account_id != current_user.id:
        # tee jotain, esim. 
        return login_manager.unauthorized()

    t.name = form.name.data
    t.powerupped = form.powerupped.data
    t.cp = form.cp.data
    t.hp = form.hp.data
    t.dust = form.dust.data

    db.session().commit()
  
    return render_template("pokemons/pokemon.html", pokemon = pokemon.query.get(pokemon_id), form= PokemonForm(), pokemondata = pokedata.query.get(pokemon.query.get(pokemon_id).pokedata_id))

@app.route("/pokemons/<pokemon_id>/delete/", methods=["POST"])
def pokemons_delete(pokemon_id):
    t = pokemon.query.get(pokemon_id)
    db.session().delete(t)
    db.session().commit()
    return redirect(url_for("pokemons_index"))