from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, validators
from wtforms.widgets import TextArea
from application.pokedatas.models import pokedata, Type


class NewPokemonForm(FlaskForm):
    name = StringField("Pokemons name", [validators.Length(min=3)])
    number = IntegerField("Number", [validators.NumberRange(min=1, max=850, message="Invalid pokemon number!")])
    info = StringField(u'Information', widget=TextArea())

    class Meta:
        csrf = False

class NewTypeForm(FlaskForm):
    name = StringField("Type's name", [validators.Length(min=3)])    
    strongAgainst = StringField("Strong Against", [validators.Length(min=3, message="If doesn't have any put '---'!")])  
    weakAgainst = StringField("Weak Against", [validators.Length(min=3, message="If doesn't have any put '---'!")])  
    other = StringField(u'Other', widget=TextArea())

    class Meta:
        csrf = False

class AddTypeToPokemonForm(FlaskForm):    
    #pokedata_id = SelectField(u'pokedata', choices=[(g.id, g.name) for g in pokedata.query.order_by('name')], coerce=int)
    #type_id = SelectField(u'type', choices=[(g.id, g.name) for g in Type.query.order_by('name')], coerce=int)

    class Meta:
        csrf = False
