from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required


app = Flask(__name__)

app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		session['name'] = form.name.data
		return redirect(url_for('index'))
	return render_template('index.html', form=form, name = session.get('name'))

@app.route('/user/<name>/')
def user(name):
	return render_template('user.html', name=name)


@app.route('/testlist/')
def renderList():
	La = [1,2,3,4]
	return render_template('user.html', La=La)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

class NameForm(FlaskForm):
	name = StringField('what is your name?', validators=[Required()])
	submit = SubmitField('Submit')


if __name__ == '__main__':
	app.run()