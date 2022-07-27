from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]

accounts={'yuval':'haha', 'judeh': 'banana', 'lian':'orange'}

@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		name = request.form['username']
		pwd = request.form['password']
		if name in accounts:
			if accounts[name]==pwd:
				return render_template('home.html', friends=facebook_friends)
			else:
				return render_template('login.html')
		else:
			return render_template('login.html')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/friend_exists/<string:name>', methods=['GET', 'POST'])
def friend_exists(name):
	if name in facebook_friends:
		exists=True
	else:
		exists=False
	return render_template('friend_exists.html', exists=exists)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)