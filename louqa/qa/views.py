#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint, render_template, current_app, jsonify, request, redirect, url_for
from ..user import User
from flask.ext.login import current_user
from .models import Question, Answer, Comment
from ..dbs import db

qa = Blueprint('qa', __name__, url_prefix='')


@qa.route('/', methods=["GET"])
def index():
    return render_template("qa/index.html", current_user=current_user)


@qa.route('/question/add', methods=["GET"])
def add_question():
    return render_template("qa/ask_question.html")


@qa.route('/question', methods=["GET", "POST"])
def question_info():
    try:
        if request.method == "POST":
            if not current_user.is_authenticated():
                return jsonify(status="error", info=u"请先登录")
            question_instance = Question.query.filter(Question.name==request.form['title']).first()
            if question_instance:
                return jsonify(status="error", info=u"已存在该问题")
            else:
                question_instance = Question()
                question_instance.author_id = current_user.id
                question_instance.name = request.form['title']
                question_instance.content = request.form['content']
                db.session.add(question_instance)
                db.session.commit()
                return jsonify(status="success", info=u"创建成功")
        else:
            question_list = Question.query.filter().all()
            return render_template("qa/questions.html", qss=question_list)
    except Exception as e:
        current_app.logger.error(e)
        if request.method == "POST":
            return jsonify(status="error", info=u"错误")
        else:
            return redirect(url_for('qa.index'))


@qa.route('/question/<int:question_id>', methods=['GET', 'POST'])
def questions(question_id):
    try:
        if request.method == "GET":
            question_instance = Question.query.filter(Question.id==question_id).first()
            if question_instance:
                return render_template("qa/question_detail.html", qs=question_instance)
            return redirect(url_for('qa.index'))
    except Exception as e:
        current_app.logger.error(e)
        return redirect(url_for('qa.index'))

