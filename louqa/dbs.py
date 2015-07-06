#!/usr/bin/env python
# encoding: utf-8

from flask.ext.sqlalchemy import SQLAlchemy
from .flask_app import app

db = SQLAlchemy(app)
