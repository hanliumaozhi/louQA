#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint, render_template
from ..user import User

qa = Blueprint('qa', __name__, url_prefix='')


@qa.route('/<title>')
@qa.route('/', defaults={'title': None})
def index(title):
    user = User.query.filter().first()
    return render_template("qa/index.html", title=title, tem_str=user.name)
