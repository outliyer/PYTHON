import csv
import os 
import matplotlib.pyplot as plt
#reading the data from the csv file
with open("cars.csv","r")as f:
    csv_reader=csv.DictReader(f)
    cars=list(csv_reader)
 #getting the horse 
# power and torque of the cars using list compresion
horse_power=[int(car['Horsepower']) for car in cars]
torque=[int (car['Torque'])for car in cars]
#program for vilzvilization as scattering
fig,ax=plt.subplots()
ax.scatter(horse_power,torque,alpha=0.15
,c='black')
ax.set_title("horse_power vs torque")
ax.set_xlabel("horse_power")
ax.set_ylabel("torque")
plt.show()
