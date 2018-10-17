'''
Created on Oct 9, 2018

@author: catiegrasse
'''

import re
import csv

# Code to convert NSQIP data to binary signals 

INT_REGEX = "^[0-9]*$"
READMISSION_REGEX = "^.*READM.*$"
REOPERATION_REGEX = "^.*REOP.*$"
NEGATIVE_REOPERATION_VALUES = ["NULL", "-99", "No"]

FILE_NAME= "testingProcessor.csv"

# open files and remove headers
f14 = open("acs_nsqip_puf14.txt", "rb")
f15 = open("acs_nsqip_puf15_v2.txt", "rb")
f16 = open("acs_nsqip_puf16.txt", "rb")


for line in f14:
    headers14 = line.split("\t")
    break

for line in f15:
    headers15 = line.split("\t")
    break

for line in f16:
    headers16 = line.split("\t")
    break

readmissionRegex = re.compile(READMISSION_REGEX)
readmissionIndices14 = []
for i in range(len(headers14)):
    if readmissionRegex.match(headers14[i]):
        readmissionIndices14.append(i)

readmissionRegex = re.compile(READMISSION_REGEX)
readmissionIndices15 = []
for i in range(len(headers15)):
    if readmissionRegex.match(headers15[i]):
        readmissionIndices15.append(i)

readmissionRegex = re.compile(READMISSION_REGEX)
readmissionIndices16 = []
for i in range(len(headers16)):
    if readmissionRegex.match(headers16[i]):
        readmissionIndices16.append(i)

with open(FILE_NAME, mode='w') as filter_file:
    csv_writer = csv.writer(filter_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    # write headers to file
    
    ageIndex14 = headers14.index("Age")
    sexIndex14 = headers14.index("SEX")

    ageIndex15 = headers15.index("Age")
    sexIndex15 = headers15.index("SEX")

    ageIndex16 = headers16.index("Age")
    sexIndex16 = headers16.index("SEX")

    intRegex = re.compile(INT_REGEX)

    for line in f14:
        line = line.split("\t")
        age = line[ageIndex14]
        sex = line[sexIndex14].strip()
        if sex == "male":
            maleBinary = 1
            femaleBinary = 0
        else:
            femaleBinary = 1
            maleBinary = 0
        
        readmissionResponses14 = [line[ind] for ind in readmissionIndices14 if line[ind] not in NEGATIVE_REOPERATION_VALUES]
        if len(readmissionResponses14) > 0:
            csv_writer.writerow([maleBinary, femaleBinary, 1])
        else:
            csv_writer.writerow([maleBinary, femaleBinary, 0])

    for line in f15:
        line = line.split("\t")
        age = line[ageIndex15]
        if sex == "male":
            maleBinary = 1
            femaleBinary = 0
        else:
            femaleBinary = 1
            maleBinary = 0
        
        readmissionResponses15 = [line[ind] for ind in readmissionIndices15 if line[ind] not in NEGATIVE_REOPERATION_VALUES]
        if len(readmissionResponses15) > 0:
            csv_writer.writerow([maleBinary, femaleBinary, 1])

        else:
            csv_writer.writerow([maleBinary, femaleBinary, 0])


    for line in f16:
        line = line.split("\t")
        age = line[ageIndex16]
        sex = line[sexIndex16].strip()
        if sex == "male":
            maleBinary = 1
            femaleBinary = 0
        else:
            femaleBinary = 1
            maleBinary = 0
        
        readmissionResponses16 = [line[ind] for ind in readmissionIndices16 if line[ind] not in NEGATIVE_REOPERATION_VALUES]
        if len(readmissionResponses16) > 0:
            csv_writer.writerow([maleBinary, femaleBinary, 1])
        else:
            csv_writer.writerow([maleBinary, femaleBinary, 0])

