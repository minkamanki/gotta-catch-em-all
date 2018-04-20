from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.pokedatas.models import pokedata
from application.pokedatas.forms import PokemonForm

@app.route("/pokedatas/new/")
def pokedata_form():
    return render_template("pokedatas/new.html", form = PokemonForm())

@app.route("/pokedatas/", methods=["POST"])
@login_required(role="ADMIN")
def pokedata_add():
    form = PokemonForm(request.form)

    if not form.validate():
        return render_template("pokedatas/new.html", form = form)

    t = pokedata(form.name.data)
    t.types = form.types.data
    t.number = form.number.data
    t.info = form.info.data

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("pokedata_form"))