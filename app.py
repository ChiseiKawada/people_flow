# -*- coding: utf-8 -*-
from flask import *  # 必要なライブラリのインポート
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, func
from flaski.database import db_session
from flaski.models import People_flow
import os
import sqlite3
import datetime
#from flask import Flask, render_template, abort

app = Flask(__name__)
#app.config['DEBUG'] = True

# 起動されたサーバーの/にアクセスした時の挙動を記述。
# @app.route("/hoge")で記述すれば、http://127.0.0.1:5000/aaでアクセスした時の挙動を記述できる。
@app.route("/")
def main():
    contents = People_flow.query.all()
    # index.htmlにcontensを引数に渡して実行。
    return render_template("index.html", contents=contents)

#sigfoxから受信したデータをDBに格納する
@app.route("/people_count", methods=["GET", "POST"])
def people():

    people_data = []
    all_column = People_flow.query.all()

    if request.method == "POST":
        people_data  = []
        people_data  = request.json

        people_flow = People_flow()
        people_flow.count = float(people_data["people_float"])
        people_flow.date = datetime.datetime.now()

        # db_session.add(people_flow)
        # db_session.commit()

    return render_template("people.html", info=people_data, all_column=all_column)

@app.route("/getInfo", methods=["GET", "POST"])
def get_info():
    pass

if __name__ == "__main__":  # 実行されたら
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)  # デバッグモード、localhost:8888 で スレッドオンで実行