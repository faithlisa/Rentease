from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/sign')
def sign():
    return render_template("sign_in.html")

