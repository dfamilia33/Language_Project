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
	return render_template("base.html", sentence = "JeviDict")

@app.route('/alpha')
def alpha():

	alphalist = Post.query.all()
	flags = list()

	for post in alphalist:
		flags.append(post.countries.split())

	alphalist.sort(key=lambda post: (post.word))



	return render_template("alpha.html", sentence = "JeviDict", postlist = alphalist, flaglist = flags)

@app.route('/ranked')
def ranked():    

	ranklist = Post.query.all()
	flags = list()

	for post in ranklist:
		flags.append(post.countries.split())

	ranklist.sort(key=lambda post: (post.upvotes), reverse = True)
	return render_template("ranked.html", sentence = "JeviDict", postlist = ranklist, flaglist = flags)

@app.route('/time')
def time():
	timelist = Post.query.all()
	flags = list()

	for post in timelist:
		flags.append(post.countries.split())

	timelist.sort(key=lambda post: (post.timestamp))
	return render_template("newest.html", sentence = "JeviDict", postlist = timelist, flaglist = flags)




