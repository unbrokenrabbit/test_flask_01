#!/bin/python3

import sys
from flask import Flask
from flask import render_template
from flask import flash
from flask import redirect
#from app import app
#from app.forms import LoginForm
from forms import LoginForm

app = Flask(__name__)
app.config.update( dict( SECRET_KEY='go fuck yourself' ) )

@app.route( '/' )
def home():
    version = str( sys.version_info[ 0 ] ) + '.' + str( sys.version_info[ 1 ] )
    message = 'python version: ' +  version

    user = { 'username': 'Darve' }

    return render_template( 'home.html', user=user, title='Moneys' )

    #return 'darve' + 'WTF'

@app.route( '/import' )
def importThings():
    debugTransactions = [
        { 'date': '02/13/2018', 'description': 'ORKIN  LLC 002', 'amount': -85.00 },
        { 'date': '02/12/2018', 'description': 'HLU*Hulu 15253597-U', 'amount': -11.99 },
        { 'date': '02/11/2018', 'description': 'Netflix.com', 'amount': -10.99 },
        { 'date': '02/09/2018', 'description': 'AUTO-OWNERS INSURANCE', 'amount': -2496.46 },
        { 'date': '02/05/2018', 'description': 'COMCAST CHICAGO', 'amount': -79.95 },
        { 'date': '02/04/2018', 'description': 'Payment Thank You - Web', 'amount': 325.47 },
        { 'date': '01/25/2018', 'description': 'AT&amp;T*BILL PAYMENT', 'amount': -138.91 },
        { 'date': '01/12/2018', 'description': 'HLU*Hulu 15253597-U', 'amount': -11.99 },
        { 'date': '01/10/2018', 'description': 'Netflix.com', 'amount': -10.99 },
        { 'date': '01/05/2018', 'description': 'COMCAST CHICAGO', 'amount': -79.95 },
        { 'date': '01/04/2018', 'description': 'Payment Thank You - Web', 'amount': 279.97 },
        { 'date': '12/25/2017', 'description': 'AT&amp;T*BILL PAYMENT', 'amount': -137.54 },
        { 'date': '12/12/2017', 'description': 'HLU*Hulu 15253597-U', 'amount': -11.99 },
        { 'date': '12/13/2017', 'description': 'ORKIN  LLC 002', 'amount': -85.00 },
        { 'date': '12/10/2017', 'description': 'Netflix.com', 'amount': -10.99 },
        { 'date': '12/05/2017', 'description': 'COMCAST CHICAGO', 'amount': -79.95 },
        { 'date': '12/03/2017', 'description': 'Payment Thank You - Web', 'amount': 242.46 },
        { 'date': '11/26/2017', 'description': 'AT&amp;T*BILL PAYMENT', 'amount': -137.54 },
        { 'date': '11/16/2017', 'description': 'DR FUHRMAN ONLINE', 'amount': -39.50 },
        { 'date': '11/12/2017', 'description': 'HLU*Hulu 15253597-U', 'amount': -11.99 },
    ]
    return render_template( 'import.html', transactions=debugTransactions )

@app.route( '/report' )
def report():
    return render_template( 'report.html' )

@app.route( '/login', methods=['GET', 'POST'] )
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template( 'login.html', title='Sign In', form=form )

@app.route( '/insult/<_name>' )
def insult( _name ):
    return 'Nobody loves ' + _name

@app.route( '/hello/' )
@app.route( '/hello/<_name>' )
def hello( _name='nobody' ):
    #return 'Hi there: ' + _name
    return render_template( 'hello.html', name=_name )
