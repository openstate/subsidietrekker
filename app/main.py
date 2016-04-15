'''
Subsidietrekker.nl

main.py

'''


from app import app


from forms import *
from views import *
from streamer import *

if __name__ == '__main__':
    app.run(debug=True) # CARE! debug mode is on!
