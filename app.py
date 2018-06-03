#!/bin/python3

import sys
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route( '/' )
def hello_world():
    version = str( sys.version_info[ 0 ] ) + '.' + str( sys.version_info[ 1 ] )
    message = 'python version: ' +  version

    return message
    #return 'darve' + 'WTF'

@app.route( '/insult/<_name>' )
def insult( _name ):
    return 'Nobody loves ' + _name

@app.route( '/hello/' )
@app.route( '/hello/<_name>' )
def hello( _name='nobody' ):
    #return 'Hi there: ' + _name
    return render_template( 'hello.html', name=_name )
