PORT = 8000

import os, sys, webbrowser

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bottle'))
from bottle import route, run, template, view, redirect, request, get, static_file
import bottle

RPI = True #allow specific actions if server is running on a rasp pi
try:
    from i2c import *
    arduino = I2C()
except ImportError:
    RPI = False

bottle.TEMPLATE_PATH.append('.')

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root="static")

@route('/interface')
@view('interface.tpl')
def load():
    print "loading interface"

@route('/action', method='POST')
def action():
    val = request.forms.get('command')
    try:
        print "Pi Sending",int(val),"over i2c"
	arduino.writeNumber(int(val))
    except (ValueError, TypeError):
        print "invalid id:", val


webbrowser.open("http://localhost:"+str(PORT)+"/interface")
run(host='0.0.0.0', port=PORT, debug=True)

