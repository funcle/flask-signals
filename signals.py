# -*- coding: utf-8 -*-

from flask.signals import Namespace

msignal = Namespace()

index_page_accessed_1 = msignal.signal("index-page-accessed-1")
index_page_accessed_2 = msignal.signal("index-page-accessed-2")

def index_page_accessed_func_1(sender, changes):
    print "index_page_accessed_func_1"

def index_page_accessed_func_2(sender, changes):
    print "index_page_accessed_func_2"