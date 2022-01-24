# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_cors import CORS 
from parser import yandex_news, ria_news, lenta_news
import json
from jsonmerge import merge


app = Flask(__name__)


app.config['JSON_AS_ASCII'] = False
app.config.from_object(__name__)

all_new = [*yandex_news,*ria_news, *lenta_news]

CORS(app, resources={r'/*':{'origins': "*", "allow_headers":"Access-Control-Allow-Origin"}})
@app.route('/', methods=['GET'])
def greeting():
    return("Hello, world!")


@app.route('/hi_shark', methods=['GET'])
def shark():
    return("New Shark!")


json.dumps(all_new, ensure_ascii=False)

@app.route('/news', methods=['GET'])
def all_news():
    return jsonify({
        'news': all_new,
        "status": 'success'
    })

if __name__ == "__main__":
    app.run(debug=True)
