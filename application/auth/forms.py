from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class NewUserForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3)])
    username = StringField("Username", [validators.Length(min=3)])
    password = PasswordField("Password", [validators.Length(min=3)])
    lvl = IntegerField("Player level", [validators.NumberRange(min=1, max=40, message="Invalid level!")])

    class Meta:
        csrf = False        