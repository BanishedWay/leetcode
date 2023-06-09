#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'使用模版'

__author__ = 'BanishedWay'

from flask import Flask, request, render_template
from gevent import pywsgi

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_from():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == '1234':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html',
                           message='Bad username or password',
                           username=username)


if __name__ == '__main__':
    ##  app.run()
    server = pywsgi.WSGIServer(("0.0.0.0", 80), app)
    server.serve_forever()
