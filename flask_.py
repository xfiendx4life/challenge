# -*- coding: utf-8 -*-
from passwordmaker import password_creator
import os
import jinja2
from flask import Flask
from flask import request
from flask import make_response
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
         
def log_the_user_in(username, password):
   

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
         resp = make_response(render('index.html',
                                     text='hello, %s' % login, visible = "Hidden",
                       password_visibility="visible",
                                     password = "You've already registered"))
         resp.set_cookie('username', login)
         resp.set_cookie('password', get_hash(password))
         return resp
   return render('index.html', text=' - Welcome, Stranger. What is your name? ',
                 password_visibility="hidden")

@app.route('/table', methods = ['GET'])
def table():
   people = db_query()
   if request.method == "GET":
      return render('table.html', base = people)

@app.route('/login', methods = ['GET', 'POST'])
def login():
   error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render('login.html', error=error)
   
   

if __name__ == '__main__':
   app.run()
