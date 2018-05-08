from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
  
from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, NewUserForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))    

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))    

@app.route("/auth/newuser/")
def users_form():
    return render_template("auth/newuser.html", form = NewUserForm())

@app.route("/auth/", methods=["POST"])
def users_create():
    form = NewUserForm(request.form)
    query = User.query.filter(User.username==form.username.data)
    if query.first():
        return render_template("auth/newuser.html", form = form, message = "Username has already taken!")
    if not form.validate():
        return render_template("auth/newuser.html", form = form)

    t = User(form.name.data, form.username.data, form.password.data)
    t.lvl = form.lvl.data
  
    db.session().add(t)
    db.session().commit() 
  
    return redirect(url_for("auth_login"))
      