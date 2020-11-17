from flask import Flask, render_template, Response, request
import RPi.GPIO as GPIO
import time
from camera_pi import Camera

app = Flask(__name__)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.output(7, True)
GPIO.output(11, True)

print ("Done")

a=1

@app.route("/")
def index():
    return render_template('index.html')

#Motor Control
@app.route('/left')
def left_side():
    data1="LEFT"
    GPIO.output(13, False)
    GPIO.output(15, True)
    return 'true'

@app.route('/right')
def right_side():
   data1="RIGHT"
   GPIO.output(13, True)
   GPIO.output(15, False)
   return 'true'

@app.route('/up')
def up_side():
   data1="FORWARD"
   GPIO.output(16, True)
   GPIO.output(18, False)
   return 'true'

@app.route('/down')
def down_side():
   data1="BACK"
   GPIO.output(16, False)
   GPIO.output(18, True)
   return 'true'

@app.route('/stop')
def stop():
   data1="STOP"
   GPIO.output(13, False)
   GPIO.output(15, False)
   GPIO.output(16, False)
   GPIO.output(18, False)
   return  'true'

@app.route('/no_turn')
def no_turn():
   data1="NOTURN"
   GPIO.output(13, False)
   GPIO.output(15, False)
   return  'true'

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    print ("Start")
    app.run(host='0.0.0.0', port =5000, debug=True, threaded=True)
