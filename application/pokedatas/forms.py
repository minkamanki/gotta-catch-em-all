from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class PokemonForm(FlaskForm):
    name = StringField("Pokemons name", [validators.Length(min=3)])
    types = StringField("Types", [validators.Length(min=3)])
    number = IntegerField("Number", [validators.NumberRange(min=1, max=850, message="Invalid pokemon number!")])
    info = StringField("Information", [validators.Length(min=5)])

    class Meta:
        csrf = False
