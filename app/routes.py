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
from app.forms import RegistrationForm
from app.forms import EditEntryForm


@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = current_user.posts.all()
    return render_template("index.html", title='Home Page', posts=posts)


@app.route('/entry', methods=['GET', 'POST'])
@login_required
def edit_entry():
    form = EditEntryForm()
    if form.validate_on_submit():
        p = Post(body=form.entry.data, author=current_user)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('login'))
    elif request.method == 'GET':
        form.entry.data = ""
    return render_template('edit.html', form=form)


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


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


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
