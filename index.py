#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import os


# In[8]:


server = Flask(__name__)


# In[9]:


@server.route('/')
def home():
    return render_template('main.html')

@server.route('/index.html', methods=['GET', 'POST'])
def admin():
    return render_template('index.html')

@server.route('/blank.html', methods=['GET', 'POST'])
def blank():
    return render_template('blank.html')

@server.route('/register.html', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@server.route('/extract_vehicles')
def extract():
    os.system('python extract.py')
    return render_template('blank.html')


# In[10]:


if __name__ == "__main__":
    server.static_folder = 'static'
    server.run()

