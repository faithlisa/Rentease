from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)


@auth.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    data = request.form
    return render_template("Sign in, boolean = True")

@auth.route('/sign-out')
def sign_out():
    return "<p>Sign out</p>"