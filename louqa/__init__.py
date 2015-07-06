#!/usr/bin/env python
# encoding: utf-8

from .qa import qa
from .flask_app import app
from .dbs import db

app.register_blueprint(qa)
