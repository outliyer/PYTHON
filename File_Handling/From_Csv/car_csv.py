#importing data from the csv_file
import os
import csv

 
with open("cars.csv","r")as f:
    csv_reader=csv.DictReader(f)
    content=list(csv_reader)
    #creating the another dict
car_brands={}
for car in content:
    car_brands[car['Make']]=car_brands.get(car['Make'],[])+[car['Horsepower']]
#this above lines sperates the hoursse power acording to the car brands
car_Brand={}#for brands and the avgs

for brand,car_list_hp in car_brands.items():#accesing the keys and values in dicts
    avg_hp=0#logic for the avg from the list
    for hp in car_list_hp:
        avg_hp=avg_hp+int(hp)
    car_Brand[brand]=avg_hp/len(car_list_hp)



print(car_Brand)