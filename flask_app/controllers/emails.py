from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.email import Email

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add/email", methods = ["POST"])
def create_email():
    data = {
        "email" : request.form["email"]
    }
    Email.save(data)
    if not Email.validate_email(data):
        return redirect ('/')
    return redirect("/success")

@app.route("/success")
def email_list():
    print(Email.getAll())
    return render_template("success.html", emails = Email.getAll())

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    Email.delete(data)
    return redirect('/success')
