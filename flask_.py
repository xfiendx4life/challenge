# -*- coding: utf-8 -*-
from passwordmaker import password_creator
import os
import jinja2
from flask import Flask
from flask import request
from db_processing import db_query, update
app = Flask(__name__)



template_dir = os.path.join(os.path.dirname(__file__), 'templates' )
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

def render_str(template,**params):
   t = jinja_env.get_template(template)
   return t.render(params)

def render(template, **kw):
   return render_str(template, **kw)



@app.route('/')
def hello_world():
   return render('index.html', text='Hello, stranger md5 me',
                 visible = 'Hidden',password_visibility="hidden")

@app.route('/ab86a1e1ef70dff97959067b723c5c24', methods = ['GET', 'POST'])
def welcome():
   if request.method == 'POST':
      login = request.form['login']
      password = password_creator()#generating password
      update(login, password, '100')#add entry to data base
      #show the table of results
      return render('index.html', text='hello, %s' % login, visible = "Hidden",
                    password_visibility="visible", password = password)
   
   return render('index.html', text=' - Welcome, Sranger. What is your name? ',password_visibility="hidden")


if __name__ == '__main__':
   app.run()
