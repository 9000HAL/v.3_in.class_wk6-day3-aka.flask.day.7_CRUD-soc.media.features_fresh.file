from flask import request, render_template, redirect, url_for, flash
from flask_login import current_user
from . import posts
from app.blueprints.posts.forms import PostForm
#from form import PostForm
from app.models import Post
from app import db

@posts.route('/create_post', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if request.method == 'POST' and form.validate_on_submit():
        #data from signup form
        post_data = {
            'img_url': form.img_url.data,
            'title': form.title.data,
            'caption': form.caption.data,
            'user_id': current_user.id
        }

        #create POST instance
        new_post = Post()

        #set post_data to our post attributes
        new_post.from_dict(post_data)

        #save to db
        db.session.add(new_post)
        db.session.commit()


        flash('Successfully created post!', 'success')
        return redirect(url_for('main.home'))
    else:
        return render_template('create_post.html', form=form)