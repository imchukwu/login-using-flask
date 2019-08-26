from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['password'] == 'password' and request.form['username'] == 'admin':
			return redirect("http://www.idscatiafrica.com/")
		else:
			flash('wrong login details!')
			
	return render_template('index.html')


if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True, port=4000)

