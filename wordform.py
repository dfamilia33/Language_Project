# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 13:30:38 2018

@author: famild
"""

from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms.validators import DataRequired


class WordForm(Form):
    word = TextField("verb")
    submit = SubmitField("enter", validators = [DataRequired()])
    
    
    