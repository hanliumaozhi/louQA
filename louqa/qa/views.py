#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint, render_template
from ..user import User
from flask.ext.login import current_user

qa = Blueprint('qa', __name__, url_prefix='')


@qa.route('/<title>')
@qa.route('/', defaults={'title': None})
def index(title):
    return render_template("qa/index.html", current_user=current_user)
