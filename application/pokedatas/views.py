from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.pokedatas.models import pokedata, Type
from application.pokedatas.forms import NewPokemonForm, NewTypeForm, AddTypeToPokemonForm

@app.route("/pokedatas/new/")
@login_required(role="ADMIN")
def pokedata_form():
    return render_template("pokedatas/new.html", form = NewPokemonForm())

@app.route("/pokedatas/new", methods=["POST"])
@login_required(role="ADMIN")
def pokedata_add():
    form = NewPokemonForm(request.form)

    if not form.validate():
        return render_template("pokedatas/new.html", form = form)

    t = pokedata(form.name.data)
    t.number = form.number.data
    t.info = form.info.data
    
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("pokedata_form"))

@app.route("/pokedatas/newtype/")
@login_required(role="ADMIN")
def pokedata_typeform():
    return render_template("pokedatas/newType.html", form = NewTypeForm())

@app.route("/pokedatas/newtype", methods=["POST"])
@login_required(role="ADMIN")
def pokedata_addType():
    form = NewTypeForm(request.form)

    if not form.validate():
        return render_template("pokedatas/newType.html", form = form)

    t = Type(form.name.data) 
    t.strongAgainst = form.strongAgainst.data
    t.weakAgainst = form.weakAgainst.data
    t.other = form.other.data

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("pokedata_typeform"))

@app.route("/pokedatas/pokemontype/", methods=["GET"])
@login_required(role="ADMIN")
def pokedata_pokemontypeform():
    return render_template("pokedatas/addTypeToPokemon.html", form = AddTypeToPokemonForm())

@app.route("/pokedatas/pokemontype", methods=["POST"])
@login_required(role="ADMIN")
def pokedata_addPokemonType():
    form = AddTypeToPokemonForm(request.form)

    if not form.validate():
        return render_template("pokedatas/addTypeToPokemon.html", form = form)

    t = Type.query.get(form.type_id.data)
    p = pokedata.query.get(form.pokedata_id.data)
    p.types.append(t)
    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("pokedata_pokemontypeform"))

@app.route("/pokedatas", methods=["GET"])
def pokedata_list():
    return render_template("pokedatas/list.html", pokedatas = pokedata.query.all())

@app.route("/pokedatas/<pokedata_id>/", methods=["GET"])
def pokedata_pokemon(pokedata_id):
    return render_template("pokedatas/pokemon.html", pokemon = pokedata.query.get(pokedata_id))

