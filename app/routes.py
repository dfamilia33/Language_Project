# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 14:27:24 2018

@author: famild
"""
from app import app, db
from flask import render_template, request
from app.models import Post, Country
from app.listhelper import page_ind
import math



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



	

	return render_template("ranked.html", sentence = "JeviDict",
	 postlist = ranklist, flaglist = flags, indlist = page_ind(num, len(ranklist))) #not going to work past 1 since ranklst is only 25 long


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


	return render_template("newest.html", sentence = "JeviDict",
	 postlist = timelist, flaglist = flags, indlist = page_ind(num, len(timelist)))

@app.route('/by_Country/<abrev_in>/<int:num>')
def country(abrev_in,num):
	cnt_list = Country.query.filter_by(abrev = abrev_in)

	postlist = list()

	for i in cnt_list:
		postlist.append(Post.query.get(i.user_id))

	name_of_country = cnt_list[0].name
	flags = list()

	return render_template("country.html", name_of_country = name_of_country,
	 abrev = abrev_in, page = num, page_len = int(math.ceil(len(postlist)/25.0)), sentence = "JeviDict",
	 postlist = postlist, flaglist = flags, indlist = page_ind(num, len(postlist)))

	#need to SELECT COUNT(*) FROM POST for page_in and page_len to work
	#ing pagelen len(postlist) needs to be replaced with a query that does SELECT COUNT(*) FROM POST






