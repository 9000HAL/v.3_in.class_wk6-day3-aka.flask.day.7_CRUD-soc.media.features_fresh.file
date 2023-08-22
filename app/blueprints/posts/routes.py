from flask import request, render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from . import posts
from app.blueprints.posts.forms import PostForm #per c4 extra or leave alone uncommented out??????
from .forms import PostForm #############ca version was commented out ----error????????
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



#update post
@posts.route('/update/<int:post_id>', methods=['GET', 'POST']) #ca version
#@posts.route('/update_post/<int:post_id>', methods=['GET', 'POST']) #c4 version
@login_required
def update_post(post_id):
    form = PostForm() #c4 version     form = PostForm(obj=post)
    post = Post.query.get(post_id)
    if request.method == 'POST' and form.validate_on_submit():
        #data coming from the post form
        post_data = {
            'img_url': form.img_url.data,
            'title': form.title.data,
            'caption': form.caption.data,
            'user_id': current_user.id
        }

        #set post data to our post attributes
        post.from_dict(post_data)

        #save to db
        db.session.commit()

        flash(f'Successfully updated post {post.title}!', 'success')
        return redirect(url_for('main.home'))
    return render_template('update_post.html', form=form)


#delete post
@posts.route('/delete/<int:post_id>', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get(post_id)
    if current_user.id == post.user_id:
        db.session.delete(post)
        db.session.commit()
        flash(f'Successfully deleted post {post.title}!', 'success')
        return redirect(url_for('main.home'))
    else:
        flash("You cannot delete someone else's posts 🐍!", 'danger')
        return redirect(url_for('main.home'))



   
