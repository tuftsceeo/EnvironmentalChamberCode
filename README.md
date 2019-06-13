# EnvironmentalChamberCode
Walker Wind's code for humidity sensors, flask website setup, and html templates
6/13/19
Chris and Ethan's Lab

Files in the repository:

humidsensors.py ::  
    When run, this program records humidity and temperature sensor data using the Adafruit DHT library, and outputs a two text files and a     jpg file. The two text files, titled humiddataA and humiddataB, have a text chart that displays the exact numbers of each data point.
    The jpg file is a chart with four subplots displaying the data using the python library matplotlib
    To run, use the command line input:
    
    $python humidsensors.py
humidwebsite.py ::  
    This code is used to set up the flask web server. Using the flask library, it implements several pages connected to the local webserver     that the Raspberry Pi puts out on the network it is connected to. The website has a couple different pages
    
    $sudo FLASK_APP=humidwebsite.py flask --host=0.0.0.0 --port=80
    
indexpage.html ::  
  This is html code used to design a template for the index page
chartdata.html ::  
  This is html code used to display an image

textchart.html ::  
  This is html code used to display a text file
