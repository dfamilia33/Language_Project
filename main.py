# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 13:49:31 2018

@author: famild
"""

from flask import Flask, render_template, session, request
app = Flask(__name__)


@app.route('/')
def main():
    return render_template("base.html")

@app.route('/check', methods = ['POST','GET'])
def check():
    if request.method == 'POST':
      result = request.form
      if result.get('box') == 'test':
          return render_template("trueorfalse.html",torf = "Correct")
      else:
          return render_template("trueorfalse.html",torf = "Incorrect")









app.secret_key = 'your secret'
app.config['SESSION_TYPE'] = 'filesystem'

if __name__ == '__main__':
  app.run(host='0.0.0.0')
    