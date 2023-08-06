from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from functools import cmp_to_key
from .models import User, Post, Current_Post, Article
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    post=Post.query.all()
    article=Article.query.all()
    return render_template('home.html', user=current_user,post=post,article=article)

@views.route('/my-blog', methods=['GET', 'POST'])
@login_required
def myBlog():
    posts = Post.query.filter_by(user_id=current_user.id)

    if request.method == 'POST':
        if request.form['btn'] == 'search':
            text = request.form.get('search-for')
            posts = Post.query.filter(Post.tags.contains(text))

    return render_template('my-blog.html', user=current_user, posts=posts)