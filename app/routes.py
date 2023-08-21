"""Routes for core Flask app.


from flask import request, render_template, redirect, url_for, flash
import requests
#from app.forms import LoginForm, SignUpForm ###### commented out match DK version
from app.blueprints.auth.forms import LoginForm, SignUpForm
from app import app, db
from app.models import User
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, current_user, login_required



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')





#############################################pokemon_name#############################################
@app.route('/pokemon_name', methods=['GET', 'POST'])
def pokemon_name():
    pokemon_data = None
    if request.method == 'POST':
        pokemon_name = request.form.get('pokemon_name').lower() 
        pokemon_data = get_pokemon_data(pokemon_name)
    return render_template('pokemon.html', title='Pokemon Page', pokemon_data=pokemon_data)

def get_pokemon_data(pokemon_name):
    base_url = "https://pokeapi.co/api/v2/"
    url = base_url + f"pokemon/{pokemon_name}/"
    response = requests.get(url)
    data = response.json()

    name = data['name']
    stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
    front_shiny_sprite = data['sprites']['front_shiny']
    ability = data['abilities'][0]['ability']['name']
    
    return {'name': name, 'hp': stats['hp'], 'defense': stats['defense'], 'attack': stats['attack'], 'front_shiny_sprite': front_shiny_sprite, 'ability': ability}




###################################



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data
        queried_user = User.query.filter(User.email == email).first()
        if queried_user and queried_user.check_password(password):
        #if queried_user and check_password_hash(queried_user.password_hash, password):           #-----DK version------
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

app.route('/signup', methods=['GET', 'POST'])
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
        return redirect(url_for('auth.login'))
    else:
        return render_template('signup.html', form=form)


######################################################





###################LOGOUT

@app.route('/logout')
#@login_required
def logout():
        logout_user()
        flash('Successfully logged out', 'warning')
        return redirect(url_for('main.home'))









Routes for core Flask app."""












