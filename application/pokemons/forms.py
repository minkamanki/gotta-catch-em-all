from flask_wtf import FlaskForm
from wtforms import BooleanField, SelectField, StringField, IntegerField, validators

class PokemonForm(FlaskForm):
    name = StringField("Pokemons name", [validators.Length(min=3)])
    powerupped = BooleanField("Powerupped")
    cp = IntegerField("CP", [validators.NumberRange(min=10, max=5000, message="Invalid cp!")])
    hp = IntegerField("HP", [validators.NumberRange(min=1, message="Invalid hp!")])
    dust = IntegerField("Stardust", [validators.NumberRange(min=200, max=10000, message="Invalid stardust!")])
    #pokedata = SelectField('Choose pokemon', choices = [(1, 'Bulbasaur'), (2, 'Ivysaur')])

    class Meta:
        csrf = False

