#!/bin/python3

import sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    version = str( sys.version_info[ 0 ] ) + '.' + str( sys.version_info[ 1 ] )
    return 'asdf python version: ' +  version
    #return 'darve' + 'WTF'

