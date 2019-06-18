###Walker Wind 
###6/11/19
###Flask code for setting up local web server

#note to self: alt + shift + 3 shows line numbers in nano

#import necessary libraries
from flask import Flask, request, render_template, url_for
import os
import random
import string

CHART_FOLDER = os.path.join('static')

app= Flask(__name__)
app.config['CHART_FOLDER'] = CHART_FOLDER

###function that generates a random string to plop on the end of the URL
def random_generator(size=6, chars=string.ascii_uppercase +string.digits):
    return ''.join(random.choice(chars) for x in range(size))


key=random_generator()
print("Type this key after the page you want: ", key)

#define home index
@app.route("/",methods= ['GET','POST'])
def index():
    return render_template('indexpage.html')

@app.route("/textcharta"+key)
def textcharta():
    filea = open("humiddataA","r")
    fileastr = filea.read()
    filea.close()
    return render_template('textchart.html', text=fileastr)

@app.route("/textchartb"+key)
def textchartb():
    fileb = open("humiddataB","r")
    filebstr = fileb.read()
    fileb.close()
    return  render_template('textchart.html', text=filebstr)

@app.route("/chartdata"+key, methods=['GET','POST'])
def chartdata():
    return render_template('chartsetup.html')

#https://github.com/cwalk/Pi-Temp/blob/master/lab_app/lab_app.py
@app.route("/current_temp")
def lab_temp():
    import sys
    import Adafruit_DHT
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 17)
    temperature = temperature * 9/5.0 + 32
    if humidity is not None and temperature is not None:
        return render_template("current_temp.html",temp=temperature,hum=humidity)
    else:
        return render_template("no_sensor.html")
