import csv
import os

fileDir = ...
fileName = ...
file = os.path.join(fileDir, fileName)
if not os.path.exists(fileDir):
os.makedirs(fileDir)
if os.path.exists(file):
os.path.remove(file)
f = open(file, 'wb+')
writer = csv.writer(f)
writer.writelines(data)
f.close()
