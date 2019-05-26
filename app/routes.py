# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 14:27:24 2018

@author: famild
"""
from app import app, db
from flask import render_template, request
from app.models import Post
from app.listhelper import page_ind



@app.route('/')
def main():
	return render_template("base.html", sentence = "JeviDict")

@app.route('/alpha/<int:num>')
def alpha(num):


	if num > 1:
		alphalist = Post.query.order_by(Post.word).offset((num * 25)-25).limit(num*25).all()
		# FLask SQL-Alchemy creates a relationship between a databse and a python program
		# to query, update, delete and create from a table within the python language

		"""
			SQL Equivalent:

			SELECT *
			FROM POST
			ORDER BY WORD
			OFFSET (num * 25) - 25
			LIMIT 25

		"""
	else:
		alphalist = Post.query.order_by(Post.word).limit(25).all()

		"""
			SQL Equivalent

			SELECT *
			FROM POST
			ORDER BY WORD
			LIMIT 25

		"""

	if((num*25) - 25 >= len(alphalist) ):
		return render_template("error.html")

	flags = list()

	for post in alphalist:
		flags.append(post.countries.split())

	return render_template("alpha.html", sentence = "JeviDict", postlist = alphalist,
	 flaglist = flags, indlist = page_ind(num, len(alphalist)))


@app.route('/ranked/<int:num>')
def ranked(num):    

	if num > 1:
		ranklist = Post.query.order_by(Post.upvotes.desc()).offset((num * 25)-25).limit(num*25).all()

		"""
			SQL Equivalent:

			SELECT *
			FROM POST
			ORDER BY Upvotes DESC
			OFFSET (num * 25) - 25
			LIMIT 25

		"""
	else:
		ranklist = Post.query.order_by(Post.upvotes.desc()).limit(25).all()

		"""
			SQL Equivalent:

			SELECT *
			FROM POST
			ORDER BY Upvotes DESC
			LIMIT 25

		"""

	if((num*25) - 25 >= len(ranklist) ):
		return render_template("error.html")
	

	flags = list()

	for post in ranklist:
		flags.append(post.countries.split())

	

	return render_template("ranked.html", sentence = "JeviDict",
	 postlist = ranklist, flaglist = flags, indlist = page_ind(num, len(ranklist)))


@app.route('/time/<int:num>')
def time(num):
	
	if num > 1:
		timelist = Post.query.order_by(Post.timestamp.desc()).offset((num * 25)-25).limit(num*25).all()

		"""
			SQL Equivalent:

			SELECT *
			FROM POST
			ORDER BY Timestamp DESC
			OFFSET (num * 25) - 25
			LIMIT 25

		"""
	else:
		timelist = Post.query.order_by(Post.timestamp.desc()).limit(25).all()

		"""
			SQL Equivalent:

			SELECT *
			FROM POST
			ORDER BY Timestamp DESC
			LIMIT 25

		"""
	
	if((num*25) - 25 >= len(timelist) ):
		return render_template("error.html")
	
	flags = list()

	for post in timelist:
		flags.append(post.countries.split())

	return render_template("newest.html", sentence = "JeviDict",
	 postlist = timelist, flaglist = flags, indlist = page_ind(num, len(timelist)))




