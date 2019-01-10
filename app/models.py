# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 12:45:33 2018

@author: famild
"""

from app import db


#represents a word to definition post
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(64))#, index=True, unique=True)
    definition = db.Column(db.String(256))
    countries = db.Column(db.String(100))
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    timestamp = db.Column(db.String(120))

    def __repr__(self):
        return '<User {}>'.format(self.word)  