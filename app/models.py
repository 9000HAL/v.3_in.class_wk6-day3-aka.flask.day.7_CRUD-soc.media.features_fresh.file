from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash

# Association table between User and Pokemon
user_pokemon = db.Table('user_pokemon',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), primary_key=True)
)

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False) 
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
    # Relation to Pokemon model
    pokemons = db.relationship('Pokemon', secondary=user_pokemon, back_populates='users')
    
    def hash_password(self, signup_password):
        return generate_password_hash(signup_password)
    
    def from_dict(self, user_data):
        self.first_name = user_data['first_name']
        self.last_name = user_data['last_name']
        self.email = user_data['email']
        self.password_hash = self.hash_password(user_data['password'])

# Pokemon model
class Pokemon(db.Model):
    __tablename__ = 'pokemon'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(500))

    # User relation through association table
    users = db.relationship('User', secondary=user_pokemon, back_populates='pokemons')

# Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String)
    title = db.Column(db.String(30))
    caption = db.Column(db.String(30))
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def from_dict(self, post_data):
        self.img_url = post_data['img_url']
        self.title = post_data['title']
        self.caption = post_data['caption']
        self.user_id = post_data['user_id']


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



































































































#v.1 pre documentation here below
"""
from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash #check_password_hash




# from documentation 1.1 ###########################################################VVVVVVVVVV


# New Pokémon model
class Pokemon(db.Model):
    __tablename__ = 'pokemon'
    
    id = db.Column(db.Integer, primary_key=True)  # Primary key for the Pokemon
    name = db.Column(db.String(100), nullable=False)  # Pokemon name
    image_url = db.Column(db.String(500))  # URL of Pokemon image

    # User relation through association table
    users = db.relationship('User', secondary='user_pokemon', back_populates='pokemons')

    # from documentation 1.1 ###########################################################^^^^^^^^^^^^^



#from documentation 1.2 ###########################################################VVVVVVVVVV

# Association table between User and Pokemon
user_pokemon = db.Table('user_pokemon',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), primary_key=True)
)

# Assuming your User model looks something like this:
class User(db.Model):
    # ...[your existing user fields here]...
    
    # Add relation to Pokemon model
    pokemons = db.relationship('Pokemon', secondary=user_pokemon, back_populates='users')


#from documentation 1.2 ###########################################################^^^^^^^^^^^^







class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    #password_hash = db.Column(db.String) 
    password_hash = db.Column(db.String, nullable=False) # Save hashed password.
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    

    #this section from template below
    # hashes our password when user signs up
    def hash_password(self, signup_password):
        return generate_password_hash(signup_password)
    
    # This method will assign our columns with their respective values

    def from_dict(self, user_data):
        self.first_name = user_data['first_name']
        self.last_name = user_data['last_name']
        self.email = user_data['email']
        self.password_hash = self.hash_password(user_data['password'])    #c4 suggested this change



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String)
    title = db.Column(db.String(30))
    caption = db.Column(db.String(30))
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    #foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

      # This method will assign our columns with their respective values
    def from_dict(self, post_data):
        self.img_url = post_data['img_url']
        self.title = post_data['title']
        self.caption = post_data['caption']
        self.user_id = post_data['user_id']

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)













#<!--removed my v.1 set up here commented out below-->
def set_password(self, password):
    self.password_hash = generate_password_hash(password)

def check_password(self, password):
    return check_password_hash(self.password_hash, password)





"""












































############lecture version below#######################

"""   
from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String)  
    created_on = db.Column(db.DateTime, default=datetime.utcnow())


    # hashes our password when a user signs up
    def hash_password(new_user, signup_password):        
        return generate_password_hash(signup_password)





##############
    # this method will assign our columns with their respective values ---- WORK ??? --NO DO NOT USE SELF
def from_dict(self, user_data): 
    self.first_name = user_data['first_name']
    self.last_name = user_data['last_name']
    self.email = user_data['email']
    self.password = self.hash_password(user_data['password'])
    --- WORK ??? --NO DO NOT USE SELF
##############

# DUPLICATE MODEL TO FIX ERROR ------WORK ?????????? ---YES!!!!!!
def from_dict(new_user, user_data): 
    new_user.first_name = user_data['first_name']
    new_user.last_name = user_data['last_name']
    new_user.email = user_data['email']
    new_user.password = new_user.hash_password(user_data['password'])


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



    """