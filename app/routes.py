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
	def alphasort(post):
		return post.word

	alphalist = Post.query.all()
	alphalist.sort(key = alphasort)
	return render_template("alpha.html", sentence = "PeoplesDict", postlist = alphalist)

@app.route('/ranked')
def ranked():    
	"""def ranksort(post1, post2):
		return ((post1.upvotes < post2.upvotes) or (post1.upvotes == post2.upvotes and post1.word < post2.word ))"""

	ranklist = Post.query.all()
	ranklist.sort(key=lambda post: (post.upvotes, post.word))
	return render_template("ranked.html", sentence = "PeoplesDict", postlist = ranklist)



