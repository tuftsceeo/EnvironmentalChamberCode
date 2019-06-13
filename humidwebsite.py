###Walker Wind 
###6/11/19
###Flask code for setting up local web server

#note to self: alt + shift + 3 shows line numbers in nano

#import necessary libraries
from flask import Flask, request, render_template, url_for
import os
CHART_FOLDER = os.path.join('static')

app= Flask(__name__)
app.config['CHART_FOLDER'] = CHART_FOLDER

#define home index
@app.route("/",methods= ['GET','POST'])
def index():
    return render_template('indexpage.html')

@app.route("/textcharta")
def textcharta():
    filea = open("humiddataA","r")
    fileastr = filea.read()
    filea.close()
    return render_template('textchart.html', text=fileastr)

@app.route("/textchartb")
def textchartb():
    fileb = open("humiddataB","r")
    filebstr = fileb.read()
    fileb.close()
    return  render_template('textchart.html', text=filebstr)

@app.route("/chartdata", methods=['GET','POST'])
def chartdata():
    return render_template('chartsetup.html')


