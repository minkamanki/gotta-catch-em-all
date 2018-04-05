from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class PokemonForm(FlaskForm):
    name = StringField("Pokemons name", [validators.Length(min=3)])
    done = BooleanField("Caught")
 
    class Meta:
        csrf = False
