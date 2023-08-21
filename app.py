from app import create_app

app = create_app()
































































































#v.1 for learning/testing

"""

from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('base.html', title='Home')

@app.route('/pokemon_name', methods=['GET', 'POST'])
def pokemon_name():
    pokemon_data = None
    if request.method == 'POST':
        pokemon_name = request.form.get('pokemon_name')
        pokemon_data = get_pokemon_data(pokemon_name)
    return render_template('pokemon_name.html', title='Pokemon Page', pokemon_data=pokemon_data)


# Function to retrieve Pokémon data
def get_pokemon_data(pokemon_name):
    base_url = "https://pokeapi.co/api/v2/"
    url = base_url + f"pokemon/{pokemon_name}/"
    response = requests.get(url)
    data = response.json()

    name = data['name']
    ability = data['abilities'][0]['ability']['name']
    base_experience = data['base_experience']
    
    return {'name': name, 'ability': ability, 'base_experience': base_experience}

if __name__ == "__main__":
    app.run(debug=True)








pokemon_name.html v.1 :

{% extends 'base.html' %}

{% block title %}
    {{ title }}
{% endblock %}

{% block content %}
<form method="POST" class="px-3">
    <div class="mb-3">
      <label for="pokemon_name" class="form-label"><br><b>WELCOME TO THE POKEMON SINGLE PAGE APP!</b><br><br><br>Enter Pokemon Name In All "lower case": </label>
      <input type="text" class="form-control" id="pokemon_name" name="pokemon_name">
    </div>
    <button type="submit" class="btn btn-primary">Get Results!</button>
  </form>
  {% if pokemon_data %}
  <table class="table">
    <thead>
      <tr>
        <th scope="col">Pokemon Name</th>
        <th scope="col">Ability</th>
        <th scope="col">Base Experience</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>{{ pokemon_data.name }}</td>
        <td>{{ pokemon_data.ability }}</td>
        <td>{{ pokemon_data.base_experience }}</td>
      </tr>
    </tbody>
  </table>
{% endif %}
{% endblock %}










base.html v.1 :

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block content %}
    {% endblock %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
</body>
</html>


"""



























"""  

from flask import Flask, request, render_template
import requests



app = Flask(__name__)




#--------ROUTES---------------------

@app.route("/")
def hello_world():
    return "<p>Hello, THIEVES-2023!</p>"



@app.route('/home')
def home():
    return '<h1>This is the home page</h1>'



@app.route('/user/<username>')
def username(username):
    # show the user profile for that user
    return f'Hello {username}!'



@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'




#HTTP methods:

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return '<h1>Logged In</h1>'
    else:
        return render_template('forms.html')




#########STUDENTS EXAMPLE

@app.route('/students')
def students():
    students_lst = ['Gabe', 'Will', 'Sean', 'Peace']
    return render_template('students.html', students_lst=students_lst)









########################### ERGAST EXAMPLE

@app.route('/ergast', methods=['GET', 'POST'])
def ergast():
    if request.method == 'POST':
        year = request.form.get('year')
        rnd = request.form.get('rnd')
        
        url = f'http://ergast.com/api/f1/{year}/{rnd}/driverStandings.json'
        response = requests.get(url)
        if response.ok:
            try:
                standings_data = response.json()['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
                driver_data = get_driver_info(standings_data)
                return render_template('ergast.html', driver_data=driver_data)
            except IndexError:
                return 'That year or round does not exist!'
    return render_template('ergast.html')

#   REMOVED:                  return get_driver_info(standings_data)



# HELPER FUNCTION FORM DAY 4 WEEK 4 CLASS LECTURE BELOW:

def get_driver_info(data):
    new_driver_data = []
    for driver in data:
        driver_dict = {
            'full_name': f"{driver['Driver']['givenName']} {driver['Driver']['familyName']}",
            'DOB': driver['Driver']['dateOfBirth'],
            'wins': driver['wins'],
            'team': driver['Constructors'][0]['name']
        }
        if len(new_driver_data) <=5:
            new_driver_data.append(driver_dict)
    return new_driver_data






########################### ERGAST EXAMPLE page renders no error but


@app.route('/ergast', methods=['GET', 'POST'])
def ergast():
    if request.method == 'POST':
        year = request.form.get('year')
        rnd = request.form.get('rnd')
        
        url = f'http://ergast.com/api/f1/{year}/{rnd}/driverStandings.json'
        response = requests.get(url)
        if response.ok:
            try:
                standings_data = response.json()['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
                return get_driver_info(standings_data)
            except IndexError:
                return 'That year or round does not exist!'
    return render_template('ergast.html')

"""  
    
