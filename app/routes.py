# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 14:27:24 2018

@author: famild
"""
from app import app, db
from flask import render_template, request
from app.models import Post

@app.route('/')
def main():
	return render_template("base.html", sentence = "PeoplesDict")

@app.route('/alpha')
def alpha():

	alphalist = Post.query.all()
	alphalist.sort(key=lambda post: (post.word))
	return render_template("alpha.html", sentence = "PeoplesDict", postlist = alphalist)

@app.route('/ranked')
def ranked():    

	ranklist = Post.query.all()
	ranklist.sort(key=lambda post: (post.upvotes), reverse = True)
	return render_template("ranked.html", sentence = "PeoplesDict", postlist = ranklist)

@app.route('/time')
def time():
	timelist = Post.query.all()
	timelist.sort(key=lambda post: (post.timestamp))
	return render_template("newest.html", sentence = "PeoplesDict", postlist = timelist)




