
import csv
import numpy

with open('mrrk.csv', newline='') as f:
  reader = csv.reader(f)
  fileData = list(reader)

fileData.pop(0)
sz = []
time = []

for i in range(len(fileData)):
  size = fileData[i][1]
  tim = fileData[i][2]
  sz.append(float(size))
  time.append(float(tim))

coefficient = numpy.corrcoef(sz, time)
print(round(coefficient[0,1], 1))

with open('cup.csv', newline='') as x:
  reader = csv.reader(x)
  fileDat = list(reader)

fileDat.pop(0)
mrk = []
time = []

for i in range(len(fileDat)):
  marks = fileData[i][1]
  tim = fileData[i][2]
  mrk.append(float(marks))
  time.append(float(tim))

coefficient = numpy.corrcoef(mrk, time)
print(round(coefficient[0,1], 1))
