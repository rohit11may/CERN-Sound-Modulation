#density of showers


from datetime import datetime

fileName = "0.1.1_07_2011-22_01_2012_allCSV.txt"

fileVar = open(fileName)


line1 = fileVar.readline().split(',')[0:2]
dateStr = line1[0] + ',' + line1[1][0:2]
currentdate_object = datetime.strptime(dateStr, '%Y/%m/%d,%H')
count = 1
numberofHitsY = []
datesX = []
for x in fileVar:
	y  = x.split(',')
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
for n in range (137):
        twenty_four = numberofHitsY[first:second]
        list_hits.append(twenty_four)
        first += 24
        second += 24

print(list_hits)

date = []
first = 0
second = 24
for n in range(137):
        twenty_four = datesX[first:second]
        date.append(twenty_four)
        first += 24
        second +=24

print(date)
        
        
        
                

'''for y in fileVar:
        x = y.split(',')
        dayStr = list(x[0])
        day = ''.join(dayStr[8:10])
        if day == '01':
                print(day)
        if day == '02':
                break'''
                

        
