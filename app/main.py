#!/usr/bin/env python

'''
Subsidietrekker.nl

main.py

'''


from app import app
from views import *
from streamer import *

main_app = app

if __name__ == '__main__':
    app.run()
