import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)


app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db')
))


def connect_db() :
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv


def get_db():
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()


def init_db():
	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

@app.route('/add')
def add_entry():
	db = get_db()
	db.execute('insert into entries (title, text) values(?, ?)',['book','book'])
	db.commit()
	return "hello"


if __name__ == '__main__' :
	app.run()