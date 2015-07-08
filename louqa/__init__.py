#!/usr/bin/env python
# encoding: utf-8

from .qa import qa
from .user import user
from .flask_app import app
from .dbs import db
from .extensions import login_manager
from .user import User


def configure_login(app):
    login_manager.login_view = 'qa.index'
    login_manager.refresh_view = 'qa.index'
    login_manager.login_message = None
    login_manager.session_protection = "basic"

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)
    login_manager.setup_app(app)

app.register_blueprint(qa)
app.register_blueprint(user)
configure_login(app)
