from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, StringField, IntegerField, validators
from application.pokedatas.models import pokedata

class PokemonForm(FlaskForm):
    name = StringField("Pokemons name", [validators.Length(min=3)])
    powerupped = BooleanField("Powerupped")
    cp = IntegerField("CP", [validators.NumberRange(min=10, max=5000, message="Invalid cp!")])
    hp = IntegerField("HP", [validators.NumberRange(min=1, message="Invalid hp!")])
    dust = IntegerField("Stardust", [validators.NumberRange(min=200, max=10000, message="Invalid stardust!")])
    pokedata_id = SelectField(u'pokedata', choices=[(g.id, g.name) for g in pokedata.query.order_by('name')], coerce=int)

    class Meta:
        csrf = False

