# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 14:27:24 2018

@author: famild
"""
from app import app, db
from flask import render_template, request, jsonify
from app.models import Post, Country
from app.listhelper import page_ind
import math
from sqlalchemy import and_
import datetime

abrevdict =	{
	"AR" : "Argentina",
	"BO" : "Bolivia",
	"BR" : "Brazil",
	"CL" : "Chile",
	"CO" : "Colombia",
	"CR" : "Costa Rica",
	"CU" : "Cuba",
	"DO" : "Dominican Republic",
	"EC" : "Ecuador",
	"SV" : "El Salvador",
	"GT" : "Guatemala",
	"HN" : "Honduras",
	"MX" : "Mexico",
	"NI" : "Nicaragua",
	"PA" : "Panama",
	"PY" : "Paraguay",
	"PE" : "Peru",
	"PR" : "Puerto Rico",
	"ES" : "Spain",
	"UY" : "Uruguay",
	"VE" : "Venezuela",
	"Argentina": "AR",
	"Bolivia" : "BO",
	"Brazil" : "BR",
	"Chile" : "CL",
	"Colombia" : "CO",
	"Costa Rica" : "CR",
	"Cuba" : "CU",
	"Dominican Republic" : "DO",
	"Ecuador" : "EC",
	"El Salvador" : "SV",
	"Guatemala" : "GT",
	"Honduras" : "HN",
	"Mexico" : "MX",
	"Nicaragua" : "NI",
	"Panama" : "PA",
	"Paraguay" : "PY",
	"Peru" : "PE",
	"Puerto Rico" : "PR",
	"Spain" : "ES",
	"Uruguay" : "UY",
	"Venezuela" : "VE"
	}		  


@app.route('/')
def main():
	ranklist = Post.query.filter_by(approved=True).order_by(Post.upvotes.desc()).limit(25).all()

	"""
			SQL Equivalent:

			SELECT *
			FROM POST
			ORDER BY Upvotes DESC
			LIMIT 25

	"""

	num = 1
	

	flags = list()

	for i in ranklist:
		flags.append(i.countries)

	

	return render_template("content.html", sentence = "JeviDict", link = "/ranked/", para = "Here all dictionary entries will be sorted by rank",
	 postlist = ranklist, flaglist = flags, indlist = page_ind(num, len(ranklist)),
	 page = num, page_len = int(math.ceil(Post.query.filter_by(approved=True).count()/25.0)))

@app.route('/alpha/<int:num>')
def alpha(num):


	if num > 1:
		alphalist = Post.query.filter_by(approved=True).order_by(Post.word).offset((num * 25)-25).limit(num*25).all()
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
		alphalist = Post.query.filter_by(approved=True).order_by(Post.word).limit(25).all()

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


	return render_template("alpha.html", sentence = "JeviDict", postlist = alphalist, link = "/alpha/",
	 flaglist = flags, indlist = page_ind(num, len(alphalist)),
	 page = num, page_len = int(math.ceil(Post.query.filter_by(approved=True).count()/25.0)))


@app.route('/ranked/<int:num>')
def ranked(num):    

	if num > 1:
		ranklist = Post.query.filter_by(approved=True).order_by(Post.upvotes.desc()).offset((num * 25)-25).limit(num*25).all()

		"""
			SQL Equivalent:

			SELECT *
			FROM POST
			ORDER BY Upvotes DESC
			OFFSET (num * 25) - 25
			LIMIT 25

		"""
	else:
		ranklist = Post.query.filter_by(approved=True).order_by(Post.upvotes.desc()).limit(25).all()

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

	for i in ranklist:
		flags.append(i.countries)

	

	return render_template("content.html", sentence = "JeviDict", link = "/ranked/", para = "Here all dictionary entries will be sorted by rank",
	 postlist = ranklist, flaglist = flags, indlist = page_ind(num, len(ranklist)),
	 page = num, page_len = int(math.ceil(Post.query.filter_by(approved=True).count()/25.0))) #not going to work past 1 since ranklst is only 25 long


@app.route('/time/<int:num>')
def time(num):
	
	if num > 1:
		timelist = Post.query.filter_by(approved=True).order_by(Post.timestamp.desc()).offset((num * 25)-25).limit(num*25).all()

		"""
			SQL Equivalent:

			SELECT *
			FROM POST
			ORDER BY Timestamp DESC
			OFFSET (num * 25) - 25
			LIMIT 25

		"""
	else:
		timelist = Post.query.filter_by(approved=True).order_by(Post.timestamp.desc()).limit(25).all()

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

	for i in timelist:
		flags.append(i.countries)


	return render_template("content.html", sentence = "JeviDict", link = "/time/", para = "Here all dictionary entries will be sorted by time posted",
	 postlist = timelist, flaglist = flags, indlist = page_ind(num, len(timelist)),
	 page = num, page_len = int(math.ceil(Post.query.filter_by(approved=True).count()/25.0)))

@app.route('/by_Country/<abrev_in>/<int:num>')
def country(abrev_in,num):
	cnt_list = list()

	zero_results = False
	
	if num >1:
		cnt_list = Country.query.filter_by(abrev = abrev_in, approved=True).offset((num * 25)-25).limit(num*25).all()
	else:
		cnt_list = Country.query.filter_by(abrev = abrev_in, approved=True).limit(25).all()
	

	cnt_count = Country.query.filter_by(abrev = abrev_in, approved=True).count()	
	
	page_len = int(math.ceil(cnt_count/25.0))
	
	postlist = list()
	flags = list()


	for i in cnt_list:
		postlist.append(Post.query.get(i.user_id))
		flags.append(Post.query.get(i.user_id).countries)


	name_of_country = abrevdict[abrev_in]

	if len(cnt_list) == 0:
		zero_results = True
	
	



	return render_template("country.html", name_of_country = name_of_country, zero_results = zero_results,
	 abrev = abrev_in, page = num, page_len = page_len, sentence = "JeviDict",
	 postlist = postlist, flaglist = flags, indlist = page_ind(num, cnt_count))

	#need to SELECT COUNT(*) FROM POST for page_in and page_len to work
	#ing pagelen len(postlist) needs to be replaced with a query that does SELECT COUNT(*) FROM POST

@app.route('/voting', methods = ["POST"])
def vote():

	op = request.form.get('operation')
	idnum = request.form.get('id')
	state = request.form.get('state')
	typ = request.form.get('type')
	val1 = 0

	if typ == 'upvote':
		if op == '+':
			Post.query.get(idnum).upvotes += 1
			if state == "up":
				Post.query.get(idnum).downvotes -= 1

		if op == '-':
			Post.query.get(idnum).upvotes -= 1

	if typ == 'downvote':
		if op == '+':
			Post.query.get(idnum).downvotes += 1
			if state == "up":
				Post.query.get(idnum).upvotes -= 1

		if op == '-':
			Post.query.get(idnum).downvotes -= 1


	db.session.commit()
	val1 = Post.query.get(idnum).upvotes
	val2 = Post.query.get(idnum).downvotes
	return jsonify({"success": True, "upvalue":val1, "downvalue" : val2})

@app.route('/wordresult/<term>')
def wordresult(term):    

	resultlist = Post.query.filter(Post.word.like("%" + term + "%")).order_by(Post.upvotes.desc()).all()


	flags = list()

	for i in resultlist:
		flags.append(i.countries)

	

	return render_template("wordgroup.html", sentence = "JeviDict", para = "Results for \'" + term + "\'",
	 postlist = resultlist, flaglist = flags) #not going to work past 1 since ranklst is only 25 long


@app.route('/searchresult',methods = ["POST"])
def searchresult():

	term = request.form['searchword']

	resultlist = Post.query.filter(and_(Post.word.like( term + "%"), Post.approved==True )).order_by(Post.upvotes.desc()).all()

	para = ""

	if not resultlist:
		para = "No results found for \'" + term + "\'"
	else:
		para = "Results for \'" + term + "\'"

	

	flags = list()

	for i in resultlist:
		flags.append(i.countries)

	

	return render_template("wordgroup.html", sentence = "JeviDict", para = para,
	 postlist = resultlist, flaglist = flags) #not going to work past 1 since ranklst is only 25 long

@app.route('/suggestion')
def suggestion():
	
	return render_template("suggestion.html", sentence = "JeviDict" )    

@app.route('/suggestpost', methods = ["POST"])
def suggestpost():
	try:
		word = request.form.get('word')
		definition = request.form.get('definition')
		sentence = request.form.get('sentence')

		countries = request.form.get('countries').split(",")



		mypost = Post(word=word,definition=definition,upvotes=0,downvotes=0,timestamp=datetime.datetime.now(),approved =False,sentence=sentence)
		db.session.add(mypost)

		for i in countries:
			mycount = Country(name= i ,abrev=abrevdict[i],Post=mypost,approved = False)
			db.session.add(mycount)

		db.session.commit()

		return jsonify({"success": True})
	except:
		return jsonify({"success": False})


