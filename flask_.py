# -*- coding: utf-8 -*-

import os
import jinja2
from flask import Flask
from flask import request
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
   return render('index.html', text='Hello, stranger md5 me', visible = 'Hidden',
                 visible_password = "Hidden")

@app.route('/ab86a1e1ef70dff97959067b723c5c24', methods = ['GET', 'POST'])
def welcome():
   if request.method == 'POST':
      login = request.form['login']
      #should access db and if there is no entry for this username ask to make a password
      return render('index.html', text='hello, %s' % login, visible_password = "visible")
   return render('index.html', text=' - Welcome, Sranger. What is your name? ')


if __name__ == '__main__':
   app.run()
