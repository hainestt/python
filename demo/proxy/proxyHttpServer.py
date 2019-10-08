# !/usr/local/bin/python3.7
# -*- coding: utf-8 -*-

import redis
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

r = redis.Redis(host='localhost', encoding='UTF-8', decode_responses=True)

class Proxy(Resource):
    def get(self):
        return r.keys('*')
    
api.add_resource(Proxy, '/proxy.json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    