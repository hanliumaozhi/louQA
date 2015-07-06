#!/usr/bin/env python
# encoding: utf-8

from ..dbs import db
from sqlalchemy import Column


class User(db.Model):

    __tablename__ = 'users'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(32), nullable=False, unique=True)
