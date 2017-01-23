from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)


@app.route('/testlist/')
def renderList():
	La = [1,2,3,4]
	return render_template('user.html', La=La)


if __name__ == '__main__':
	app.run()