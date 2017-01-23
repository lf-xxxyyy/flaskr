import os
import mysql.connector
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)


app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))


def connect_db() :
	conn = mysql.connector.connect(user='root', password='123', database='test')
	return conn


def get_db():
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
		print ('connect db...')
	return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.cursor().close_db()


def init_db():
	conn = mysql.connector.connect(user='root', password='123', database='test')
	cursor = conn.cursor()
	cursor.execute('create table userx (id varchar(20) primary key, name varchar(20))')
	conn.commit()
	cursor.close()


@app.route('/')
def show_entries():
	db = get_db()
	cur = db.execute('select title, text from entries order by id desc')
	entries = cur.fetchall()
	return render_template('show_entries.html', entries=entries)


@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME']:
			error = 'invalid username'
		elif request.form['password'] != app.config['PASSWORD']:
			error = 'invalid password'
		else:
			session['logged_in'] = True
			flash('you were logged in')
			return redirect(url_for('show_entries'))
	return render_template('login.html', error=error)




if __name__ == '__main__' :
	app.run()