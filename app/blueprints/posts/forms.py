from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

"""
class PostForm(FlaskForm):
    email = EmailField('Email: ', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_btn = SubmitField('Log In')

"""

class PostForm(FlaskForm):
    img_url = StringField('Image URL: ', validators=[DataRequired()])
    title = StringField('Title: ', validators=[DataRequired()])
    caption = StringField('Caption: ', validators=[DataRequired()])
    submit_btn = SubmitField('Create Post')
