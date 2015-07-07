#!/usr/bin/env python
# encoding: utf-8

from ..dbs import db
from sqlalchemy import Column
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):

    __tablename__ = 'users'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(32), nullable=False, unique=True)
    email = Column(db.String(64), nullable=False, unique=True)

    __password = Column(db.String(128))

    def set_password(self, password):
        self.__password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.__password, password)
