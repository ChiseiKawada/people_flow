# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from flaski.database import Base
from datetime import datetime

class People_flow(Base):
    __tablename__ = 'counter'                  # テーブル名
    count = Column(Float, primary_key=True)        # カラム１(count) 計測した人数
    date = Column(DateTime, default=datetime.now()) # カラム２(date) デフォルト現在日時を設定

    def __init__(self, count=None, date=None):
        self.count = count
        self.date = date

# class WikiContent(Base):
#    __tablename__ = 'wikicontents'                  # テーブル名
#    id = Column(Integer, primary_key=True)          # カラム１(id)
#    title = Column(String(128), unique=True)        # カラム２(title)
#    body = Column(Text)                             # カラム3(body)
#    date = Column(DateTime, default=datetime.now()) # カラム４(date) デフォルト現在日時を設定

#    def __init__(self, title=None, body=None, date=None):
#        self.title = title
#        self.body = body
#        self.date = date

#    def __repr__(self):
#        return '<Title %r>' % (self.title)