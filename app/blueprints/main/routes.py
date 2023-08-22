from flask import request, render_template, redirect, url_for
from flask_login import current_user, login_required
from . import main
from app import db
from app.models import User, Pokemon
import requests
from app.models import Post #per documentation c4------


# Assuming you're using blueprints, use @main.route for your routes
@main.route('/catch', methods=['POST'])
@login_required  # Ensure only logged-in users can catch a Pokémon
def catch_pokemon():
    user = current_user
    
    pokemon_name = request.form.get('pokemon_name')
    image_url = request.form.get('image_url')
    
    pokemon = Pokemon.query.filter_by(name=pokemon_name).first()
    
    if not pokemon:
        pokemon = Pokemon(name=pokemon_name, image_url=image_url)
        db.session.add(pokemon)

    user.pokemons.append(pokemon)
    db.session.commit()

    return redirect(url_for('main.home'))




@main.route('/')
@main.route('/home')
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts[::-1])


@main.route('/pokemon', methods=['GET', 'POST'])
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
































































































#v.1 pre documentation here below
"""

from flask import request, render_template
import requests
#from app.blueprints.main import app  #GHCP -----check DK version????
from . import main
#from flask import Blueprint      #---- GHCP commented out????use???
from flask_login import login_required
#from app.models import Posts #error causing ca ver.
from app.models import Post #no error-------
#from app.models import posts #error
#from app.models import post #error

#documentation 2.1 #######################VVVVVVVVVVVVVVVVVVVVV
from app import db
from app.models import User, Pokemon





@app.route('/catch', methods=['POST'])
def catch_pokemon():
    # Assuming user is logged in and you're using Flask-Login to get current_user
    user = current_user  # you might need to import current_user
    
    # Get Pokemon data from form (make sure you send these data from your frontend)
    pokemon_name = request.form.get('pokemon_name')
    image_url = request.form.get('image_url')
    
    # Check if Pokemon already exists in our DB
    pokemon = Pokemon.query.filter_by(name=pokemon_name).first()
    
    # If not, create new Pokemon entry
    if not pokemon:
        pokemon = Pokemon(name=pokemon_name, image_url=image_url)
        db.session.add(pokemon)
        db.session.commit()
    
    # Link the caught Pokemon to the user
    user.pokemons.append(pokemon)
    db.session.commit()

    # Redirect back to the page or wherever you want
    return redirect(url_for('main.home'))  # replace 'main.home' with wherever you want to redirect


#documentation 2.1 #######################^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




@main.route('/')
@main.route('/home') ###########gabe fix???
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts[::-1])



#############################################pokemon_name#############################################
@main.route('/pokemon', methods=['GET', 'POST'])
#@login_required           #------dk version
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



"""