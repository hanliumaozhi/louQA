#!/usr/bin/env python
# encoding: utf-8

from flask import (Blueprint, request, current_app, redirect, url_for,
        jsonify)
from .models import User
from sqlalchemy import or_
from ..dbs import db
from flask.ext.login import login_user


user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/signup', methods=['POST'])
def signup_user():
    try:
        user_instance = User.query.filter(or_(User.name==request.form['name'],
                                            User.email==request.form['email'])).first()
        if user_instance:
            return jsonify(status="error", info=u"已存在该用户")
        else:
            user_instance = User()
            user_instance.name = request.form['name']
            user_instance.email = request.form['email']
            user_instance.set_password(request.form['password'])
            db.session.add(user_instance)
            db.session.commit()
            return jsonify(status="success", info=u"创建成功")
    except Exception as e:
        current_app.logger.error(e)
        return redirect(url_for('qa.index'))


@user.route('/login', methods=['POST'])
def login_users():
    try:
        user_instance = User.query.filter(User.name==request.form['name']).first()
        if user_instance:
            if user_instance.verify_password(request.form['password']):
                login_user(user_instance)
        return redirect(url_for('qa.index'))
    except Exception as e:
        current_app.logger.error(e)
        return redirect(url_for('qa.index'))
