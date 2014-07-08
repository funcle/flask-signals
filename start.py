# -*- coding: utf-8 -*-

from flask import Flask, current_app
from flask.signals import Namespace

from signals import index_page_accessed_1, index_page_accessed_2
from signals import index_page_accessed_func_1, index_page_accessed_func_2

msignal = Namespace()

index_page_accessed = msignal.signal("index-page-accessed")

def configure_signal(app):
    @index_page_accessed.connect_via(app)
    def page_accessed(sender, changes):
        print changes

# def configure_signal(app):
#     items = [(index_page_accessed_1, index_page_accessed_func_1), 
#         (index_page_accessed_2, index_page_accessed_func_2)]
#     for signal, func in items:
#         signal.connect_via(app)(func)

def init_app(_app):
    configure_signal(_app)
    return _app

_app = Flask(__name__)
app = init_app(_app)

@app.route("/")
def home():

    index_page_accessed.send(current_app._get_current_object(), 
        changes="home-page-accessed")

    # index_page_accessed_1.send(current_app._get_current_object(), 
    #     changes="home-page-accessed")

    return '@home'

@app.route('/index', methods=["GET"])
def index():

    index_page_accessed.send(current_app._get_current_object(), 
        changes="index-page-accessed")
    
    # index_page_accessed_2.send(current_app._get_current_object(), 
    #     changes="index-page-accessed")

    return "@index"

if __name__ == "__main__":
    app.run(debug=True)


