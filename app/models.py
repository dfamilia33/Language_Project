# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 12:45:33 2018

@author: famild
"""

from app import db


#represents a word to definition post
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(64))
    definition = db.Column(db.String(256))
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    timestamp = db.Column(db.String(120))
    countries = db.relationship('Country', backref='Post', lazy=True)
    approved = db.Column(db.Boolean)
    sentence = db.Column(db.String(256))

    def __repr__(self):
        return '<User {}>'.format(self.word)  

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    abrev = db.Column(db.String(4))
    user_id = db.Column(db.Integer, db.ForeignKey('post.id')) #HAS TO BE LOWERCASE
    approved = db.Column(db.Boolean)