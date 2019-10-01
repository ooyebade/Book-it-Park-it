#import click #for command line arguments
#from flask.ext.runner import Runner(also for comand line arguments)
from flask import jsonify
from importlib import reload
import time
#from flask_ngrok import run_with_ngrok
from flask import Flask, flash, redirect, render_template, request, session, abort,url_for,send_from_directory
import os,sys



app = Flask(__name__)



DEBUG =True
PORT = 5001

mylist=[]

@app.route('/',methods=['POST','GET'])
@app.route('/index',methods=['POST','GET'])
def home():
	if request.method == 'POST':
		username = request.form['uname']
		password = request.form['psw']
		mylist.append(username)
		mylist.append(password)
		print(username+" "+password)	
		return redirect(url_for('spots'))
	return render_template('index.html')

@app.route('/conference')
def conference():
	return render_template('conference.html')
@app.route('/spots')
def spots():
	
	return render_template('spots.html')




if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	if DEBUG:
		app.run(host='0.0.0.0', debug=True,port=PORT)
	else:
		#run_with_ngrok(app)

		app.run()