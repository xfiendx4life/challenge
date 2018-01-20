# -*- coding: utf-8 -*-
from passwordmaker import password_creator
import os #KI R4L#c2I%fT
import jinja2
from flask import Flask
from flask import request
from flask import make_response
from flask import abort, redirect, url_for
from db_processing import db_query, update
import hashlib
app = Flask(__name__)



template_dir = os.path.join(os.path.dirname(__file__), 'templates' )
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

def render_str(template,**params):
   t = jinja_env.get_template(template)
   return t.render(params)

def render(template, **kw):
   return render_str(template, **kw)

def get_hash(password):
   return hashlib.md5(password.encode('utf-8')).hexdigest()

def valid_login(login,password):
   people = db_query()
   for person in people:
      if person.name == login and get_hash(password) == person.password:
         return True
 
def check_cookies (login, password):
	people = db_query()
	for person in people:
		if person.name == login and password == person.password:
			return True 

def log_the_user_in(username, password): #add logout parameter to function and render different page in case of logout
   resp = make_response(render('signin.html',visible = "Hidden", name = username))
   print('!!!!'+username)
   resp.set_cookie('username', username)
   resp.set_cookie('password', get_hash(password))
   return resp
   
   

@app.route('/')
def hello_world():
   return render('index.html', text='Hello, stranger md5 me',
                 visible = 'Hidden',password_visibility="hidden")

@app.route('/ab86a1e1ef70dff97959067b723c5c24', methods = ['GET', 'POST'])
def welcome():
   if request.method == 'POST':
      login = request.form['login']
      password = password_creator()#generating password
      up = update(login, password, '100')#add entry to data base
      print(up)
      if up:
         #show the table of results
         return render('index.html', text='hello, %s' % login, visible = "Hidden",
                       password_visibility="visible", password = password)
      #need to set cookie here
      else:
         return redirect(url_for('login'))
   return render('index.html', text=' - Welcome, Stranger. What is your name? ',
                 password_visibility="hidden")

@app.route('/table', methods = ['GET'])
def table():
   try:
      login = request.cookies['username']
      pswd = request.cookies['password']
   except:
      login = ""
      pswd = ""

   if check_cookies(login,pswd):
      people = db_query()
      if request.method == "GET":
         return render('base.html', base = people, table_visibility = "visible", loginFlag = "hidden")
   else:
      if request.method == "GET":
         return render('base.html', table_visibility = "hidden", loginFlag = "visibles")


@app.route('/login', methods = ['GET', 'POST'])
def login():
   error = "LOG IN, My FRIEND"
   if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
      #print('!!!' + username + password)
      #print(login + password)
      if valid_login(username,password):#ниже ошибка
         return log_the_user_in(username, password)
      else:
         error = 'Invalid username/password'
   return render('signin.html', error=error)
   
@app.route('/logout') 
def logout():
   resp = make_response(render('logout.html', text="You're out, login and join us",
                 visible = 'Hidden',password_visibility="hidden"))
   resp.set_cookie("username", '')
   resp.set_cookie("password", '')
   return resp

@app.route('/second', methods = ['GET', 'POST'])
def second ():
	try:
		login = request.cookies['username']
		pswd = request.cookies['password']
		if check_cookies(login, pswd):
			return render('second.html')
	except:
		return redirect(url_for('login'))
if __name__ == '__main__':
   app.run()
