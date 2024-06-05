from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 3 characters.', category='error')
        else:
            flash('Account created!', category='success')
        


    
        
    return render_template("Sign_in.html, boolean = True")

@auth.route('/sign-out')
def sign_out():
    return "<p>Sign out</p>"