# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 14:27:24 2018

@author: famild
"""
from app import app, db
from flask import render_template, request
from app.models import Post
from app.listhelper import slice_list, page_ind



@app.route('/')
def main():
	return render_template("base.html", sentence = "JeviDict")

@app.route('/alpha/<int:num>')
def alpha(num):


	alphalist = Post.query.all()

	if((num*25) - 25 >= len(alphalist) ):
		return render_template("error.html")

	flags = list()

	for post in alphalist:
		flags.append(post.countries.split())

	alphalist.sort(key=lambda post: (post.word))


	return render_template("alpha.html", sentence = "JeviDict", 
		postlist = slice_list(alphalist, num),
	 flaglist = flags, indlist = page_ind(num, len(alphalist)))


@app.route('/ranked/<int:num>')
def ranked(num):    

	ranklist = Post.query.all()
	
	if((num*25) - 25 >= len(ranklist) ):
		return render_template("error.html")
	

	flags = list()

	for post in ranklist:
		flags.append(post.countries.split())

	ranklist.sort(key=lambda post: (post.upvotes), reverse = True)

	return render_template("ranked.html", sentence = "JeviDict",
	 postlist = slice_list(ranklist, num), flaglist = flags)


@app.route('/time/<int:num>')
def time(num):
	timelist = Post.query.all()
	
	if((num*25) - 25 >= len(timelist) ):
		return render_template("error.html")
	
	flags = list()

	for post in timelist:
		flags.append(post.countries.split())

	timelist.sort(key=lambda post: (post.timestamp))
	return render_template("newest.html", sentence = "JeviDict",
	 postlist = slice_list(timelist, num), flaglist = flags)




