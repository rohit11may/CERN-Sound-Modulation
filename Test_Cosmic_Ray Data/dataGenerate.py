# density of showers

import pickle
from datetime import datetime
from scale import scaleNum as scale

def generateNotenumbers():
    fileName = "0.1.1_07_2011-22_01_2012_allCSV.txt"

    fileVar = open(fileName)

    line1 = fileVar.readline().split(',')[0:2]
    dateStr = line1[0] + ',' + line1[1][0:2]
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

    print(len(numberofHitsY))

    list_hits = []
    first = 0
    second = 24
    for n in range(137):
        twenty_four = numberofHitsY[first:second]
        list_hits.append(twenty_four)
        first += 24
        second += 24

    count = 0
    averages = []
    ranges = []
    for day in list_hits:
        count += 1
        average = sum(day)/len(day)
        averages.append(round(average, 0))
        ranges.append((max(day)) - min(day))

    return(averages, ranges)
noteNum = []
duration = []

def getValues():
    averages, ranges = generateNotenumbers()

    minimumA = min(averages)
    maximumA = max(averages)
    minimumR = min(ranges)
    maximumR = max(ranges)

    for a in averages:
        noteNum.append(int(round(scale(a, minimumA, maximumA, 7), 0)))
    for r in ranges:
        duration.append(int(round(scale(r, minimumR, maximumR, 16), 0)))

    return(noteNum, duration)

'''
print("NOTE  |  DURATION")
for a,b in zip(noteNum, duration):
    print(str(a) + "     |     " + str(b))
'''