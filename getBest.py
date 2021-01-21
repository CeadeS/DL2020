import glob
import csv
import re
from pathlib import Path

csvFileList = Path('./').rglob('*.csv')
fNameRegex = re.compile(r'(?:.*/)?(.*)(?:\.csv$)')
showLines = (1,5,20,40,80,200)
bestList = {}
for k in showLines:
    bestList[k] = []

for filePath in csvFileList:
    fName = fNameRegex.search(filePath.name).groups()[0]
    # print('=== FILE:', fName," ===")
    with open(filePath.absolute(), 'r') as file:
        csvreader = csv.reader(file, delimiter=',')
        for row in csvreader:
            try:
                if row[0].isdecimal() and int(row[0])+1 in showLines:
                    # print(int(row[0])+1, ',', row[3])
                    bestList[int(row[0])+1].append((float(row[3]),fName,))
            except:
                print('Error in file:', fName, ' - Not all lines from this file were processed.')

# pretty inefficient, but easier to type
showMax = 10
for k in showLines:
    bestList[k].sort(key=lambda x: x[0], reverse=True)
    print(f'\n=== TOP {showMax} in {k} EPOCH(S) ===')
    for i in range(0,showMax):
        print(bestList[k][i][0],'\t',bestList[k][i][1])