#Walker Wind
#6/9/19
#Humidity Sensors Python Code  
#This code is used to read humidity sensors and display 
#the data on a chart over the period of 7 days.
#The humidity and temperature data is recorded every minute

#current problems
#saving a blank jpg instead of the chart
#wrong celsius to farenheit conversion

import time
import Adafruit_DHT as dht
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


print('Input test number that will be placed at the end of your files: ')
datakey= str(input())

#clear data files before use
open("humiddataA","w").close()
open("humiddataB","w").close()

#open datafiles for sensors A and B
dataA = open("humiddataA", "a+")
dataB = open("humiddataB", "a+")

#opens a set of datafiles that will be a copy of the data that is saved every test
abspathcopy = '/home/pi/HumiditySensors/datarecords/'
dataAcopy = open(abspathcopy+ "humiddataA" + datakey,"a+")
dataBcopy = open(abspathcopy+ "humiddataB" + datakey,"a+")

#Take command line input for setting the time of the test

print('Set length of time for humidity test in minutes: \n ')

#converts the input time from minutes to seconds
testlength= int(60*float(input()))

#sets length for data lists
huma=[0]*(testlength)
tempa=[0]*(testlength)
humb=[0]*(testlength)
tempb=[0]*(testlength)
timelist=[0]*(testlength)


print('\n Test Beginning \n')

#read_retry refreshes every two seconds
#for loop populates lists with data using read_retry(sensor,GPIOpin)
#appends the data to text files
#creates as many datapoints as it can in the alotted time

starttime= time.time()
currenttime= time.time()
i=0
while currenttime-starttime <= testlength:
    huma[i],tempa[i] = dht.read_retry(dht.DHT22,4)
    humb[i],tempb[i] = dht.read_retry(dht.DHT22,17)
    tempa[i] = 9*(tempa[i])/5 + 32
    tempb[i] = 9*(tempb[i])/5 + 32
    currenttime=time.time()
    timelist[i]=currenttime-starttime
    if(int(timelist[i])%5 == 0):
        print('Time in test: '+ str(int(timelist[i])))
    dataA.write('Time = {0:0.1f}s   Temp = {1:0.1f}*F   Humidity = {2:0.1f}%\n'.format(timelist[i], tempa[i], huma[i]))
    dataB.write('Time = {0:0.1f}s   Temp = {1:0.1f}*F   Humidity = {2:0.1f}%\n'.format(timelist[i],tempb[i], humb[i]))
    dataAcopy.write('Time = {0:0.1f}s   Temp = {1:0.1f}*F   Humidity = {2:0.1f}%\n'.format(timelist[i], tempa[i], huma[i]))
    dataBcopy.write('Time = {0:0.1f}s   Temp = {1:0.1f}*F   Humidity = {2:0.1f}%\n'.format(timelist[i],tempb[i], humb[i]))
    i=i+1

#trims the zeros off of the ends of the data lists
huma=np.trim_zeros(huma)
tempa=np.trim_zeros(tempa)
humb=np.trim_zeros(humb)
tempb=np.trim_zeros(tempb)

#makes sure that the time list and the data lists are the same length
timelist=timelist[0:(len(huma))]

#Plotting the data using matplotlib
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(timelist, huma)
axs[0, 0].set_title('Sample A')
axs[0, 0].set_ylabel('Humidity')
axs[0, 0].set_ylim([0,105])

axs[0, 1].plot(timelist, humb, 'tab:orange')
axs[0, 1].set_title('Sample B')
axs[0, 1].set_ylim([0,105])

axs[1, 0].plot(timelist, tempa, 'tab:green')
axs[1, 0].set_ylabel('Temperature')
axs[1, 0].set_xlabel('Time')
axs[1, 0].set_ylim([45,115])

axs[1, 1].plot(timelist, tempb, 'tab:red')
axs[1, 1].set_xlabel('Time')
axs[1, 1].set_ylim([45, 115])

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

abspathfig='/home/pi/HumiditySensors/static/'

plt.savefig(abspathfig + 'datachart.png')
Image.open(abspathfig + 'datachart.png').save(abspathfig + 'datachart.jpg','JPEG')
plt.savefig(abspathcopy + 'datachart'+datakey+'.png')
Image.open(abspathcopy + 'datachart'+datakey+'.png').save(abspathfig+'datachart'+datakey+'.jpg','JPEG')


dataA.close()
dataB.close()
dataAcopy.close()
dataBcopy.close()

