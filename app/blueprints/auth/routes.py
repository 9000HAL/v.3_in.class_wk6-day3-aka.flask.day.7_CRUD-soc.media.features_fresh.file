from flask import request, render_template, redirect, url_for, flash
import requests
from app.blueprints.auth.forms import LoginForm, SignUpForm
from app import db
from . import auth
from app.models import User
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required




#Authentication routes
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data
        queried_user = User.query.filter(User.email == email).first()
        #if queried_user and queried_user.check_password(password):
        #if queried_user and check_password_hash(queried_user.password_hash, password):     #-----DK version------
        if queried_user and queried_user.password_hash and check_password_hash(queried_user.password_hash, password):   #c4---------
            login_user(queried_user)
            flash(f'Welcome back {queried_user.first_name}!', 'success')
            return redirect(url_for('main.home'))
        else:
            error = 'INVALID EMAIL OR PASSWORD'
            return render_template('login.html', form=form, error=error)
    else:
        print('not validated')
        return render_template('login.html', form=form) 



######################################################

##########DK signup version##########

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():

        #data from signup form
        user_data = {
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'email': form.email.data.lower(),
            'password': form.password.data
        
        }

        #create new user instance
        new_user = User()

        #set user_data to our user attributes
        new_user.from_dict(user_data)

        #save to db
        db.session.add(new_user)
        db.session.commit()


        flash(f'Thank you for signing up {user_data["first_name"]}!', 'success')
        #return redirect(url_for('main.home'))
        return redirect(url_for('auth.login'))
    else:
        return render_template('signup.html', form=form)


######################################################





###################LOGOUT

@auth.route('/logout')
@login_required       #----dk version?????
def logout():
        logout_user()
        flash('Successfully logged out', 'warning')
        return redirect(url_for('main.home'))













