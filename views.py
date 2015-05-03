from app import app, db
from flask import render_template, request, url_for, redirect
from forms import CreateForm
from models import Post


@app.route('/')
def homepage():
    return render_template('base.html')


@app.route('/create', methods=['GET', 'POST'])
def create():
    my_form = CreateForm(csrf_enabled=False)
    if request.method == 'GET':
        return render_template('create.html', form=my_form)
    if request.method == 'POST':
        if my_form.validate_on_submit():
            create_post = Post(my_form.title.data, my_form.text.data)
            db.session.add(create_post)
            db.session.commit()
    return redirect(url_for('homepage'))
