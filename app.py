#!/usr/bin/env python
from flask import Flask, render_template, Response, request
from i2c import I2C
from camera_pi import Camera
import os

RobotArduino = I2C(); #The robot's arduino controller

app = Flask(__name__, template_folder='site')

@app.route('/')
def index():
    """Main page: controller + video stream"""
    return render_template('index.html')

@app.route('/action', methods=['POST'])
def action():
    """Handle button presses - Send commands to the robot"""
    val = request.form.get('command')

    print("Sending ["+str(val)+"] To Arduino")
    RobotArduino.writeNumber(int(val))

    return ('',204) #no response

def gen(camera):
    """Video streaming generator function."""
    while True:
	import time
	time.sleep(1./24.)
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/shutdown', methods=['POST'])
def poweroff():
    """Turn off the server and Raspberry Pi to allow safe power removal"""
    request.environ.get('werkzeug.server.shutdown')()
    os.system('sudo shutdown -h now')
    return 'Powering down'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True, port=8000)
