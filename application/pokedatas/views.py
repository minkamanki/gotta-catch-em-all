from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.pokedatas.models import pokedata, Type
from application.pokedatas.forms import NewPokemonForm, NewTypeForm, AddTypeToPokemonForm
from flask_login import current_user


@app.route("/pokedatas/new/")
@login_required(role="ADMIN")
def pokedata_form():
    return render_template("pokedatas/new.html", form=NewPokemonForm())


@app.route("/pokedatas/new", methods=["POST"])
@login_required(role="ADMIN")
def pokedata_add():
    form = NewPokemonForm(request.form)

    if not form.validate():
        return render_template("pokedatas/new.html", form=form)

    t = pokedata(form.name.data)
    t.number = form.number.data
    t.info = form.info.data

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("pokedata_form"))


@app.route("/pokedatas/newtype/")
@login_required(role="ADMIN")
def pokedata_typeform():
    form = NewTypeForm()
    return render_template("pokedatas/newType.html", form=form)


@app.route("/pokedatas/newtype", methods=["POST"])
@login_required(role="ADMIN")
def pokedata_addType():
    form = NewTypeForm(request.form)

    if not form.validate():
        return render_template("pokedatas/newType.html", form=form)

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
    form = AddTypeToPokemonForm()
    form.type_id.choices = [(a.id, a.name) for a in Type.query.order_by('name')]
    form.pokedata_id.choices = [(g.id, g.name) for g in pokedata.query.order_by('name')]
    
    return render_template("pokedatas/addTypeToPokemon.html", form = form)

@app.route("/pokedatas/pokemontype", methods=["POST"])
@login_required(role="ADMIN")
def pokedata_addPokemonType():
    form = AddTypeToPokemonForm(request.form)
    form.type_id.choices = [(a.id, a.name) for a in Type.query.order_by('name')]
    form.pokedata_id.choices = [(g.id, g.name) for g in pokedata.query.order_by('name')]
    
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
    return render_template("pokedatas/pokemon.html", pokemon = pokedata.query.get(pokedata_id), bestpokemons = pokedata.find_pokemons_best_for_species(pokedata_id))

@app.route("/types", methods=["GET"])
def pokedata_list_types():
    return render_template("pokedatas/listTypes.html", types = Type.query.all())

@app.route("/types/<type_id>/", methods=["GET"])
def pokedata_type(type_id):
    if current_user.id:
        return render_template("pokedatas/type.html", type = Type.query.get(type_id), pokemons = Type.find_users_pokemons_for_type(type_id, current_user.id))
    
    return render_template("pokedatas/type.html", type = Type.query.get(type_id))