# density of showers

from datetime import datetime

import matplotlib.pyplot as plt

fileName = "0.1.1_07_2011-22_01_2012_allCSV.txt"

fileVar = open(fileName)

density = []
line1 = fileVar.readline().split(',')[0:2]
print("LINE1: ", line1)
dateStr = line1[0] + ',' + line1[1][0:2]
print("DATEstr: " + dateStr)
currentdate_object = datetime.strptime(dateStr, '%Y/%m/%d,%H')
count = 1
numberofHitsY = []
datesX = []
for x in fileVar:
    y = x.split(',')
    dateStr = y[0] + ',' + y[1][0:2]
    newdate_object = datetime.strptime(dateStr, '%Y/%m/%d,%H')
    if newdate_object == currentdate_object:
        count += 1
    else:
        datesX.append(currentdate_object)
        numberofHitsY.append(count)
        currentdate_object = newdate_object
        count = 1

fig, ax = plt.subplots()
print(len(numberofHitsY))
ax.set_ylabel('Number of Hits per Hour')
ax.set_xlabel('Time')
ax.set_title('Number of Hits per Hour VS. Time')

ax.set_ylim(ymin=0, ymax=200)
print(len(numberofHitsY))
# plt.plot(datesX, numberofHitsY)
plt.scatter(datesX, numberofHitsY)
plt.show()
