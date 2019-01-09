

from flask import Flask
from flask import Flask, render_template, request, jsonify
import RPi.GPIO as GPIO
import time

app = Flask(__name__)
print('start')
m1p=21
m2p=26
m3p=17
m4p=18
m11=16
m12=20
m21=19
m22=13
m31=27
m32=22
m41=23
m42=24
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(m21, GPIO.OUT)
GPIO.setup(m22, GPIO.OUT)
GPIO.setup(m31, GPIO.OUT)
GPIO.setup(m32, GPIO.OUT)
GPIO.setup(m41, GPIO.OUT)
GPIO.setup(m42, GPIO.OUT)
GPIO.setup(m1p, GPIO.OUT)
GPIO.setup(m2p, GPIO.OUT)
GPIO.setup(m3p, GPIO.OUT)
GPIO.setup(m4p, GPIO.OUT)
p1 = GPIO.PWM(m1p,50)
p2 = GPIO.PWM(m2p,50)
p3 = GPIO.PWM(m3p,50)
p4 = GPIO.PWM(m4p,50)

p1.start(50)
p2.start(50)
p3.start(50)
p4.start(50)
GPIO.output(m11, 0)
GPIO.output(m12, 0)
GPIO.output(m21, 0)
GPIO.output(m22, 0)
GPIO.output(m31, 0)
GPIO.output(m32, 0)
GPIO.output(m41, 0)
GPIO.output(m42, 0)
GPIO.output(m1p, 0)
GPIO.output(m2p, 0)
GPIO.output(m3p, 0)
GPIO.output(m4p, 0)
print ('Done')

a=1
@app.route("/")
def index():
  return render_template('robot.html')

@app.route('/left_side')
def left_side():
  data1="LEFT"
  GPIO.output(m1p, 1)
  GPIO.output(m2p, 1)
  GPIO.output(m3p, 1)
  GPIO.output(m4p, 1)
  GPIO.output(m11, 1)
  GPIO.output(m12 , 0)
  GPIO.output(m21 , 0)
  GPIO.output(m22 , 1)
  GPIO.output(m31 , 1)
  GPIO.output(m32 , 0)
  GPIO.output(m41 , 0)
  GPIO.output(m42 , 1)
  return 'true'

@app.route('/right_side')
def right_side():
  data1="RIGHT"
  GPIO.output(m1p, 1)
  GPIO.output(m2p, 1)
  GPIO.output(m3p, 1)
  GPIO.output(m4p, 1)
  GPIO.output(m11 , 0)
  GPIO.output(m12 , 1)
  GPIO.output(m21 , 1)
  GPIO.output(m22 , 0)
  GPIO.output(m31 , 0)
  GPIO.output(m32 , 1)
  GPIO.output(m41 , 1)
  GPIO.output(m42 , 0)
  return 'true'

@app.route('/up_side')
def up_side():
  data1="FORWARD"
  GPIO.output(m1p, 1)
  GPIO.output(m2p, 1)
  GPIO.output(m3p, 1)
  GPIO.output(m4p, 1)
  GPIO.output(m11 , 1)
  GPIO.output(m12 , 0)
  GPIO.output(m21 , 1)
  GPIO.output(m22 , 0)
  GPIO.output(m31 , 1)
  GPIO.output(m32 , 0)
  GPIO.output(m41 , 1)
  GPIO.output(m42 , 0)
  return 'true'

@app.route('/down_side')
def down_side():
  data1="BACK"
  GPIO.output(m1p, 1)
  GPIO.output(m2p, 1)
  GPIO.output(m3p, 1)
  GPIO.output(m4p, 1)
  GPIO.output(m11 , 0)
  GPIO.output(m12 , 1)
  GPIO.output(m21 , 0)
  GPIO.output(m22 , 1)
  GPIO.output(m31 , 0)
  GPIO.output(m32 , 1)
  GPIO.output(m41 , 0)
  GPIO.output(m42 , 1)
  return 'true'

@app.route('/stop')
def stop():
  data1="STOP"
  GPIO.output(m1p, 0)
  GPIO.output(m2p, 0)
  GPIO.output(m3p, 0)
  GPIO.output(m4p, 0)
  GPIO.output(m11 , 0)
  GPIO.output(m12 , 0)
  GPIO.output(m21 , 0)
  GPIO.output(m22 , 0)
  GPIO.output(m31 , 0)
  GPIO.output(m32 , 0)
  GPIO.output(m41 , 0)
  GPIO.output(m42 , 0)
  return  'true'


@app.route('/')
def my_form():
   return render_template('robot.html')

@app.route('/', methods = ['POST', 'GET'])
def my_form_post1():
   if request.method == 'POST':
      print("First")
      form_name = next(iter(request.form))
      print(next(iter(request.form.values())))
      result = next(iter(request.form.values()))
      if form_name == "form1":
         resultfunction1(result)
      elif form_name == "form2":
         resultfunction2(result)
      elif form_name == "form3":
         resultfunction3(result)
      elif form_name == "form4":
         resultfunction4(result)
      return render_template('robot.html')

def resultfunction1(result):
#Use result as a constant in this function
   result = (float(result)/18)+2
   print(result)
   print("first")
   return jsonify(result),200

def resultfunction2(result):
#Use result as a constant in this function
   result = (float(result)/18)+2
   print(result)
   print("second")
   return jsonify(result),200

def resultfunction3(result):
#Use result as a constant in this function
   result = (float(result)/18)+2
   print(result)
   print("third")
   return jsonify(result),200

def resultfunction4(result):
#Use result as a constant in this function
   result = (float(result)/18)+2
   print(result)
   print("fourth")
   return jsonify(result),200

if __name__ == "__main__":
   print ('Start')
   app.run(host='0.0.0.0',port=5010)

