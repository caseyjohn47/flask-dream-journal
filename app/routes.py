from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from app.models import User
from app import db
from app.models import User, Post
from app.forms import RegistrationForm, EditProfileForm, NewEntryForm, EditEntryForm

# Home page
@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = current_user.posts.all()
    return render_template("index.html", title='Home Page', posts=posts)

# New entry in dream journal
@app.route('/new_entry', methods=['GET', 'POST'])
@login_required
def new_entry():
    form = NewEntryForm()
    if form.validate_on_submit():
        p = Post(body=form.entry.data, author=current_user)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('login'))
    elif request.method == 'GET':
        form.entry.data = ""
    return render_template('new.html', form=form)

# Delete entry in dream journal
@app.route('/delete/<int:id>')
@login_required
def delete_entry(id):
    post_to_delete = Post.query.get_or_404(id)
    try:
        db.session.delete(post_to_delete)
        db.session.commit()
        flash("Post deleted successfully.")
        return redirect(url_for('index'))
    except:
        flash("There was a problem! Please try again.")
        return redirect(url_for('index'))

# Edit entry in dream journal
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_entry(id):
    post_to_edit = Post.query.get_or_404(id)
    form = EditEntryForm()
    if form.validate_on_submit():
        post_to_edit.body = form.entry.data
        db.session.commit()
        return redirect(url_for('login'))
    elif request.method == 'GET':
        form.entry.data = post_to_edit.body
    return render_template('edit.html', form=form)

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

# Logout user
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Register user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

# Profile page
@app.route('/profile/<int:id>')
@login_required
def profile_page(id):
    this_user = User.query.get_or_404(id)
    posts = this_user.posts.all()
    return render_template("profile.html", title='Profile Page', usr=this_user, posts=posts)

# Community page
@app.route('/community')
@login_required
def community_page():
    users = User.query.all()
    posts = Post.query.all()
    return render_template("community.html", title='Community', users=users, posts=posts)

# Edit About Me section
@app.route('/edit/profile/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_profile(id):
    this_user = User.query.get_or_404(id)
    form = EditProfileForm()
    if form.validate_on_submit():
        this_user.about_me = form.about_me.data
        db.session.commit()
        return redirect(url_for('profile_page', id=id))
    elif request.method == 'GET':
        form.about_me.data = this_user.about_me
    return render_template('edit_profile.html', form=form)