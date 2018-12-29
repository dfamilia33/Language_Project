# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 14:27:24 2018

@author: famild
"""
from app import app
from flask import render_template, request

@app.route('/')
def main():
    return render_template("base.html", sentence = "PeoplesDict")

@app.route('/alpha')
def alpha():
    return render_template("alpha.html", sentence = "PeoplesDict")

@app.route('/ranked')
def ranked():    
    return render_template("ranked.html", sentence = "PeoplesDict")



