#!/usr/bin/env python
# -*- coding:utf-8 -*-
from kokemomo.plugins.engine.utils.km_model_utils import *
from kokemomo.plugins.engine.controller.km_db_manager import Base
from sqlalchemy.types import Text

__author__ = 'hiroki'

"""
It is blog article table to be used in the KOKEMOMO.
[Table Layouts]
    id:Integer
    info_id:Integer
    title:Text
    article:Text
    post_date:DateTime
    create_at:DateTime(Automatic Updates)
    update_at:DateTime(Automatic Updates)

"""

class KMBlogArticle(Base):
    __tablename__ = 'km_blog_article'
    id = Column(Integer, autoincrement=True, primary_key=True)
    info_id = Column(Integer)
    title = Column(Text)
    article = Column(Text)
    post_date = Column(DateTime)
    create_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    update_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __repr__(self):
        return create_repr_str(self)

    def get_json(self):
        return create_json(self)

def create(id, session):
    if id == 'None':
        article = KMBlogArticle()
        article.info_id = 0
        article.title = ""
        article.article = ""
        article.post_date = datetime.datetime.now()
    else:
        article = find(id, session)
    return article

def find(id, session):
    result = None
    for article in session.query(KMBlogArticle).filter_by(id=id).all():
        result = article
    return result

def find_by_info_id(info_id, session):
    result = []
    fetch = session.query(KMBlogArticle).filter_by(info_id=info_id).all();
    for article in fetch:
        result.append(article)
    return result

def find_all(session):
    result = []
    fetch = session.query(KMBlogArticle)
    for article in fetch.all():
        result.append(article)
    return result


def add(article, session):
    try:
        session.add(article)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def update(article, session):
    try:
        session.merge(article)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def delete(id, session):
    fetch_object = session.query(KMBlogArticle).filter_by(id=id).one()
    try:
        session.delete(fetch_object)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e