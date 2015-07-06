#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from .config import FlaskConfig

app = Flask(__name__)
app.config.from_object(FlaskConfig)
