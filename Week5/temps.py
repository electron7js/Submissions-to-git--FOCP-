from sys import argv
from statistics import mean

tempsin=argv[1:]
temps=list()
if len(tempsin):
    for i in tempsin:
        temp=float(i)
        temps.append(temp)
    print("max : ",max(temps),"min :",min(temps),"mean : ",round(mean(temps),2))
else :
    print("Please pass in some temperatures.")